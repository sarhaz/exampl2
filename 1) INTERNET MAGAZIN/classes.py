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
    def __init__(self, name: str):
        self.name = name

    def insert(self, table):
        query = f"""INSERT INTO {table}(name) VALUES ('{self.name}')"""
        return Database.connect(query, "insert")


class City(Country):
    def __init__(self, name: str, country_id: int):
        super().__init__(name)
        self.country_id = country_id

    def insert(self, table):
        query = f"""INSERT INTO {table}(name,country_id) VALUES ('{self.name}',{self.country_id})"""
        return Database.connect(query, "insert")


class Payment(Base):
    def __init__(self, amount: float, payment_type: str):
        self.amount = amount
        self.payment_type = payment_type

    def insert(self, table):
        query = f"""INSERT INTO {table}(amount,payment_type) VALUES ({self.amount}, '{self.payment_type}')"""
        return Database.connect(query, "insert")


class Shop(Base):
    def __init__(self, name: str, city_id: int):
        self.name = name
        self.city_id = city_id

    def insert(self, table):
        query = f"""INSERT INTO {table}(name,city_id) VALUES ('{self.name}', {self.city_id})"""
        return Database.connect(query, "insert")


class ProductCategory(Base):
    def __init__(self, name: str):
        self.name = name

    def insert(self, table):
        query = f"""INSERT INTO {table}(name) VALUES ('{self.name}');"""
        return Database.connect(query, "insert")


class Client(Base):
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

class Product(Base):
    def __init__(self, name: str, product_category_id: int, description: str, number_products: int, rating: float, product_status: str):
        self.name = name
        self.product_category_id = product_category_id
        self.description = description
        self.number_products = number_products
        self.rating = rating
        self.product_status = product_status

    def insert(self, table):
        query = f"""INSERT INTO {table}(name,product_category_id,description,number_products,rating,product_status) VALUES ('{self.name}', {self.product_category_id}, '{self.description}',{self.number_products},{self.rating},'{self.product_status}')"""
        return Database.connect(query, "insert")

class Basket(Base):
    def __init__(self, client_id: int, product_id: int):
        self.client_id = client_id
        self.product_id = product_id

    def insert(self, table):
        query = f"""INSERT INTO {table}(client_id,product_id) VALUES ({self.client_id}, {self.product_id})"""
        return Database.connect(query, "insert")



class ShopProduct(Base):
    def __init__(self, shop_id: int, product_id: int):
        self.shop_id = shop_id
        self.product_id = product_id

    def insert(self, table):
        query = f"""INSERT INTO {table}(shop_id,product_id) VALUES ({self.shop_id}, {self.product_id})"""
        return Database.connect(query, "insert")


class CommentProduct(Base):
    def __init__(self, comment: str, client_id: int, product_id: int):
        self.comment = comment
        self.client_id = client_id
        self.product_id = product_id

    def insert(self, table):
        query = f"""INSERT INTO {table}(comment,client_id,product_id) VALUES ('{self.comment}', {self.client_id}, {self.product_id});"""
        return Database.connect(query, "insert")


# if __name__ == "__main__":
