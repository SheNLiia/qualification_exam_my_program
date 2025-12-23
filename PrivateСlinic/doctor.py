class Doctor:
    """
        Модуль Доктор
    """
    def __init__(self, doctor_id: int, doctor_fio: str, doctor_specialization: str):
        self.doctor_id = doctor_id
        self.doctor_fio = doctor_fio
        self.doctor_specialization = doctor_specialization

    def __str__(self):
        return f"{self.doctor_id};{self.doctor_fio};{self.doctor_specialization}"

    def __repr__(self):
        return self.__str__()