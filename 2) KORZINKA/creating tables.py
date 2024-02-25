from base import Database


def creating_tables():
    category = f"""CREATE TABLE category(
        id SERIAL PRIMARY KEY,
        name text,
        last_updated TIMESTAMP DEFAULT now());
        """


    product = f"""CREATE TABLE product(
            id SERIAL PRIMARY KEY,
            name TEXT,
            category_id INT REFERENCES category(id),
            description TEXT,
            number_products int,
            product_status text,
            last_updated TIMESTAMP DEFAULT now());
            """

    payment = f"""CREATE TABLE payment(
    id SERIAL PRIMARY KEY,
    amount FLOAT,
    payment_type VARCHAR(20),
    payment_status VARCHAR(20),
    last_updated TIMESTAMP DEFAULT now());
    """

    region = f"""CREATE TABLE region(
        id SERIAL PRIMARY KEY,
        name TEXT,
        last_updated TIMESTAMP DEFAULT now());
    """

    city = f"""CREATE TABLE city(
        id SERIAL PRIMARY KEY,
        name TEXT,
        region_id INT REFERENCES region(id),
        last_updated TIMESTAMP DEFAULT now());
        """

    store = f"""CREATE TABLE store(
            id SERIAL PRIMARY KEY,
            location TEXT,
            city_id INT REFERENCES city(id),
            number_stores int,
            last_updated TIMESTAMP DEFAULT now());
            """

    customer = f"""CREATE TABLE customer(
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

    korzinka = f"""CREATE TABLE korzinka(
                    id SERIAL PRIMARY KEY,
                    customer_id INT REFERENCES customer(id),
                    product_id INT REFERENCES product(id),
                    last_updated TIMESTAMP DEFAULT now());"""

    store_product = f"""CREATE TABLE store_product(
                id SERIAL PRIMARY KEY,
                store_id INT REFERENCES store(id),
                product_id INT REFERENCES product(id),
                product_status text,
                last_updated TIMESTAMP DEFAULT now());
                """

    address = f"""CREATE TABLE address(
                    id SERIAL PRIMARY KEY,
                    name_district text,
                    city_id INT REFERENCES city(id),
                    last_updated TIMESTAMP DEFAULT now());
                    """

    data_tables = {
        "category": category,
        "product": product,
        "payment": payment,
        "region": region,
        "city": city,
        "store": store,
        "customer": customer,
        "korzinka": korzinka,
        "store_product": store_product,
        "address": address,
    }

    for i in data_tables:
        print(f"{i} {Database.connect(data_tables[i], "create")}")


if __name__ == "__main__":
    creating_tables()
