class Patient:
    """
        Модуль Пациент
    """
    def __init__(self, patient_id: int, patient_fio: str, patient_address: str):
        self.patient_id = patient_id
        self.patient_fio = patient_fio
        self.patient_address = patient_address

    def __str__(self):
        return f"{self.patient_id};{self.patient_fio};{self.patient_address}"

    def __repr__(self):
        return self.__str__()