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

class Category(Base):
    def __init__(self, name: str):
        self.name = name

    def insert(self, table):
        query = f"""INSERT INTO {table}(name) VALUES ('{self.name}');"""
        return Database.connect(query, "insert")

class Product(Base):
    def __init__(self, name: str, category_id: int, description: str, number_products: int,  product_status: str):
        self.name = name
        self.category_id = category_id
        self.description = description
        self.number_products = number_products
        self.product_status = product_status

    def insert(self, table):
        query = f"""INSERT INTO {table}(name,category_id,description,number_products,product_status) VALUES ('{self.name}', {self.category_id}, '{self.description}',{self.number_products},'{self.product_status}')"""
        return Database.connect(query, "insert")


class Payment(Base):
    def __init__(self, amount: float, payment_type: str, payment_status: str):
        self.amount = amount
        self.payment_type = payment_type
        self.payment_status = payment_status

    def insert(self, table):
        query = f"""INSERT INTO {table}(amount,payment_type,payment_status) VALUES ({self.amount}, '{self.payment_type}', '{self.payment_status}')"""
        return Database.connect(query, "insert")


class Region(Base):
    def __init__(self, name: str):
        self.name = name

    def insert(self, table):
        query = f"""INSERT INTO {table}(name) VALUES ('{self.name}')"""
        return Database.connect(query, "insert")


class City(Base):
    def __init__(self, name: str, region_id: int):
        self.name = name
        self.region_id = region_id

    def insert(self, table):
        query = f"""INSERT INTO {table}(name,region_id) VALUES ('{self.name}',{self.region_id})"""
        return Database.connect(query, "insert")

class Store(Base):
    def __init__(self, location: str, city_id: int, number_stores: int):
        self.location = location
        self.city_id = city_id
        self.number_stores = number_stores

    def insert(self, table):
        query = f"""INSERT INTO {table}(location,city_id,number_stores) VALUES ('{self.name}', {self.city_id},{self.number_stores})"""
        return Database.connect(query, "insert")

class Customer(Base):
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

class Korzinka(Base):
    def __init__(self, customer_id: int, product_id: int):
        self.customer_id = customer_id
        self.product_id = product_id

    def insert(self, table):
        query = f"""INSERT INTO {table}(customer_id,product_id) VALUES ({self.client_id}, {self.product_id})"""
        return Database.connect(query, "insert")



class StoreProduct(Base):
    def __init__(self, store_id: int, product_id: int, product_status: str):
        self.store_id = store_id
        self.product_id = product_id
        self.product_status = product_status

    def insert(self, table):
        query = f"""INSERT INTO {table}(store_id,product_id,product_status) VALUES ({self.shop_id}, {self.product_id},'{self.product_status}')"""
        return Database.connect(query, "insert")


class Address(Base):
    def __init__(self, name_district: str, city_id: int):
        self.name_district = name_district
        self.city_id = city_id

    def insert(self, table):
        query = f"""INSERT INTO {table}(comment,client_id,product_id) VALUES ('{self.comment}', {self.client_id}, {self.product_id});"""
        return Database.connect(query, "insert")


# if __name__ == "__main__":
