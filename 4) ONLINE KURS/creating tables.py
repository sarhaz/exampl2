from base import Database


def creating_tables():
    payment = f"""CREATE TABLE payment(
    id SERIAL PRIMARY KEY,
    amount FLOAT,
    payment_type VARCHAR(20),
    last_updated TIMESTAMP DEFAULT now());
    """

    country = f"""CREATE TABLE country(
        id SERIAL PRIMARY KEY,
        name TEXT,
        last_updated TIMESTAMP DEFAULT now());
    """

    city = f"""CREATE TABLE city(
        id SERIAL PRIMARY KEY,
        name TEXT,
        country_id INT REFERENCES country(id),
        last_updated TIMESTAMP DEFAULT now());
        """

    mentor = f"""CREATE TABLE mentor(
            id SERIAL PRIMARY KEY,
            first_name TEXT,
            last_name TEXT,
            password TEXT,
            rating FLOAT,
            birth_date DATE,
            last_updated TIMESTAMP DEFAULT now());
            """

    lesson = f"""CREATE TABLE lesson(
            id SERIAL PRIMARY KEY,
            name TEXT,
            description TEXT,
            period_hours FLOAT,
            last_updated TIMESTAMP DEFAULT now());
            """

    modul = f"""CREATE TABLE modul(
                id SERIAL PRIMARY KEY,
                name TEXT,
                description TEXT,
                number_lessons INT,
                lesson_id INT REFERENCES lesson(id),
                period_months FLOAT,
                last_updated TIMESTAMP DEFAULT now());
                """

    speciality = f"""CREATE TABLE speciality(
            id SERIAL PRIMARY KEY,
            name TEXT,
            description text,
            last_updated TIMESTAMP DEFAULT now());
            """

    mentor_course = f"""CREATE TABLE mentor_course(
                    id SERIAL PRIMARY KEY,
                    mentor_id INT REFERENCES mentor(id),
                    course_id INT REFERENCES course(id),
                    last_updated TIMESTAMP DEFAULT now()
                    );"""

    speciality_course = f"""CREATE TABLE speciality_course(
            id SERIAL PRIMARY KEY,
            speciality_id INT REFERENCES speciality(id),
            course_id INT REFERENCES course(id),
            last_updated TIMESTAMP DEFAULT now()
            );"""

    basket = f"""CREATE TABLE basket(
                    id SERIAL PRIMARY KEY,
                    student_id INT REFERENCES student(id),
                    course_id INT REFERENCES course(id),
                    last_updated TIMESTAMP DEFAULT now());"""

    student = f"""CREATE TABLE student(
                id SERIAL PRIMARY KEY,
                first_name TEXT,
                last_name TEXT,
                email TEXT,
                balance FLOAT,
                last_updated TIMESTAMP DEFAULT now(),
                birth_date date,
                payment_id INT REFERENCES payment(id),
                password text,
                city_id INT REFERENCES city(id));
                """


    data_tables = {
        "payment": payment,
        "country": country,
        "city": city,
        "mentor": mentor,
        "lesson": lesson,
        "modul": modul,
        "mentor_course": mentor_course,
        "speciality_course": speciality_course,
        "basket": basket,
        "student": student
    }

    for i in data_tables:
        print(f"{i} {Database.connect(data_tables[i], "create")}")


if __name__ == "__main__":
    creating_tables()