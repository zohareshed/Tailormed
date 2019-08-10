from hospitals_data_format.base_format import BaseFormat


class Hospital_2TreatmentFormat(BaseFormat):
    def __init__(self, unparsed_patient_data: dict):
        super().__init__(unparsed_patient_data["PatientId"])
        self.start_date = unparsed_patient_data["StartDate"]
        self.end_date = unparsed_patient_data["EndDate"]
        self.protocol_id = unparsed_patient_data["ProtocolID"]
        self.display_name = unparsed_patient_data["DisplayName"]
        self.associated_diagnoses = unparsed_patient_data["AssociatedDiagnoses"]
        self.status = unparsed_patient_data["Status"]
        self.number_of_cycles = unparsed_patient_data["NumberOfCycles"]
        self.treatment_id = unparsed_patient_data["TreatmentId"]

    def get_normalized_data(self) -> dict:
        pass