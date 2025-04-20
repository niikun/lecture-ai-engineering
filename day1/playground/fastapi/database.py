import sqlite3

def init_db():
    """SQLiteデータベースの初期化"""
    conn = sqlite3.connect("test.db")
    conn.execute(
        """CREATE TABLE IF NOT EXISTS test(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL NOT NULL,
        description TEXT
        )"""
    )
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM test")
    count = c.fetchone()[0]
    if count == 0:
        c.execute("INSERT INTO test (name, price, description) VALUES('shoes', 1000, 'red shoes')")
        c.execute("INSERT INTO test (name, price, description) VALUES('bag', 2000, 'blue bag')")
        c.execute("INSERT INTO test (name, price, description) VALUES('hat', 3000, 'green hat')")
        conn.commit()
    conn.close()
    print("データベースを初期化しました。")

def get_item_by_id(item_id:int):
    """指定されたIDのアイテムを取得"""
    with sqlite3.connect("test.db") as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM test WHERE id = ?", (item_id,))
        item = c.fetchone()
        return item
    
def insert_item(name:str, price:float, description:str):
    """新しいアイテムをデータベースに挿入"""
    with sqlite3.connect("test.db") as conn:
        c = conn.cursor()
        c.execute("INSERT INTO test (name, price, description) VALUES(?, ?, ?)", 
                  (name, price, description))
        conn.commit()
