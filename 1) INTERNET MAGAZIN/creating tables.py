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

    shop = f"""CREATE TABLE shop(
            id SERIAL PRIMARY KEY,
            name TEXT,
            city_id INT REFERENCES city(id),
            last_updated TIMESTAMP DEFAULT now());
            """

    product_category = f"""CREATE TABLE product_category(
            id SERIAL PRIMARY KEY,
            name text,
            last_updated TIMESTAMP DEFAULT now());
            """


    client = f"""CREATE TABLE client(
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

    product = f"""CREATE TABLE product(
            id SERIAL PRIMARY KEY,
            name TEXT,
            product_category_id INT REFERENCES product_category(id),
            description TEXT,
            number_products int,
            rating float,
            product_status text,
            last_updated TIMESTAMP DEFAULT now());
            """



    basket = f"""CREATE TABLE basket(
                    id SERIAL PRIMARY KEY,
                    client_id INT REFERENCES client(id),
                    product_id INT REFERENCES product(id),
                    last_updated TIMESTAMP DEFAULT now());"""


    shop_product = f"""CREATE TABLE shop_product(
                id SERIAL PRIMARY KEY,
                shop_id INT REFERENCES shop(id),
                product_id INT REFERENCES product(id),
                last_updated TIMESTAMP DEFAULT now());
                """

    comment_product = f"""CREATE TABLE comment_product(
                id SERIAL PRIMARY KEY,
                comment text,
                client_id INT REFERENCES client(id),
                product_id INT REFERENCES product(id),
                last_updated TIMESTAMP DEFAULT now());
                """

    data_tables = {
        "country": country,
        "city": city,
        "payment": payment,
        "shop": shop,
        "product_category": product_category,
        "client": client,
        "product": product,
        "basket": basket,
        "shop_product": shop_product,
        "comment_product": comment_product,
    }

    for i in data_tables:
        print(f"{i} {Database.connect(data_tables[i], "create")}")


if __name__ == "__main__":
    creating_tables()
