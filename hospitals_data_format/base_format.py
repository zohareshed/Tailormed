from abc import ABC, abstractmethod


class BaseFormat(ABC):
    def __init__(self, patient_id: int):
        self.patient_id = patient_id

    @abstractmethod
    def get_normalized_data(self) -> dict:
        pass
