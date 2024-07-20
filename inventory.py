import sqlite3
from config import DB_NAME

def add_product(name, price, quantity):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)", (name, price, quantity))
    conn.commit()
    conn.close()

def get_all_products():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM products")
    products = c.fetchall()
    conn.close()
    return products

if __name__ == "__main__":
    add_product("Sample Product", 10.0, 100)
    products = get_all_products()
    for product in products:
        print(product)
