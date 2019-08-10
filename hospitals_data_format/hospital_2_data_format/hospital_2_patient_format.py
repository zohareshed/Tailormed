import datetime

from hospitals_data_format.base_format import BaseFormat
from hospitals_data_format.invalid_data_error import InvalidDataError
from config import PatientFormatConfig

PATIENT_DOB_TIME_FORMAT = '%d/%m/%Y'
UNPARSED_TO_NORMALIZE_DECEASE_STATUS = {
    "Y": "Active",
    "N": "Deceased"
}


class Hospital_2PatientFormat(BaseFormat):
    def __init__(self, unparsed_patient_data: dict):
        super().__init__(unparsed_patient_data["PatientId"])
        self.mrn = unparsed_patient_data["MRN"]
        self.patient_dob = unparsed_patient_data["PatientDOB"]
        self.is_patient_deceased = unparsed_patient_data["IsPatientDeceased"]
        self.death_date = unparsed_patient_data["DeathDate"]
        self.last_name = unparsed_patient_data["LastName"]
        self.first_name = unparsed_patient_data["FirstName"]
        self.gender = unparsed_patient_data["Gender"]
        self.sex = unparsed_patient_data["Sex"]
        self.address_line = unparsed_patient_data["AddressLine"]
        self.address_city = unparsed_patient_data["AddressCity"]
        self.address_state = unparsed_patient_data["AddressState"]
        self.address_zip_code = unparsed_patient_data["AddressZipCode"]

    def _get_normalized_patient_dob(self):
        try:
            return datetime.datetime.strptime(self.patient_dob, PATIENT_DOB_TIME_FORMAT)
        except KeyError:
            raise InvalidDataError(f"Bad date format: {self.patient_dob}")

    def _get_normalized_deceased_status(self):
        try:
            return UNPARSED_TO_NORMALIZE_DECEASE_STATUS[self.is_patient_deceased]
        except KeyError:
            raise InvalidDataError(f"Bad decease status: {self.is_patient_deceased}")

    def get_normalized_data(self) -> dict:
        normalized_data = {
            PatientFormatConfig.PATIENT_ID: self.patient_id,
            PatientFormatConfig.MRN: self.mrn,
            PatientFormatConfig.DATE_OF_BIRTH: self.patient_dob,
            PatientFormatConfig.IS_DECEASED: self._get_normalized_deceased_status(),
            PatientFormatConfig.DATE_OF_DEATH: self.death_date,
            PatientFormatConfig.FIRST_NAME: self.first_name,
            PatientFormatConfig.LAST_NAME: self.last_name,
            PatientFormatConfig.GENDER: self.gender,
            PatientFormatConfig.SEX: self.sex,
            PatientFormatConfig.STREET_ADDRESS: self.address_line,
            PatientFormatConfig.CITY: self.address_city,
            PatientFormatConfig.STATE: self.address_city,
            PatientFormatConfig.ZIP_CODE: self.address_zip_code
        }
        return normalized_data
