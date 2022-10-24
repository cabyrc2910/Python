import sqlite3
from sqlite3 import Error


DB_NAME = "school.db"


def connect():
    try:
        con = sqlite3.connect(DB_NAME)
        return con
    except Error:
        print(Error)
        raise Error


def init():
    conn = connect()
    print(f'Connected to database {DB_NAME}')
    studentsTable = """CREATE TABLE IF NOT EXISTS students(
            id INTEGER primary key autoincrement,
            name text not null,
            lastname text not null,
            birthdate date not null
            )"""
    conn.execute(studentsTable)
    classRoomsTable = """CREATE TABLE IF NOT EXISTS classrooms(
            number int primary key
            )"""
    conn.execute(classRoomsTable)
    classesTable = """CREATE TABLE IF NOT EXISTS classes(
            id INTEGER primary key autoincrement,
            title text not null
            )"""
    conn.execute(classesTable)
    placesTable = """CREATE TABLE IF NOT EXISTS places(
            id INTEGER primary key autoincrement,
            row int not null,
            cell int not null,
            variant int not null,
            classroom_number int not null,
            FOREIGN KEY(classroom_number) REFERENCES classrooms(number)
            )"""
    conn.execute(placesTable)
    classAndStudentsTable = """CREATE TABLE IF NOT EXISTS class_students(
            class_number int not null,
            student_id int not null,
            FOREIGN KEY(class_number) REFERENCES classes(number),
            FOREIGN KEY(student_id) REFERENCES students(id)
            )"""
    conn.execute(classAndStudentsTable)
    studentsOnPlaceTable = """CREATE TABLE IF NOT EXISTS students_on_place(
            id INTEGER primary key autoincrement,
            student_id int not null,
            place_id int not null,
            took_at timestamp not null,
            free_at timestamp,
            FOREIGN KEY(student_id) REFERENCES students(id),
            FOREIGN KEY(place_id) REFERENCES places(id)
            )"""
    conn.execute(studentsOnPlaceTable)
    conn.commit()
    conn.close()
