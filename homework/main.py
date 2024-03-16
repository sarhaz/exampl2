import psycopg2 as db


class Database:
    @staticmethod
    def connect(query, query_type):
        database = db.connect(
            host="localhost",
            database="n37",
            password="1914",
            user="postgres"
        )
        cursor = database.cursor()
        cursor.execute(query)
        if query_type == "insert":
            database.commit()
            return "inserted"

        if query_type == "select":
            return cursor.fetchall()
