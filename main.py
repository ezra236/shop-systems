import sqlite3
from config import DB_NAME

def create_connection():
    conn = sqlite3.connect(DB_NAME)
    return conn

def create_tables():
    conn = create_connection()
    c = conn.cursor()
    
    c.execute('''CREATE TABLE IF NOT EXISTS products (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    price REAL NOT NULL,
                    quantity INTEGER NOT NULL)''')

    c.execute('''CREATE TABLE IF NOT EXISTS sales (
                    id INTEGER PRIMARY KEY,
                    product_id INTEGER,
                    quantity INTEGER,
                    total_price REAL,
                    FOREIGN KEY(product_id) REFERENCES products(id))''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()
    print("Database and tables created.")
