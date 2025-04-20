from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from typing import Union
import sqlite3

# FastAPIのインポート
app = FastAPI()

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
if count ==0:
    c.execute("INSERT INTO test (name, price, description) VALUES('shoes', 1000, 'red shoes')")
    c.execute("INSERT INTO test (name, price, description) VALUES('bag', 2000, 'blue bag')")
    c.execute("INSERT INTO test (name, price, description) VALUES('hat', 3000, 'green hat')")
    conn.commit()
conn.close()
# SQLite3のインポート

# JSONデータ用のクラスを定義
class Item(BaseModel):
    name: str 
    price: float 
    description: Union[str, None] = None

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def get_item(item_id:int):
    with sqlite3.connect("test.db") as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM test WHERE id = ?",(item_id,))
        item = c.fetchone()
        if item:
            return {"id": item[0], "name": item[1], "price": item[2], "description": item[3]}
        else:
            return {"error": "Item not found"}

    
@app.post("/items")
def create_item(item:Item):
    print(f"登録します。{item.name}, {item.price}, {item.description}")
    with sqlite3.connect("test.db") as conn:
        c = conn.cursor()
        c.execute("INSERT INTO test (name, price, description) VALUES(?, ?, ?)", 
                  (item.name, item.price, item.description))
        conn.commit()
        c.execute("SELECT * FROM test")
        item_all = c.fetchall()
        for row in item_all:
            print(row)

    return item
