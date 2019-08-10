from pymongo import MongoClient

from config import TREATMENT_DOCUMENT_TYPE, PATIENT_DOCUMENT_TYPE


class MongoConfig:
    MONGO_PORT = 27017
    DB_NAME = "tailormed"
    PATIENT_COLLECTION = "patient"
    TREATMENT_COLLECTION = "treatment"


class DalMongo:
    def __init__(self, db_addr: str):
        self.client = MongoClient(db_addr, MongoConfig.MONGO_PORT)

    def is_document_exits(self, patient_id: int, document_type: str) -> bool:
        """
        This method checks if the document exists in a specific collection
        :param patient_id:
        :param document_type:
        :return:
        """
        collection = self._get_collection(document_type)
        if collection.find_one({"patient_id": patient_id}) is not None:
            return True
        return False

    def insert_many_documents(self, documents: list, document_type: str):
        collection = self._get_collection(document_type)
        collection.insert_one(documents)

    def update_document(self, document: dict, document_type: str, patient_id: int) -> bool:
        collection = self._get_collection(document_type)
        collection.replaceOne({"patient_id": patient_id}, document)
        return True

    def _get_collection(self, document_type: str):
        """
        This method returns the correct colletion
        :param document_type: The medical document type
        :return:
        """
        if document_type == TREATMENT_DOCUMENT_TYPE:
            return self.client[MongoConfig.DB_NAME][MongoConfig.TREATMENT_COLLECTION]
        elif document_type == PATIENT_DOCUMENT_TYPE:
            return self.client[MongoConfig.DB_NAME][MongoConfig.PATIENT_COLLECTION]
        else:
            raise Exception(f"Bad Document type: {document_type}")