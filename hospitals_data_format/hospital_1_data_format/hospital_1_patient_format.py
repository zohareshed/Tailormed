import datetime

from hospitals_data_format.base_format import BaseFormat
from config import PatientFormatConfig, ABBREV_TO_STATE
from hospitals_data_format.invalid_data_error import InvalidDataError

PATIENT_DOB_TIME_FORMAT = '%m/%d/%Y %H:%M'


class Hospital_1PatientFormat(BaseFormat):
    def __init__(self, unparsed_patient_data: dict):
        super().__init__(unparsed_patient_data["PatientID"])
        self.mrn = unparsed_patient_data["MRN"]
        self.patient_dob = unparsed_patient_data["PatientDOB"]
        self.is_deceased = unparsed_patient_data["IsDeceased"]
        self.dod_ts = unparsed_patient_data["DOD_TS"]
        self.last_name = unparsed_patient_data["LastName"]
        self.first_name = unparsed_patient_data["FirstName"]
        self.gender = unparsed_patient_data["Gender"]
        self.sex = unparsed_patient_data["Sex"]
        self.address = unparsed_patient_data["Address"]
        self.city = unparsed_patient_data["City"]
        self.state = unparsed_patient_data["State"]
        self.zip_code = unparsed_patient_data["ZipCode"]
        self.last_modified_date = unparsed_patient_data["LastModifiedDate"]

    def _get_normalized_patient_dob(self):
        try:
            return datetime.datetime.strptime(self.patient_dob, PATIENT_DOB_TIME_FORMAT)
        except KeyError:
            raise InvalidDataError(f"Bad date format: {self.patient_dob}")

    def _get_normalized_state(self):
        try:
            return ABBREV_TO_STATE[self.state]
        except KeyError:
            raise InvalidDataError(f"State does not exists: {self.state}")

    def get_normalized_data(self) -> dict:
        normalized_data = {
            PatientFormatConfig.PATIENT_ID: self.patient_id,
            PatientFormatConfig.MRN: self.mrn,
            PatientFormatConfig.DATE_OF_BIRTH: self._get_normalized_patient_dob(),
            PatientFormatConfig.IS_DECEASED: self.is_deceased,
            PatientFormatConfig.DATE_OF_DEATH: self.dod_ts,
            PatientFormatConfig.FIRST_NAME: self.first_name,
            PatientFormatConfig.LAST_NAME: self.last_name,
            PatientFormatConfig.GENDER: self.gender,
            PatientFormatConfig.SEX: self.sex,
            PatientFormatConfig.STREET_ADDRESS: self.address,
            PatientFormatConfig.CITY: self.city,
            PatientFormatConfig.STATE: self._get_normalized_state(),
            PatientFormatConfig.ZIP_CODE: self.zip_code
        }
        return normalized_data

