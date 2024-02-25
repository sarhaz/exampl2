import psycopg2 as psql
import os
from dotenv import load_dotenv
load_dotenv()

class Database:
    @staticmethod
    def connect(query, types):
        project = psql.connect(
            database=os.getenv("DB_NAME"),
            password=os.getenv("DB_PASSWORD"),
            user=os.getenv("DB_USER"),
            host=os.getenv("DB_HOST")
        )
        cursor = project.cursor()
        cursor.execute(query, types)
        query_types = ["insert", "delete", "update", "create"]
        if types in query_types:
            project.commit()
            if types == "insert":
                return "INSERTED SUCCESFULLY"

            elif types == "delete":
                return "DELETED SUCCESFULLY"

            elif types == "update":
                return "UPDATED SUCCESFULLY"

            elif types == "create":
                return "CREATED SUCCESFULLY"

        else:
            return cursor.fetchall()


# if __name__ == "__main__":
