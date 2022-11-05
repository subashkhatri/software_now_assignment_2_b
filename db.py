import sqlite3

class Database:
    def __init__(self, db):
        self.db_connection = sqlite3.connect(db)
        self.cur = self.db_connection.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS wish_list_items (id INTEGER PRIMARY KEY, list_name text, brand_name text, retailer text, price text)")
        self.db_connection.commit()