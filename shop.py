from db import DatabaseManager

db = DatabaseManager("shop_dp.db")


while True:
    print("---")
    answer = input("Виберіть дію.1-Всі товари 2-Пошук за номером товару 3-Пошук за назвою товару:")
    if answer == "0":
        break

    elif answer == "1":
        products = db.get_all_products()
        for product in products:
            print(f"Товар:{product[0]} - {product[1]} - {product[2]}грн.")

    elif answer == "2":    
        product_id = int(input("Введіть номер товару:"))
        product = db.get_product(product_id)
        print(f"Товар:{product[0]} - {product[1]} \n {product[2]}грн.  {product[3]} \n Кількість: {product[4]}")

    elif answer == "3":
        title = input("Введіть назву товару:")
        products = db.search_product(title)
        if products:
            for product in products:
                print(f"Товар:{product[0]} - {product[1]} - {product[2]}грн.")
        else:
            print("За вашим запитом нічого не знайдено")

    elif answer == "4":
        category_title = input("Введіть назву категорії:")
        category = db.search_title_categories(category_title)
      








#зробити реєстрацію

#зробити пошук за категоріями