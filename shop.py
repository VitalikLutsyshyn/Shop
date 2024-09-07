import sqlite3 
connect = sqlite3.connect("shop_dp.db")
cursor = connect.cursor()

cursor.execute('''SELECT * FROM categories WHERE title =="Техніка" ''')




connect.commit()