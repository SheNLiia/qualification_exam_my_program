class Reception:
    """
        Модуль Приёмы
    """
    def __init__(self, reception_id: int, doctor_id: int, patient_id: int, date: str, time: str, diagnosis_id: int):
        self.reception_id = reception_id
        self.doctor_id = doctor_id
        self.patient_id = patient_id
        self.date = date
        self.time = time
        self.diagnosis_id = diagnosis_id

    def __str__(self):
        return f"{self.reception_id};{self.doctor_id};{self.patient_id};{self.date};{self.time};{self.diagnosis_id}"

    def __repr__(self):
        return self.__str__()
