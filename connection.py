# db_connection.py
import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="product_management"
    )
