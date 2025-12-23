from service import PrivateClinic
from gui import PrivateClinicWindow
import sys
from PyQt6.QtWidgets import QApplication


def load_data():
    """
    Загрузка данных в БД
    """
    private_clinic = PrivateClinic()

    try:
        private_clinic.load_doctors()
        private_clinic.load_patients()
        private_clinic.load_diagnoses()
        private_clinic.load_receptions()

        print("Данные успешно загружены в БД")

    except Exception as e:
        print(f"Ошибка при загрузке данных: {e}")


def main():
    """
        Запуск программы
    """
    try:
        load_data()

        app = QApplication(sys.argv)
        window = PrivateClinicWindow()
        window.show()
        sys.exit(app.exec())

    except Exception as e:
        print(f"Ошибка при запуске программы: {e}")


if __name__ == "__main__":
    """
        Запуск программы
    """
    main()
