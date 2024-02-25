from base import Database


class Base:
    @staticmethod
    def select(table):
        query = f"""SELECT * FROM {table} """
        return Database.connect(query, "select")

    @staticmethod
    def delete(table, column, column_data):
        query = f"""DELETE FROM {table} WHERE {column} = {column_data}"""
        return Database.connect(query, "delete")

    @staticmethod
    def update(table, column, new_data, where_column, where_row):
        query = f"""UPDATE {table} SET {column} = '{new_data}' WHERE {where_column} = '{where_row}' """
        return Database.connect(query, "update")


class Country(Base):
    def __init__(self, name: str, created_date: str):
        self.name = name
        self.created_date = created_date

    def insert(self, table):
        query = f"""INSERT INTO {table}(name,created_date) VALUES ('{self.name}', '{self.created_date}')"""
        return Database.connect(query, "insert")


class City(Country):
    def __init__(self, name: str, country_id: int, created_date: str):
        super().__init__(name, created_date)
        self.country_id = country_id

    def insert(self, table):
        query = f"""INSERT INTO {table}(name,country_id,created_date) VALUES ('{self.name}',{self.country_id} '{self.created_date}')"""
        return Database.connect(query, "insert")


class Payment(Base):
    def __init__(self, amount: float, payment_type: str):
        self.amount = amount
        self.payment_type = payment_type

    def insert(self, table):
        query = f"""INSERT INTO {table}(amount,payment_type) VALUES ({self.amount}, '{self.payment_type}')"""
        return Database.connect(query, "insert")


class Mentor(Base):
    def __init__(self, first_name: str, last_name: str, password: str, rating: float, birth_date: str):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.rating = rating
        self.birth_date = birth_date

    def insert(self, table):
        query = f"""INSERT INTO {table}(first_name,last_name,password,rating,birth_date) VALUES ('{self.first_name}', '{self.last_name}', '{self.password}','{self.rating}', '{self.birth_date}')"""
        return Database.connect(query, "insert")


class Lesson(Base):
    def __init__(self, name: str, description: str, period_hours: float):
        self.name = name
        self.description = description
        self.period_hours = period_hours

    def insert(self, table):
        query = f"""INSERT INTO {table}(name,description,period_hours) VALUES ('{self.name}', '{self.description}', {self.period_hours})"""
        return Database.connect(query, "insert")


class Modul(Base):
    def __init__(self, name: str, description: str, number_lessons: int, lesson_id: int, period_months: float):
        self.name = name
        self.description = description
        self.number_lessons = number_lessons
        self.lesson_id = lesson_id
        self.period_months = period_months

    def insert(self, table):
        query = f"""INSERT INTO {table}(name,description,number_lessons,lesson_id,period_months) VALUES ('{self.name}', '{self.description}', {self.number_lessons},{self.lesson_id},{self.period_months})"""
        return Database.connect(query, "insert")


class Speciality(Base):
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def insert(self, table):
        query = f"""INSERT INTO {table}(name,description) VALUES ('{self.name}', '{self.description}')"""
        return Database.connect(query, "insert")


class Course(Base):
    def __init__(self, name: str, description: str, language: str, price: str, rating: float):
        self.name = name
        self.description = description
        self.language = language
        self.price = price
        self.rating = rating

    def insert(self, table):
        query = f"""INSERT INTO {table}(name,description,language,price,rating) VALUES ('{self.name}', '{self.description}', '{self.language}', '{self.price}', {self.rating})"""
        return Database.connect(query, "insert")


class MentorCourse(Base):
    def __init__(self, mentor_id: int, course_id: int):
        self.mentor_id = mentor_id
        self.course_id = course_id

    def insert(self, table):
        query = f"""INSERT INTO {table}(mentor_id,course_id) VALUES ({self.mentor_id}, {self.course_id})"""
        return Database.connect(query, "insert")


class SpecialityCourse(Base):
    def __init__(self, speciality_id: int, course_id: int):
        self.speciality_id = speciality_id
        self.course_id = course_id

    def insert(self, table):
        query = f"""INSERT INTO {table}(speciality_id,course_id) VALUES ({self.speciality_id}, {self.course_id})"""
        return Database.connect(query, "insert")


class Basket(Base):
    def __init__(self, student_id: int, course_id: int):
        self.student_id = student_id
        self.course_id = course_id

    def insert(self, table):
        query = f"""INSERT INTO {table}(student_id,course_id) VALUES ({self.speciality_id}, {self.course_id})"""
        return Database.connect(query, "insert")


class Student(Base):
    def __init__(self, first_name: str, last_name: str, email: str, balance: float, birth_date: str, payment_id: int, password: str, city_id: int):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.balance = balance
        self.birth_date = birth_date
        self.payment_id = payment_id
        self.password = password
        self.city_id = city_id

    def insert(self, table):
        query = f"""INSERT INTO {table}(first_name,last_name,email,balance,birth_date,payment_id,password,city_id) VALUES ('{self.first_name}', '{self.last_name}','{self.email}', {self.balance}, '{self.birth_date}', {self.payment_id}, '{self.password}', {self.city_id})"""
        return Database.connect(query, "insert")


# if __name__ == "__main__":
#     print(Payment.select("payment"))
