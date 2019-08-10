import csv
import pydoc
import time
import re

from data_importer.ftp_document_worker import FtpDocumentWorker
from dal.dal_mongo import DalMongo
import config


class DataImportFormats:
    MODULE_IMPORT_FORMAT = "hospitals_data_format.{hospital_name}_data_format.{hospital_name}_{data_type}_format"
    CLASS_IMPORT_FORMAT = "{hospital_name_cap}{data_type_cap}Format"


class BackupConfig:
    BACKUP = "backup"
    CORRUPTED = "bad"


DOCUMENT_RE = r"(\w+)_(\w+)"


class ImportManager:
    def __init__(self):
        self.ftp_document_worker = FtpDocumentWorker(config.FTP_ROOT_DIRECTORY, config.FTP_DATA_SUFFIX)
        self.dal = DalMongo(config.MongoAddr)

    def run(self):
        """
        This method takes all the patient documents every configured interval, parses them, stores them in the db
        and backs them up.
        """
        while True:
            new_patient_documents = self.ftp_document_worker.get_files()
            for patient_document in new_patient_documents:
                if self._handle_patient_document(patient_document):
                    self._move_and_backup(patient_document)
                else:
                    self._move_and_backup_corrupted(patient_document)
            time.sleep(config.MAIN_LOOP_TIME_INTERVAL)

    def _handle_patient_document(self, patient_document: str) -> bool:
        """
        This method takes each patient document, parses it and insert/updates it in the db.
        :return: True if handled successfully, else False.
        """
        hospital_name, document_type = self._get_hospital_name_and_document_type(patient_document)
        bulk_normalized_data = []
        with open(patient_document, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            try:
                for row in reader:
                    normalized_data = self._get_normalized_data(hospital_name, document_type, row)
                    if self.dal.is_document_exits(normalized_data["patient_id"], document_type):
                        self.dal.update_document(normalized_data, document_type, normalized_data["patient_id"])
                    else:
                        bulk_normalized_data.append(normalized_data)

                    if len(bulk_normalized_data) >= config.BULK_NORAMLIZED_DATA_SIZE:
                        self.dal.insert_many_documents(bulk_normalized_data, document_type)

                if len(bulk_normalized_data) > 0:
                    self.dal.insert_many_documents(bulk_normalized_data, document_type)
            except Exception as e:
                print(str(e))
                return False
        return True

    def _move_and_backup(self, patient_document: str):
        """
        This method moves documents to the backup folder.
        :return: True if moved successfully, else False.
        """
        self.ftp_document_worker.move_file(patient_document, BackupConfig.BACKUP)

    def _move_and_backup_corrupted(self, patient_document: str):
        """
        This method moves a document to the corrupted backup folder.
        :return: True if moved successfully, else False.
        """
        self.ftp_document_worker.move_file(patient_document, BackupConfig.CORRUPTED)

    def _get_normalized_data(self, hospital_name: str, data_type: str, unparsed_patient_data: dict) -> dict:
        """
        This method gets the correct class format from the name and the data type, and returns the parsed data.
        :param hospital_name: Hospitals name, low chars
        :param data_type: Document type, low chars
        :param unparsed_patient_data: Unparsed patient data
        :return:
        """
        module_name = DataImportFormats.MODULE_IMPORT_FORMAT.format(hospital_name=hospital_name, data_type=data_type)
        class_name = DataImportFormats.CLASS_IMPORT_FORMAT.format(hospital_name_cap=hospital_name.title(),
                                                                  data_type_cap=data_type.title())
        my_module = pydoc.locate(module_name)
        suitable_format_class = getattr(my_module, class_name)
        instance = suitable_format_class(unparsed_patient_data)
        return instance.get_normalized_data()

    def _get_hospital_name_and_document_type(self, document_name) -> list:
        """
        This method gets the hospital and document type from the document name with regex.
        :param document_name: Document name
        :return:
        """
        re_object = re.search(DOCUMENT_RE, document_name)
        return [group.lower() for group in re_object.groups()]
