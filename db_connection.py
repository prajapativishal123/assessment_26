import psycopg2

def get_connection():
    try:
        conn = psycopg2.connect(
            database="your_database",
            user="your_user",
            password="your_password",
            host="your_host",
            port="your_port"
        )
        return conn
    except Exception as e:
        print("Error connecting to the database:", e)
        return None
