# models.py
from db_connection import get_connection

class ProductManager:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def register(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO product_manager (username, password) VALUES (%s, %s)", (self.username, self.password))
        conn.commit()
        cursor.close()
        conn.close()

    def login(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM product_manager WHERE username=%s AND password=%s", (self.username, self.password))
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return result is not None

class Customer:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.__balance = 0.0

    def register(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO customer (username, password, balance) VALUES (%s, %s, %s)", (self.username, self.password, self.__balance))
        conn.commit()
        cursor.close()
        conn.close()

    def login(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM customer WHERE username=%s AND password=%s", (self.username, self.password))
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        if result:
            self.__balance = result[3]
        return result is not None

    def get_balance(self):
        return self.__balance

    def update_balance(self, amount):
        self.__balance += amount
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE customer SET balance=%s WHERE username=%s", (self.__balance, self.username))
        conn.commit()
        cursor.close()
        conn.close()

class Product:
    def __init__(self, name, stock, price):
        self.name = name
        self.stock = stock
        self.price = price

    def add_product(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO product (name, stock, price) VALUES (%s, %s, %s)", (self.name, self.stock, self.price))
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def get_all_products():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM product")
        products = cursor.fetchall()
        cursor.close()
        conn.close()
        return products

    @staticmethod
    def update_stock(product_id, stock):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE product SET stock=%s WHERE product_id=%s", (stock, product_id))
        conn.commit()
        cursor.close()
        conn.close()
