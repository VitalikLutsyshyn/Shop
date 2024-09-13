from db import DatabaseManager

db = DatabaseManager("shop_dp.db")

def print_products(products):
    if products:
        for product in products:
            print(f"Товар:{product[0]} - {product[1]} - {product[2]}грн.")
    else:
        print("За вашим запитом нічого не знайдено")


while True:
    answer = input("Виберіть дію.0-Кінець1-Всі товари 2-Пошук за номером товару 3-Пошук за назвою товару 4-Пошук за категорією,5-Створити профіль:")
    if answer == "0":
        break

    elif answer == "1":
        products = db.get_all_products()
        print_products(products)
    elif answer == "2":    
        product_id = int(input("Введіть номер товару:"))
        product = db.get_product(product_id)
        print_products([product])

    elif answer == "3":
        title = input("Введіть назву товару:")
        products = db.search_product(title)
        print_products(products)

    elif answer == "4":
        category_title = input("Введіть назву категорії:")
        products = db.search_title_categories(category_title)
        print_products(products)  

    elif answer == "5":
        name = input("Ваше ім'я: ")
        surname = input("Прізвище:")    
        email = input("Email: ")
        phone_number = input("Номер")
        password = input("Пароль:")
        is_user_registered = db.create_user(name, surname, email, phone_number, password)
        if is_user_registered == True:
            print("Профіль створено")
        else:
            print("Такий email або номер телефону вже є!!")



#зробити функцію login яка має запитувати email і пароль і перевіряти за допомогою SELECT з AND