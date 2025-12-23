class Diagnosis:
    """
        Модуль Диагноз
    """
    def __init__(self, diagnosis_id: int, diagnosis_name: str, diagnosis_treatment: str):
        self.diagnosis_id = diagnosis_id
        self.diagnosis_name = diagnosis_name
        self.diagnosis_treatment = diagnosis_treatment

    def __str__(self):
        return f"{self.diagnosis_id};{self.diagnosis_name};{self.diagnosis_treatment}"

    def __repr__(self):
        return self.__str__()