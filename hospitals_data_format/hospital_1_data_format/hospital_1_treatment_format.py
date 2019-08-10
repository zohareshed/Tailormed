from hospitals_data_format.base_format import BaseFormat


class Hospital_1TreatmentFormat(BaseFormat):
    def __init__(self, unparsed_patient_data: dict):
        super().__init__(unparsed_patient_data["PatientID"])
        self.start_date = unparsed_patient_data["StartDate"]
        self.end_date = unparsed_patient_data["EndDate"]
        self.active = unparsed_patient_data["Active"]
        self.display_name = unparsed_patient_data["DisplayName"]
        self.diagnoses = unparsed_patient_data["Diagnoses"]
        self.treatment_line = unparsed_patient_data["TreatmentLine"]
        self.cycles_x_days = unparsed_patient_data["CyclesXDays"]
        self.treatment_id = unparsed_patient_data["TreatmentID"]

    def get_normalized_data(self) -> dict:
        pass