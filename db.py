import sqlite3

class Database:
    def __init__(self, db):
        self.db_connection = sqlite3.connect(db)
        self.cur = self.db_connection.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS wish_list_items (id INTEGER PRIMARY KEY, list_name text, brand_name text, retailer text, price text)")
        self.db_connection.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM parts")
        rows = self.cur.fetchall()
        return rows

        def insert(self, part, customer, retailer, price):
            self.cur.execute("INSERT INTO parts VALUES (NULL, ?, ?, ?, ?)",
                            (part, customer, retailer, price))
            self.db_connection.commit()

        def remove(self, id):
            self.cur.execute("DELETE FROM parts WHERE id=?", (id,))
            self.db_connection.commit()

        def update(self, id, part, customer, retailer, price):
            self.cur.execute("UPDATE parts SET part = ?, customer = ?, retailer = ?, price = ? WHERE id = ?",
                            (part, customer, retailer, price, id))
            self.db_connection.commit()

        def __del__(self):
            self.db_connection.close()