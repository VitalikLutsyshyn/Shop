import sqlite3 


class DatabaseManager:
    def __init__(self,dbname):
        self.dbname = dbname
        self.connect = None
        self.cursor = None

    def open(self):
        self.connect = sqlite3.connect(self.dbname)
        self.cursor = self.connect.cursor()
        
    def close(self):
        self.cursor.close()
        self.connect.close()

    def get_all_products(self):
        self.open()
        self.cursor.execute("""SELECT id,title,price FROM products """)
        products = self.cursor.fetchall()
        self.close()
        return products
    
    def get_product(self,product_id):
        self.open()
        self.cursor.execute("""SELECT * FROM products WHERE id =? """,[product_id])
        product = self.cursor.fetchone()
        self.close()
        return product
        
    def search_product(self,product_title):
        self.open()
        self.cursor.execute("""SELECT * FROM products WHERE title LIKE? """,['%'+product_title+'%'])
        products = self.cursor.fetchall()
        self.close()
        return products


#функція реєстрації

        
