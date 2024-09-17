from db import DatabaseManager

db = DatabaseManager("shop_dp.db")
current_user = None
current_order_id = None

def print_products(products):
    if products:
        for product in products:
            print(f"Товар:{product[0]} - {product[1]} - {product[2]}грн.")
    else:
        print("За вашим запитом нічого не знайдено")

def add_to_cart(product_id):
    global current_order_id
    product = db.get_product(product_id)
    if current_user:
        if product:
            quantity = int(input("Введіть кількість товару:"))
            if not current_order_id:
                current_order_id = db.create_order(current_user[0])
            db.add_to_order(product_id,quantity,current_order_id)
            print("Товар додано до замовлення")
        else:
            print("Такого товару нема!!")
    else:
        print("Спочатку зареєструйтесь або ввійдіть в профіль!")


while True:
    answer = input("Виберіть дію.0-Кінець1-Всі товари 2-Пошук за номером товару 3-Пошук за назвою товару 4-Пошук за категорією,5-Створити профіль:")
    if answer == "0":
        break

    elif answer == "1":
        
        products = db.get_all_products()
        print_products(products)
        item_id = int(input("Введіть номер товару який ви хочете додати в кошик:"))
        add_to_cart(item_id)
    elif answer == "2":     
        product_id = int(input("Введіть номер товару:"))
        product = db.get_product(product_id)
        print_products([product])
        yes_no = input("Чи хочете ви додати цей товар до кошика?:").lower()
        if yes_no == "так":
            add_to_cart(product_id)
            
    elif answer == "3":
        title = input("Введіть назву товару:")
        products = db.search_product(title)
        print_products(products)
        item_id = int(input("Введіть номер товару який ви хочете додати в кошик:"))
        add_to_cart(item_id)

    elif answer == "4":
        category_title = input("Введіть назву категорії:")
        products = db.search_title_categories(category_title)
        print_products(products)  
        item_id = int(input("Введіть номер товару який ви хочете додати в кошик:"))
        add_to_cart(item_id)
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

    elif answer == "6":
        email = input("Ваш зареєстрований email:")
        password = input("Ваш пароль:")
        current_user = db.check_user(email,password)
        if current_user:
            print("Вітаємо ",current_user[1],current_user[2])
        else:
            print("Неправильний email або пароль")
        
    elif answer == "7":
        city = input("Введіть ваше місто:")
        address = input("Введіть ваш адрес:")
        comment = input("Введіть коментар до замовлення:")
        db.submit_order(current_order_id,city,address,comment)
        current_order_id = None
        print("ЗАмовлення оформлено!")


#зробити в таблиці orders його статус на оформлене неоформлене в дорозі
#зробити відображення кошика
#зробити видалення товару з кошика