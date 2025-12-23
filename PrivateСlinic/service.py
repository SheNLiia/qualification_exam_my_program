import json

from database import get_connection


class PrivateClinic:
    """
        Модуль Чатная клиника
    """

    def load_doctors(self, filename="doctors.txt"):
        """
            Метод загрузки данных докторов в БД
        """
        try:
            connection = get_connection()
            cursor = connection.cursor()

            with open(filename, 'r', encoding="utf-8") as file:
                for line in file:
                    doctor_id, doctor_fio, doctor_specialization = line.strip().split(';')

                    cursor.execute("INSERT OR REPLACE INTO doctors VALUES (?, ?, ?)",
                                   (int(doctor_id), doctor_fio, doctor_specialization)
                                   )
            connection.commit()
            connection.close()

        except Exception as e:
            print(f"Ошибка при загрузке данных: {e}")

    def load_patients(self, filename="patients.txt"):
        """
            Метод загрузки данных пациентов в БД
        """
        try:
            connection = get_connection()
            cursor = connection.cursor()

            with open(filename, 'r', encoding="utf-8") as file:
                for line in file:
                    patient_id, patient_fio, patient_address = line.strip().split(';')

                    cursor.execute("INSERT OR REPLACE INTO patients VALUES (?, ?, ?)",
                                   (int(patient_id), patient_fio, patient_address)
                                   )
            connection.commit()
            connection.close()

        except Exception as e:
            print(f"Ошибка при загрузке данных: {e}")

    def load_diagnoses(self, filename="diagnoses.txt"):
        """
            Метод загрузки данных диагнозов в БД
        """
        try:
            connection = get_connection()
            cursor = connection.cursor()

            with open(filename, 'r', encoding="utf-8") as file:
                for line in file:
                    diagnosis_id, diagnosis_name, diagnosis_treatment = line.strip().split(';')

                    cursor.execute("INSERT OR REPLACE INTO diagnoses VALUES (?, ?, ?)",
                                   (int(diagnosis_id), diagnosis_name, diagnosis_treatment)
                                   )
            connection.commit()
            connection.close()

        except Exception as e:
            print(f"Ошибка при загрузке данных: {e}")

    def load_receptions(self, filename="receptions.txt"):
        """
            Метод загрузки данных приёмов в БД
        """
        try:
            connection = get_connection()
            cursor = connection.cursor()

            with open(filename, 'r', encoding="utf-8") as file:
                for line in file:
                    reception_id, doctor_id, patient_id, date, time, diagnosis_id = line.strip().split(';')

                    cursor.execute("INSERT OR REPLACE INTO receptions VALUES (?, ?, ?, ?, ?, ?)",
                                   (int(reception_id), int(doctor_id), int(patient_id), date, time, int(diagnosis_id))
                                   )

            connection.commit()
            connection.close()

        except Exception as e:
            print(f"Ошибка при загрузке данных: {e}")

    def patient_receptions(self, filename="patient_receptions.json"):
        """
        Метод нахождения пациентов, побывавших у врача более одного раза
        """
        try:
            conn = get_connection()
            cur = conn.cursor()

            cur.execute("SELECT * FROM patients")
            patients = cur.fetchall()

            cur.execute("SELECT * FROM receptions")
            receptions = cur.fetchall()

            conn.close()

            # Считаю посещения
            visits = {}
            for reception in receptions:
                patient_id = reception[2]
                visits[patient_id] = visits.get(patient_id, 0) + 1

            # Формирую список пациентов с >1 посещением
            result = []
            for patient in patients:
                patient_id = patient[0]
                if visits.get(patient_id, 0) > 1:
                    result.append({
                        "id": patient_id,
                        "fio": patient[1],
                        "address": patient[2],
                        "visits": visits[patient_id]
                    })

            # Сохраняю в JSON
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(result, f, ensure_ascii=False, indent=2)

            print(f"JSON файл создан: {filename}")

        except Exception as e:
            print(f"Ошибка: {e}")

    def doctors_specialization(self, filename="doctors_specialization.json"):
        """
        Метод построения таблицы относительной загрузки врачей по специализациям
        """
        try:
            conn = get_connection()
            cur = conn.cursor()

            cur.execute("SELECT * FROM doctors")
            doctors = cur.fetchall()

            cur.execute("SELECT * FROM receptions")
            receptions = cur.fetchall()

            conn.close()

            # Считаю приемы по врачам
            doctor_counts = {}
            for reception in receptions:
                doctor_id = reception[1]
                doctor_counts[doctor_id] = doctor_counts.get(doctor_id, 0) + 1

            # прохожусь по специализациям
            specs = {}
            for doctor in doctors:
                spec = doctor[2]
                if spec not in specs:
                    specs[spec] = {"doctors": 0, "receptions": 0}

                specs[spec]["doctors"] += 1
                specs[spec]["receptions"] += doctor_counts.get(doctor[0], 0)

            # результат
            result = []
            for spec, data in specs.items():
                doctors_count = data["doctors"]
                receptions_count = data["receptions"]

                if doctors_count > 0:
                    avg = receptions_count / doctors_count
                else:
                    avg = 0

                result.append({
                    "specialization": spec,
                    "doctors": doctors_count,
                    "receptions": receptions_count,
                    "average": round(avg, 2)
                })

            # Сортирую среднюю нагрузку
            result.sort(key=lambda x: x["average"], reverse=True)

            # Сохраняю в JSON
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(result, f, ensure_ascii=False, indent=2)

            print(f"JSON файл создан: {filename}")

        except Exception as e:
            print(f"Ошибка: {e}")

