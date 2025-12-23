from service import PrivateClinic
from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QMessageBox, QPushButton)

class PrivateClinicWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.private_clinic = PrivateClinic()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Частная клиника")
        self.setFixedSize(500, 150)

        layout = QVBoxLayout()

        self.btn_patient_receptions = QPushButton("список пациентов, побывавших у врача более одного раза")
        self.btn_patient_receptions.clicked.connect(self.generate_patient_receptions)
        layout.addWidget(self.btn_patient_receptions)

        self.btn_doctors_specialization = QPushButton("таблица относительной загрузки врачей по специализациям")
        self.btn_doctors_specialization.clicked.connect(self.generate_doctors_specialization)
        layout.addWidget(self.btn_doctors_specialization)

        self.setLayout(layout)

    def generate_patient_receptions(self):
        try:
            self.private_clinic.patient_receptions()
            QMessageBox.information(
                self,
                "Успех",
                "Файл успешно создан"
            )
        except Exception as e:
            QMessageBox.information(
                self,
                "Успех",
                f"Ошибка при создании файла: {e}"
            )

    def generate_doctors_specialization(self):
        try:
            self.private_clinic.doctors_specialization()
            QMessageBox.information(
                self,
                "Успех",
                "Файл успешно создан"
            )
        except Exception as e:
            QMessageBox.information(
                self,
                "Успех",
                f"Ошибка при создании файла: {e}"
            )











