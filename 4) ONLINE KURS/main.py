from classes import Country, City, Payment, Mentor, Lesson, Modul,  Speciality, Course, MentorCourse, SpecialityCourse, Basket, Student
def services_country():
    services = input("""
1.SELECT        #####    #    #     ####     ####     ####    ######
2.INSERT      #          #    #    #    #   #    #    #       #
3.DELETE      #          ######    #    #   #    #    ####    ######
4.UPDATE      #          #    #    #    #   #    #       #    # 
0.BACK          #####    #    #     ####     ####     ####    ######

    """)
    if services == '1':
        for i in Country.select("country"):
            print(i)
        return services_country()

    elif services == '2':
        country = input("enter country name: ")
        create_date = input("enter created date: ")
        country = Country(country, create_date)
        print(country.insert("country"))
        return services_country()

    elif services == '3':
        column_name = input("enter column name: ")
        column_data = input("enter column value: ")
        print(Country.delete("country", column_name, column_data))
        return services_country()

    elif services == '4':
        column_name = input("enter the name of the column in which one do you want to change: ")
        new_data_for_column = input(f"enter the data you want to change in {column_name} column: ")
        where_column = input(f"enter the column where you want to change exactly: ")
        where_row = input(f"enter the row where you want to change exactly: ")
        print(Country.update("country", column_name, new_data_for_column, where_column, where_row))
        return services_country()

    elif services == '0':
        return main()

    else:
        print(">>>>>>WRONG BUTTON<<<<<")
        print(">>>>>>CHOOSE AGAIN<<<<<")
        return services_country()

def services_city():
    services = input("""
1.SELECT        #####    #    #     ####     ####     ####    ######
2.INSERT      #          #    #    #    #   #    #    #       #
3.DELETE      #          ######    #    #   #    #    ####    ######
4.UPDATE      #          #    #    #    #   #    #       #    # 
0.BACK          #####    #    #     ####     ####     ####    ######

        """)
    if services == '1':
        for i in City.select("country"):
            print(i)
        return services_city()

    elif services == '2':
        city_name = input("enter city name: ")
        country_id = int(input("enter id of country which this city belongs to: "))
        create_date = input("enter created date: ")
        city = City(city_name, country_id, create_date)
        print(city.insert("city"))
        return services_city()

    elif services == '3':
        column_name = input("enter column name: ")
        column_data = input("enter column value: ")
        print(City.delete("city", column_name, column_data))
        return services_city()

    elif services == '4':
        column_name = input("enter the name of the column in which one do you want to change: ")
        new_data_for_column = input(f"enter the data you want to change in {column_name} column: ")
        where_column = input(f"enter the column where you want to change exactly: ")
        where_row = input(f"enter the row where you want to change exactly: ")
        print(City.update("city", column_name, new_data_for_column, where_column, where_row))
        return services_city()

    elif services == '0':
        return main()

    else:
        print(">>>>>>WRONG BUTTON<<<<<")
        print(">>>>>>CHOOSE AGAIN<<<<<")
        return services_city()


def services_payment():
    services = input("""
1.SELECT        #####    #    #     ####     ####     ####    ######
2.INSERT      #          #    #    #    #   #    #    #       #
3.DELETE      #          ######    #    #   #    #    ####    ######
4.UPDATE      #          #    #    #    #   #    #       #    # 
0.BACK          #####    #    #     ####     ####     ####    ######

                    """)
    if services == '1':
        for i in Payment.select("payment"):
            print(i)
        return services_payment()

    elif services == '2':
        amount = float(input("enter the amount you would like to pay for: "))
        payment_type = input("write type of payment like click,payme , ipoteka, uzum and so on: ")
        payment = Payment(amount, payment_type)
        print(payment.insert("payment"))
        return services_payment()

    elif services == '3':
        column_name = input("enter column name: ")
        column_data = input("enter column value: ")
        print(Payment.delete("payment", column_name, column_data))
        return services_payment()

    elif services == '4':
        column_name = input("enter the name of the column in which one do you want to change: ")
        new_data_for_column = input(f"enter the data you want to change in {column_name} column: ")
        where_column = input(f"enter the column where you want to change exactly: ")
        where_row = input(f"enter the row where you want to change exactly: ")
        print(Payment.update("payment", column_name, new_data_for_column, where_column, where_row))
        return services_payment()


    elif services == '0':
        return main()

    else:
        print(">>>>>>WRONG BUTTON<<<<<")
        print(">>>>>>CHOOSE AGAIN<<<<<")
        return services_payment()


def services_mentor():
    services = input("""
1.SELECT        #####    #    #     ####     ####     ####    ######
2.INSERT      #          #    #    #    #   #    #    #       #
3.DELETE      #          ######    #    #   #    #    ####    ######
4.UPDATE      #          #    #    #    #   #    #       #    # 
0.BACK          #####    #    #     ####     ####     ####    ######

                            """)
    if services == '1':
        for i in Mentor.select("mentor"):
            print(i)
        return services_mentor()

    elif services == '2':
        first_name = input("enter first name: ")
        last_name = input("enter last_name: ")
        password = input("enter password: ")
        rating = float(input("enter a number up to 10 for rating: "))
        birth_date = input("enter birth day: ")
        mentor = Mentor(first_name, last_name, password, rating, birth_date)
        print(mentor.insert("mentor"))
        return services_mentor()

    elif services == '3':
        column_name = input("enter column name: ")
        column_data = input("enter column value: ")
        print(Mentor.delete("mentor", column_name, column_data))
        return services_mentor()

    elif services == '4':
        column_name = input("enter the name of the column in which one do you want to change: ")
        new_data_for_column = input(f"enter the data you want to change in {column_name} column: ")
        where_column = input(f"enter the column where you want to change exactly: ")
        where_row = input(f"enter the row where you want to change exactly: ")
        print(Mentor.update("mentor", column_name, new_data_for_column, where_column, where_row))
        return services_mentor()

    elif services == '0':
        return main()

    else:
        print(">>>>>>WRONG BUTTON<<<<<")
        print(">>>>>>CHOOSE AGAIN<<<<<")
        return services_mentor()


def services_lesson():
    services = input("""
1.SELECT        #####    #    #     ####     ####     ####    ######
2.INSERT      #          #    #    #    #   #    #    #       #
3.DELETE      #          ######    #    #   #    #    ####    ######
4.UPDATE      #          #    #    #    #   #    #       #    # 
0.BACK          #####    #    #     ####     ####     ####    ######

         """)
    if services == '1':
        for i in Lesson.select("lesson"):
            print(i)
        return services_lesson()

    elif services == '2':
        name = input("enter topic of the course: ")
        description = input("a description about the lesson: ")
        period_hours = float(input("enter period of hours for one lesson: "))
        lesson = Lesson(name, description, period_hours)
        print(lesson.insert("lesson"))
        return services_lesson()

    elif services == '3':
        column_name = input("enter column name: ")
        column_data = input("enter column value: ")
        print(Lesson.delete("lesson", column_name, column_data))
        return services_lesson()

    elif services == '4':
        column_name = input("enter the name of the column in which one do you want to change: ")
        new_data_for_column = input(f"enter the data you want to change in {column_name} column: ")
        where_column = input(f"enter the column where you want to change exactly: ")
        where_row = input(f"enter the row where you want to change exactly: ")
        print(Lesson.update("lesson", column_name, new_data_for_column, where_column, where_row))
        return services_lesson()

    elif services == '0':
        return main()

    else:
        print(">>>>>>WRONG BUTTON<<<<<")
        print(">>>>>>CHOOSE AGAIN<<<<<")
        return services_lesson()


def services_modul():
    services = input("""
1.SELECT        #####    #    #     ####     ####     ####    ######
2.INSERT      #          #    #    #    #   #    #    #       #
3.DELETE      #          ######    #    #   #    #    ####    ######
4.UPDATE      #          #    #    #    #   #    #       #    # 
0.BACK          #####    #    #     ####     ####     ####    ######

                            """)
    if services == '1':
        for i in Modul.select("modul"):
            print(i)
        return services_modul()

    elif services == '2':
        name = input("write a name of the modul: ")
        description = input("write a description about this modul: ")
        number_lesson = int(input("enter number of lesson for this modul: "))
        lesson_id = int(input(f"enter id of lesson which are exists in {name}: "))
        period_months = float(input("enter period of months how much will it take to finish the modul: "))
        modul = Modul(name, description, number_lesson, lesson_id, period_months)
        print(modul.insert("modul"))
        return services_modul()

    elif services == '3':
        column_name = input("enter column name: ")
        column_data = input("enter column value: ")
        print(Modul.delete("modul", column_name, column_data))
        return services_modul()

    elif services == '4':
        column_name = input("enter the name of the column in which one do you want to change: ")
        new_data_for_column = input(f"enter the data you want to change in {column_name} column: ")
        where_column = input(f"enter the column where you want to change exactly: ")
        where_row = input(f"enter the row where you want to change exactly: ")
        print(Modul.update("modul", column_name, new_data_for_column, where_column, where_row))
        return services_modul()

    elif services == '0':
        return main()

    else:
        print(">>>>>>WRONG BUTTON<<<<<")
        print(">>>>>>CHOOSE AGAIN<<<<<")
        return services_modul()


def services_speciality():
    services = input("""
1.SELECT        #####    #    #     ####     ####     ####    ######
2.INSERT      #          #    #    #    #   #    #    #       #
3.DELETE      #          ######    #    #   #    #    ####    ######
4.UPDATE      #          #    #    #    #   #    #       #    # 
0.BACK          #####    #    #     ####     ####     ####    ######

                """)
    if services == '1':
        for i in Speciality.select("speciality"):
            print(i)
        return services_speciality()

    elif services == '2':
        name = input("name of the speciality: ")
        description = input("write a description about the speciality: ")
        speciality = Speciality(name, description)
        print(speciality.insert("speciality"))
        return services_speciality()

    elif services == '3':
        column_name = input("enter column name: ")
        column_data = input("enter column value: ")
        print(Speciality.delete("speciality", column_name, column_data))
        return services_speciality()

    elif services == '4':
        column_name = input("enter the name of the column in which one do you want to change: ")
        new_data_for_column = input(f"enter the data you want to change in {column_name} column: ")
        where_column = input(f"enter the column where you want to change exactly: ")
        where_row = input(f"enter the row where you want to change exactly: ")
        print(Speciality.update("speciality", column_name, new_data_for_column, where_column, where_row))
        return services_speciality()

    elif services == '0':
        return main()

    else:
        print(">>>>>>WRONG BUTTON<<<<<")
        print(">>>>>>CHOOSE AGAIN<<<<<")
        return services_speciality()


def services_course():
    services = input("""
1.SELECT        #####    #    #     ####     ####     ####    ######
2.INSERT      #          #    #    #    #   #    #    #       #
3.DELETE      #          ######    #    #   #    #    ####    ######
4.UPDATE      #          #    #    #    #   #    #       #    # 
0.BACK          #####    #    #     ####     ####     ####    ######

                            """)
    if services == '1':
        for i in Course.select("course"):
            print(i)
        return services_course()

    elif services == '2':
        course_name = input("enter name of course like python,java and so on...: ")
        description = input(
            "write description about this language what kind of things can be done if person learns this language: ")
        language = input("which language: ")
        price = input("enter the price of the course: ")
        rating = float(input("enter number for rating up to 10: "))
        course = Course(course_name, description, language, price, rating)
        print(course.insert("course"))
        return services_course()

    elif services == '3':
        column_name = input("enter column name: ")
        column_data = input("enter column value: ")
        print(Course.delete("course", column_name, column_data))
        return services_course()

    elif services == '4':
        column_name = input("enter the name of the column in which one do you want to change: ")
        new_data_for_column = input(f"enter the data you want to change in {column_name} column: ")
        where_column = input(f"enter the column where you want to change exactly: ")
        where_row = input(f"enter the row where you want to change exactly: ")
        print(Course.update("course", column_name, new_data_for_column, where_column, where_row))
        return services_course()

    elif services == '0':
        return main()

    else:
        print(">>>>>>WRONG BUTTON<<<<<")
        print(">>>>>>CHOOSE AGAIN<<<<<")
        return services_course()


def services_mentor_course():
    services = input("""
1.SELECT        #####    #    #     ####     ####     ####    ######
2.INSERT      #          #    #    #    #   #    #    #       #
3.DELETE      #          ######    #    #   #    #    ####    ######
4.UPDATE      #          #    #    #    #   #    #       #    # 
0.BACK          #####    #    #     ####     ####     ####    ######

                            """)
    if services == '1':
        for i in MentorCourse.select("mentor_course"):
            print(i)
        return services_mentor_course()

    elif services == '2':
        mentor_id = int(input("enter mentor`s id: "))
        course_id = int(input("enter course`s id: "))
        mentor_course = MentorCourse(mentor_id, course_id)
        print(mentor_course.insert("mentor_course"))
        return services_mentor_course()

    elif services == '3':
        column_name = input("enter column name: ")
        column_data = input("enter column value: ")
        print(MentorCourse.delete("mentor_course", column_name, column_data))
        return services_mentor_course()

    elif services == '4':
        column_name = input("enter the name of the column in which one do you want to change: ")
        new_data_for_column = input(f"enter the data you want to change in {column_name} column: ")
        where_column = input(f"enter the column where you want to change exactly: ")
        where_row = input(f"enter the row where you want to change exactly: ")
        print(MentorCourse.update("mentor_course", column_name, new_data_for_column, where_column, where_row))
        return services_mentor_course()

    elif services == '0':
        return main()

    else:
        print(">>>>>>WRONG BUTTON<<<<<")
        print(">>>>>>CHOOSE AGAIN<<<<<")
        return services_mentor_course()


def services_speciality_course():
    services = input("""
1.SELECT        #####    #    #     ####     ####     ####    ######
2.INSERT      #          #    #    #    #   #    #    #       #
3.DELETE      #          ######    #    #   #    #    ####    ######
4.UPDATE      #          #    #    #    #   #    #       #    # 
0.BACK          #####    #    #     ####     ####     ####    ######

                            """)
    if services == '1':
        for i in SpecialityCourse.select("speciality_course"):
            print(i)
        return services_speciality_course()

    elif services == '2':
        speciality_id = int(input("enter speciality`s id: "))
        course_id = int(input("enter course`s id: "))
        speciality_course = SpecialityCourse(speciality_id, course_id)
        print(speciality_course.insert("speciality_course"))
        return services_speciality_course()

    elif services == '3':
        column_name = input("enter column name: ")
        column_data = input("enter column value: ")
        print(SpecialityCourse.delete("speciality_course", column_name, column_data))
        return services_speciality_course()

    elif services == '4':
        column_name = input("enter the name of the column in which one do you want to change: ")
        new_data_for_column = input(f"enter the data you want to change in {column_name} column: ")
        where_column = input(f"enter the column where you want to change exactly: ")
        where_row = input(f"enter the row where you want to change exactly: ")
        print(SpecialityCourse.update("speciality_course", column_name, new_data_for_column, where_column, where_row))
        return services_speciality_course()

    elif services == '0':
        return main()

    else:
        print(">>>>>>WRONG BUTTON<<<<<")
        print(">>>>>>CHOOSE AGAIN<<<<<")
        return services_speciality_course()


def services_basket():
    services = input("""
1.SELECT        #####    #    #     ####     ####     ####    ######
2.INSERT      #          #    #    #    #   #    #    #       #
3.DELETE      #          ######    #    #   #    #    ####    ######
4.UPDATE      #          #    #    #    #   #    #       #    # 
0.BACK          #####    #    #     ####     ####     ####    ######

                            """)
    if services == '1':
        for i in Basket.select("basket"):
            print(i)
        return services_basket()

    elif services == '2':
        student_id = int(input("enter student`s id: "))
        course_id = int(input("enter course`s id: "))
        basket = Basket(student_id, course_id)
        print(basket.insert("basket"))
        return services_basket()

    elif services == '3':
        column_name = input("enter column name: ")
        column_data = input("enter column value: ")
        print(Basket.delete("basket", column_name, column_data))
        return services_basket()

    elif services == '4':
        column_name = input("enter the name of the column in which one do you want to change: ")
        new_data_for_column = input(f"enter the data you want to change in {column_name} column: ")
        where_column = input(f"enter the column where you want to change exactly: ")
        where_row = input(f"enter the row where you want to change exactly: ")
        print(Basket.update("basket", column_name, new_data_for_column, where_column, where_row))
        return services_basket()

    elif services == '0':
        return main()

    else:
        print(">>>>>>WRONG BUTTON<<<<<")
        print(">>>>>>CHOOSE AGAIN<<<<<")
        return services_basket()


def services_student():
    services = input("""
1.SELECT        #####    #    #     ####     ####     ####    ######
2.INSERT      #          #    #    #    #   #    #    #       #
3.DELETE      #          ######    #    #   #    #    ####    ######
4.UPDATE      #          #    #    #    #   #    #       #    # 
0.BACK          #####    #    #     ####     ####     ####    ######

                """)

    if services == '1':
        for i in Student.select("student"):
            print(i)
        return services_student()

    elif services == '2':
        first_name = input("enter first name : ")
        last_name = input("enter last name : ")
        email = input("enter email: ")
        balance = float(input("how much money do u want to transfer: "))
        payment_id = int(input("enter payment id : "))
        birth_date = input("enter birth date: ")
        password = input("enter password: ")
        city_id = int(input("enter id the city: "))
        student = Student(first_name, last_name, email, balance, payment_id, birth_date, password, city_id)
        print(student.insert("student"))
        return services_student()

    elif services == '3':
        column_name = input("enter column name: ")
        column_data = input("enter column value: ")
        print(Student.delete("student", column_name, column_data))
        return services_student()

    elif services == '4':
        column_name = input("enter the name of the column in which one do you want to change: ")
        new_data_for_column = input(f"enter the data you want to change in {column_name} column: ")
        where_column = input(f"enter the column where you want to change exactly: ")
        where_row = input(f"enter the row where you want to change exactly: ")
        print(Student.update("student", column_name, new_data_for_column, where_column, where_row))
        return services_student()

    elif services == '0':
        return main()

    else:
        print(">>>>>>WRONG BUTTON<<<<<")
        print(">>>>>>CHOOSE AGAIN<<<<<")
        return services_student()


def main():
    print(">>>>>>>WHICH TABLE DO U WANT TO CHOOSE<<<<<<")
    tables = input("""
1.Country Table
2.City Table
3.Payment Table
4.Mentor Table
5.Lesson Table
6.Modul Table                    #####    #     #     #####      #####     ######    ######
7.Speciality Table              #         #     #    #     #    #     #    #         #
8.Course Table                  #         #######    #     #    #     #    ######    ######
9.Mentor Course Table           #         #     #    #     #    #     #         #    # 
10.Speciality Course Table       #####    #     #     #####      #####     ######    ######    
11.Basket Table
12.Student Table


    """)
    if tables == "1":
        return services_country()

    elif tables == "2":
        return services_city()

    elif tables == "3":
        return services_payment()

    elif tables == "4":
        return services_mentor()

    elif tables == "5":
        return services_lesson()

    elif tables == "6":
        return services_modul()

    elif tables == "7":
        return services_speciality()

    elif tables == "8":
        return services_course()

    elif tables == "9":
        return services_mentor_course()

    elif tables == "10":
        return services_speciality_course()

    elif tables == "11":
        return services_basket()

    elif tables == "12":
        return services_student()

    else:
        print(">>>>>>WRONG BUTTON<<<<<<")
        print(">>>>>>CHOOSE AGAIN<<<<<<")
        return main()