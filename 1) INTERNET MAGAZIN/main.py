from classes import Country, City, Payment, Shop, ProductCategory, Product,  Basket, Client, ShopProduct, CommentProduct
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
        country = Country(country)
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
        for i in City.select("city"):
            print(i)
        return services_city()

    elif services == '2':
        city_name = input("enter city name: ")
        country_id = int(input("enter id of country which this city belongs to: "))
        city = City(city_name, country_id)
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
        payment_type = input("write type of payment like click ,payme , ipoteka, uzum or others: ")
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


def services_shop():
    services = input("""
1.SELECT        #####    #    #     ####     ####     ####    ######
2.INSERT      #          #    #    #    #   #    #    #       #
3.DELETE      #          ######    #    #   #    #    ####    ######
4.UPDATE      #          #    #    #    #   #    #       #    # 
0.BACK          #####    #    #     ####     ####     ####    ######

                            """)
    if services == '1':
        for i in Shop.select("shop"):
            print(i)
        return services_shop()

    elif services == '2':
        name = input("enter shop`s name: ")
        city_id = int(input("enter id of the city: "))
        shop = Shop(name, city_id)
        print(shop.insert("shop"))
        return services_shop()

    elif services == '3':
        column_name = input("enter column name: ")
        column_data = input("enter column value: ")
        print(Shop.delete("shop", column_name, column_data))
        return services_shop()

    elif services == '4':
        column_name = input("enter the name of the column in which one do you want to change: ")
        new_data_for_column = input(f"enter the data you want to change in {column_name} column: ")
        where_column = input(f"enter the column where you want to change exactly: ")
        where_row = input(f"enter the row where you want to change exactly: ")
        print(Shop.update("shop", column_name, new_data_for_column, where_column, where_row))
        return services_shop()

    elif services == '0':
        return main()

    else:
        print(">>>>>>WRONG BUTTON<<<<<")
        print(">>>>>>CHOOSE AGAIN<<<<<")
        return services_shop()


def services_product_category():
    services = input("""
1.SELECT        #####    #    #     ####     ####     ####    ######
2.INSERT      #          #    #    #    #   #    #    #       #
3.DELETE      #          ######    #    #   #    #    ####    ######
4.UPDATE      #          #    #    #    #   #    #       #    # 
0.BACK          #####    #    #     ####     ####     ####    ######

         """)
    if services == '1':
        for i in ProductCategory.select("product_category"):
            print(i)
        return services_product_category()

    elif services == '2':
        name = input("write category of the product: ")
        product_category = ProductCategory(name)
        print(product_category.insert("product_category"))
        return services_product_category()

    elif services == '3':
        column_name = input("enter column name: ")
        column_data = input("enter column value: ")
        print(ProductCategory.delete("product_category", column_name, column_data))
        return services_product_category()

    elif services == '4':
        column_name = input("enter the name of the column in which one do you want to change: ")
        new_data_for_column = input(f"enter the data you want to change in {column_name} column: ")
        where_column = input(f"enter the column where you want to change exactly: ")
        where_row = input(f"enter the row where you want to change exactly: ")
        print(ProductCategory.update("product_category", column_name, new_data_for_column, where_column, where_row))
        return services_product_category()

    elif services == '0':
        return main()

    else:
        print(">>>>>>WRONG BUTTON<<<<<")
        print(">>>>>>CHOOSE AGAIN<<<<<")
        return services_product_category()


def services_client():
    services = input("""
1.SELECT        #####    #    #     ####     ####     ####    ######
2.INSERT      #          #    #    #    #   #    #    #       #
3.DELETE      #          ######    #    #   #    #    ####    ######
4.UPDATE      #          #    #    #    #   #    #       #    # 
0.BACK          #####    #    #     ####     ####     ####    ######

                    """)

    if services == '1':
        for i in Client.select("client"):
            print(i)
        return services_client()

    elif services == '2':
        first_name = input("enter first name: ")
        last_name = input("enter last name: ")
        email = input("enter an email: ")
        balance = float(input(f"enter balance: "))
        birth_date = input("enter birth date: ")
        payment_id = int(input("enter payment id: "))
        password = input("enter password: ")
        city_id = int(input("enter city id: "))
        client = Client(first_name, last_name, email, balance, birth_date, payment_id, password, city_id)
        print(client.insert("client"))
        return services_client()

    elif services == '3':
        column_name = input("enter column name: ")
        column_data = input("enter column value: ")
        print(Client.delete("client", column_name, column_data))
        return services_client()

    elif services == '4':
        column_name = input("enter the name of the column in which one do you want to change: ")
        new_data_for_column = input(f"enter the data you want to change in {column_name} column: ")
        where_column = input(f"enter the column where you want to change exactly: ")
        where_row = input(f"enter the row where you want to change exactly: ")
        print(Client.update("client", column_name, new_data_for_column, where_column, where_row))
        return services_client()

    elif services == '0':
        return main()

    else:
        print(">>>>>>WRONG BUTTON<<<<<")
        print(">>>>>>CHOOSE AGAIN<<<<<")
        return services_client()


def services_product():
    services = input("""
1.SELECT        #####    #    #     ####     ####     ####    ######
2.INSERT      #          #    #    #    #   #    #    #       #
3.DELETE      #          ######    #    #   #    #    ####    ######
4.UPDATE      #          #    #    #    #   #    #       #    # 
0.BACK          #####    #    #     ####     ####     ####    ######

                """)
    if services == '1':
        for i in Product.select("product"):
            print(i)
        return services_product()

    elif services == '2':
        name = input("name of the speciality: ")
        product_category_id = int(input("enter id of the product category: "))
        description = input("write a description about the speciality: ")
        number_products = int(input("enter a number of products: "))
        rating = float(input("enter a number for rating: "))
        product_status = input("enter a status of the product if it ``has`` or ``has not`` : ")
        product = Product(name, product_category_id, description, number_products, rating, product_status)
        print(product.insert("product"))
        return services_product()

    elif services == '3':
        column_name = input("enter column name: ")
        column_data = input("enter column value: ")
        print(Product.delete("product", column_name, column_data))
        return services_product()

    elif services == '4':
        column_name = input("enter the name of the column in which one do you want to change: ")
        new_data_for_column = input(f"enter the data you want to change in {column_name} column: ")
        where_column = input(f"enter the column where you want to change exactly: ")
        where_row = input(f"enter the row where you want to change exactly: ")
        print(Product.update("product", column_name, new_data_for_column, where_column, where_row))
        return services_product()

    elif services == '0':
        return main()

    else:
        print(">>>>>>WRONG BUTTON<<<<<")
        print(">>>>>>CHOOSE AGAIN<<<<<")
        return services_product()


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
        client_id = int(input("enter id of the client: "))
        product_id = int(input("enter enter id of the product: "))
        basket = Basket(client_id, product_id)
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


def services_shop_product():
    services = input("""
1.SELECT        #####    #    #     ####     ####     ####    ######
2.INSERT      #          #    #    #    #   #    #    #       #
3.DELETE      #          ######    #    #   #    #    ####    ######
4.UPDATE      #          #    #    #    #   #    #       #    # 
0.BACK          #####    #    #     ####     ####     ####    ######

                            """)
    if services == '1':
        for i in ShopProduct.select("shop_product"):
            print(i)
        return services_shop_product()

    elif services == '2':
        shop_id = int(input("enter shop`s id to find out which product has in this shop: "))
        product_id = int(input("enter product`s id: "))
        shop_product = ShopProduct(shop_id, product_id)
        print(shop_product.insert("shop_product"))
        return services_shop_product()

    elif services == '3':
        column_name = input("enter column name: ")
        column_data = input("enter column value: ")
        print(ShopProduct.delete("shop_product", column_name, column_data))
        return services_shop_product()

    elif services == '4':
        column_name = input("enter the name of the column in which one do you want to change: ")
        new_data_for_column = input(f"enter the data you want to change in {column_name} column: ")
        where_column = input(f"enter the column where you want to change exactly: ")
        where_row = input(f"enter the row where you want to change exactly: ")
        print(ShopProduct.update("shop_product", column_name, new_data_for_column, where_column, where_row))
        return services_shop_product()

    elif services == '0':
        return main()

    else:
        print(">>>>>>WRONG BUTTON<<<<<")
        print(">>>>>>CHOOSE AGAIN<<<<<")
        return services_shop_product()


def services_comment_product():
    services = input("""
1.SELECT        #####    #    #     ####     ####     ####    ######
2.INSERT      #          #    #    #    #   #    #    #       #
3.DELETE      #          ######    #    #   #    #    ####    ######
4.UPDATE      #          #    #    #    #   #    #       #    # 
0.BACK          #####    #    #     ####     ####     ####    ######

                            """)
    if services == '1':
        for i in CommentProduct.select("comment_product"):
            print(i)
        return services_comment_product()

    elif services == '2':
        comment = input("write a comment for the product")
        client_id = int(input("enter client`s id: "))
        product_id = int(input("enter product`s id: "))
        comment_product = CommentProduct(comment, client_id, product_id)
        print(comment_product.insert("comment_product"))
        return services_comment_product()

    elif services == '3':
        column_name = input("enter column name: ")
        column_data = input("enter column value: ")
        print(CommentProduct.delete("comment_product", column_name, column_data))
        return services_comment_product()

    elif services == '4':
        column_name = input("enter the name of the column in which one do you want to change: ")
        new_data_for_column = input(f"enter the data you want to change in {column_name} column: ")
        where_column = input(f"enter the column where you want to change exactly: ")
        where_row = input(f"enter the row where you want to change exactly: ")
        print(CommentProduct.update("comment_product", column_name, new_data_for_column, where_column, where_row))
        return services_comment_product()

    elif services == '0':
        return main()

    else:
        print(">>>>>>WRONG BUTTON<<<<<")
        print(">>>>>>CHOOSE AGAIN<<<<<")
        return services_comment_product()


def main():
    print(">>>>>>>WHICH TABLE DO U WANT TO CHOOSE<<<<<<")
    tables = input("""
1.Country Table
2.City Table
3.Payment Table
4.shop Table
5.product category Table
6.client Table                    #####    #     #     #####      #####     ######    ######
7.product Table                  #         #     #    #     #    #     #    #         #
8.basket Table                   #         #######    #     #    #     #    ######    ######
9.shop product Table             #         #     #    #     #    #     #         #    # 
10.comment product Table          #####    #     #     #####      #####     ######    ######    


    """)
    if tables == "1":
        return services_country()

    elif tables == "2":
        return services_city()

    elif tables == "3":
        return services_payment()

    elif tables == "4":
        return services_shop()

    elif tables == "5":
        return services_product_category()

    elif tables == "6":
        return services_client()

    elif tables == "7":
        return services_product()

    elif tables == "8":
        return services_basket()

    elif tables == "9":
        return services_shop_product()

    elif tables == "10":
        return services_comment_product()

    else:
        print(">>>>>>WRONG BUTTON<<<<<<")
        print(">>>>>>CHOOSE AGAIN<<<<<<")
        return main()


if __name__ == "__main__":
    main()