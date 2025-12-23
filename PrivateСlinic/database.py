import sqlite3

def get_connection():
    """
       Метод подключения к базе данных
    """
    try:
        return sqlite3.connect("private_clinic.db")
    except sqlite3.Error as e:
        print(f"Ошибка соединения с БД, {e}")