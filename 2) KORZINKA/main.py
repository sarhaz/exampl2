from classes import Region, City, Payment, Store, Category, Product,  Korzinka, Customer, StoreProduct, Address
def services_category():
    services = input("""
1.SELECT        #####    #    #     ####     ####     ####    ######
2.INSERT      #          #    #    #    #   #    #    #       #
3.DELETE      #          ######    #    #   #    #    ####    ######
4.UPDATE      #          #    #    #    #   #    #       #    # 
0.BACK          #####    #    #     ####     ####     ####    ######

    """)
    if services == '1':
        for i in Category.select("category"):
            print(i)
        return services_category()

    elif services == '2':
        country = input("enter category name: ")
        category = Category(country)
        print(category.insert("category"))
        return services_category()

    elif services == '3':
        column_name = input("enter column name: ")
        column_data = input("enter column value: ")
        print(Category.delete("category", column_name, column_data))
        return services_category()

    elif services == '4':
        column_name = input("enter the name of the column in which one do you want to change: ")
        new_data_for_column = input(f"enter the data you want to change in {column_name} column: ")
        where_column = input(f"enter the column where you want to change exactly: ")
        where_row = input(f"enter the row where you want to change exactly: ")
        print(Category.update("category", column_name, new_data_for_column, where_column, where_row))
        return services_category()

    elif services == '0':
        return main()

    else:
        print(">>>>>>WRONG BUTTON<<<<<")
        print(">>>>>>CHOOSE AGAIN<<<<<")
        return services_category()

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
        category_id = int(input("enter id of the product`s category: "))
        description = input("write a description about the speciality: ")
        number_products = int(input("enter a number of products: "))
        product_status = input("enter a status of the product if it ``has`` or ``has not`` : ")
        product = Product(name, category_id, description, number_products,  product_status)
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
        payment_status = input("enter a status of the product if it ``has`` or ``has not``: ")
        payment = Payment(amount, payment_type, payment_status)
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


def services_region():
    services = input("""
1.SELECT        #####    #    #     ####     ####     ####    ######
2.INSERT      #          #    #    #    #   #    #    #       #
3.DELETE      #          ######    #    #   #    #    ####    ######
4.UPDATE      #          #    #    #    #   #    #       #    # 
0.BACK          #####    #    #     ####     ####     ####    ######

                    """)
    if services == '1':
        for i in Region.select("region"):
            print(i)
        return services_region()

    elif services == '2':
        name = input("write a name of the region the city belongs to: ")
        region = Region(name)
        print(region.insert("region"))
        return services_region()

    elif services == '3':
        column_name = input("enter column name: ")
        column_data = input("enter column value: ")
        print(Region.delete("region", column_name, column_data))
        return services_region()

    elif services == '4':
        column_name = input("enter the name of the column in which one do you want to change: ")
        new_data_for_column = input(f"enter the data you want to change in {column_name} column: ")
        where_column = input(f"enter the column where you want to change exactly: ")
        where_row = input(f"enter the row where you want to change exactly: ")
        print(Region.update("region", column_name, new_data_for_column, where_column, where_row))
        return services_region()


    elif services == '0':
        return main()

    else:
        print(">>>>>>WRONG BUTTON<<<<<")
        print(">>>>>>CHOOSE AGAIN<<<<<")
        return services_region()


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
        region_id = int(input("enter id of region which this city belongs to: "))
        city = City(city_name, region_id)
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



def services_store():
    services = input("""
1.SELECT        #####    #    #     ####     ####     ####    ######
2.INSERT      #          #    #    #    #   #    #    #       #
3.DELETE      #          ######    #    #   #    #    ####    ######
4.UPDATE      #          #    #    #    #   #    #       #    # 
0.BACK          #####    #    #     ####     ####     ####    ######

                            """)
    if services == '1':
        for i in Store.select("store"):
            print(i)
        return services_store()

    elif services == '2':
        location = input("enter shop`s location: ")
        city_id = int(input("enter id of the city: "))
        number_stores = int(input("enter number of the stores which are exists in the city: "))
        store = Store(location, city_id, number_stores)
        print(store.insert("store"))
        return services_store()

    elif services == '3':
        column_name = input("enter column name: ")
        column_data = input("enter column value: ")
        print(Store.delete("store", column_name, column_data))
        return services_store()

    elif services == '4':
        column_name = input("enter the name of the column in which one do you want to change: ")
        new_data_for_column = input(f"enter the data you want to change in {column_name} column: ")
        where_column = input(f"enter the column where you want to change exactly: ")
        where_row = input(f"enter the row where you want to change exactly: ")
        print(Store.update("store", column_name, new_data_for_column, where_column, where_row))
        return services_store()

    elif services == '0':
        return main()

    else:
        print(">>>>>>WRONG BUTTON<<<<<")
        print(">>>>>>CHOOSE AGAIN<<<<<")
        return services_store()


def services_customer():
    services = input("""
1.SELECT        #####    #    #     ####     ####     ####    ######
2.INSERT      #          #    #    #    #   #    #    #       #
3.DELETE      #          ######    #    #   #    #    ####    ######
4.UPDATE      #          #    #    #    #   #    #       #    # 
0.BACK          #####    #    #     ####     ####     ####    ######

         """)
    if services == '1':
        for i in Customer.select("customer"):
            print(i)
        return services_customer()

    elif services == '2':
        first_name = input("enter first name: ")
        last_name = input("enter last name: ")
        email = input("enter email: ")
        balance = float(input("enter balance: "))
        birth_date = input("enter birth date: ")
        payment_id = int(input("enter payment id: "))
        password = input("enter password: ")
        city_id = int(input("enter city_id: "))
        customer = Customer(first_name, last_name, email, balance, birth_date, payment_id, password, city_id)
        print(customer.insert("customer"))
        return services_customer()

    elif services == '3':
        column_name = input("enter column name: ")
        column_data = input("enter column value: ")
        print(Customer.delete("customer", column_name, column_data))
        return services_customer()

    elif services == '4':
        column_name = input("enter the name of the column in which one do you want to change: ")
        new_data_for_column = input(f"enter the data you want to change in {column_name} column: ")
        where_column = input(f"enter the column where you want to change exactly: ")
        where_row = input(f"enter the row where you want to change exactly: ")
        print(Customer.update("customer", column_name, new_data_for_column, where_column, where_row))
        return services_customer()

    elif services == '0':
        return main()

    else:
        print(">>>>>>WRONG BUTTON<<<<<")
        print(">>>>>>CHOOSE AGAIN<<<<<")
        return services_customer()


def services_korzinka():
    services = input("""
1.SELECT        #####    #    #     ####     ####     ####    ######
2.INSERT      #          #    #    #    #   #    #    #       #
3.DELETE      #          ######    #    #   #    #    ####    ######
4.UPDATE      #          #    #    #    #   #    #       #    # 
0.BACK          #####    #    #     ####     ####     ####    ######

                    """)
    if services == '1':
        for i in Korzinka.select("korzinka"):
            print(i)
        return services_korzinka()

    elif services == '2':
        customer_id = int(input("enter id of the customer: "))
        product_id = int(input("enter enter id of the product: "))
        korzinka = Korzinka(customer_id, product_id)
        print(korzinka.insert("korzinka"))
        return services_korzinka()

    elif services == '3':
        column_name = input("enter column name: ")
        column_data = input("enter column value: ")
        print(Korzinka.delete("korzinka", column_name, column_data))
        return services_korzinka()

    elif services == '4':
        column_name = input("enter the name of the column in which one do you want to change: ")
        new_data_for_column = input(f"enter the data you want to change in {column_name} column: ")
        where_column = input(f"enter the column where you want to change exactly: ")
        where_row = input(f"enter the row where you want to change exactly: ")
        print(Korzinka.update("korzinka", column_name, new_data_for_column, where_column, where_row))
        return services_korzinka()

    elif services == '0':
        return main()

    else:
        print(">>>>>>WRONG BUTTON<<<<<")
        print(">>>>>>CHOOSE AGAIN<<<<<")
        return services_korzinka()


def services_store_product():
    services = input("""
1.SELECT        #####    #    #     ####     ####     ####    ######
2.INSERT      #          #    #    #    #   #    #    #       #
3.DELETE      #          ######    #    #   #    #    ####    ######
4.UPDATE      #          #    #    #    #   #    #       #    # 
0.BACK          #####    #    #     ####     ####     ####    ######

                            """)
    if services == '1':
        for i in StoreProduct.select("store_product"):
            print(i)
        return services_store_product()

    elif services == '2':
        store_id = int(input("enter store`s id to find out which product has in this shop: "))
        product_id = int(input("enter product`s id: "))
        product_status = input("enter product`s status  does it ``has`` or ``has not``: ")
        store_product = StoreProduct(store_id, product_id, product_status)
        print(store_product.insert("store_product"))
        return services_store_product()

    elif services == '3':
        column_name = input("enter column name: ")
        column_data = input("enter column value: ")
        print(StoreProduct.delete("store_product", column_name, column_data))
        return services_store_product()

    elif services == '4':
        column_name = input("enter the name of the column in which one do you want to change: ")
        new_data_for_column = input(f"enter the data you want to change in {column_name} column: ")
        where_column = input(f"enter the column where you want to change exactly: ")
        where_row = input(f"enter the row where you want to change exactly: ")
        print(StoreProduct.update("store_product", column_name, new_data_for_column, where_column, where_row))
        return services_store_product()

    elif services == '0':
        return main()

    else:
        print(">>>>>>WRONG BUTTON<<<<<")
        print(">>>>>>CHOOSE AGAIN<<<<<")
        return services_store_product()


def services_address():
    services = input("""
1.SELECT        #####    #    #     ####     ####     ####    ######
2.INSERT      #          #    #    #    #   #    #    #       #
3.DELETE      #          ######    #    #   #    #    ####    ######
4.UPDATE      #          #    #    #    #   #    #       #    # 
0.BACK          #####    #    #     ####     ####     ####    ######

                    """)

    if services == '1':
        for i in Address.select("address"):
            print(i)
        return services_address()

    elif services == '2':
        name_district = input("enter name of the district : ")
        city_id = int(input("enter city id: "))
        address = Address(name_district, city_id)
        print(address.insert("address"))
        return services_address()

    elif services == '3':
        column_name = input("enter column name: ")
        column_data = input("enter column value: ")
        print(Address.delete("address", column_name, column_data))
        return services_address()

    elif services == '4':
        column_name = input("enter the name of the column in which one do you want to change: ")
        new_data_for_column = input(f"enter the data you want to change in {column_name} column: ")
        where_column = input(f"enter the column where you want to change exactly: ")
        where_row = input(f"enter the row where you want to change exactly: ")
        print(Address.update("address", column_name, new_data_for_column, where_column, where_row))
        return services_address()

    elif services == '0':
        return main()

    else:
        print(">>>>>>WRONG BUTTON<<<<<")
        print(">>>>>>CHOOSE AGAIN<<<<<")
        return services_address()


def main():
    print(">>>>>>>WHICH TABLE DO U WANT TO CHOOSE<<<<<<")
    tables = input("""
1.category Table               TTTTTTTT      A         BBBBB       L         EEEEEEE      SSSSS
2.product Table                   TT        A A        B    B      L         E           S     
3.Payment Table                   TT       A   A       BBBBB       L         EEEEEEE      SSSSS
4.region Table                    TT      AAAAAAA      B    B      L         E                 S
5.city Table                      TT     A       A     BBBBB       LLLLLL    EEEEEEE      SSSSS
6.store Table                  
7.customer Table             
8.korzinka Table             
9.store product Table        
10.address Table                


    """)
    if tables == "1":
        return services_category()

    elif tables == "2":
        return services_product()

    elif tables == "3":
        return services_payment()

    elif tables == "4":
        return services_region()

    elif tables == "5":
        return services_city()

    elif tables == "6":
        return services_store()

    elif tables == "7":
        return services_customer()

    elif tables == "8":
        return services_korzinka()

    elif tables == "9":
        return services_store_product()

    elif tables == "10":
        return services_address()

    else:
        print(">>>>>>WRONG BUTTON<<<<<<")
        print(">>>>>>CHOOSE AGAIN<<<<<<")
        return main()


if __name__ == "__main__":
    main()