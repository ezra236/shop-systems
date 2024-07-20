import sqlite3
from config import DB_NAME

def record_sale(product_id, quantity, total_price):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO sales (product_id, quantity, total_price) VALUES (?, ?, ?)", (product_id, quantity, total_price))
    conn.commit()
    conn.close()

def get_sales():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM sales")
    sales = c.fetchall()
    conn.close()
    return sales

if __name__ == "__main__":
    record_sale(1, 2, 20.0)
    sales = get_sales()
    for sale in sales:
        print(sale)
