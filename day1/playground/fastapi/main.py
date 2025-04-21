from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from typing import Union
import database
from fastapi.middleware.cors import CORSMiddleware

# ---Middleware設定 ---
app = FastAPI()
# CORSミドルウェアを追加
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
database.init_db()

class Item(BaseModel):
    name: str 
    price: float 
    description: Union[str, None] = None
@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def get_item(item_id:int):
    item = database.get_item_by_id(item_id)
    if item:
        return {"id": item[0], "name": item[1], "price": item[2], "description": item[3]}
    else:
        return {"error": "Item not found"}
    
@app.post("/items")
def create_item(item:Item):
    print(f"登録します。{item.name}, {item.price}, {item.description}")
    database.insert_item(item.name, item.price, item.description)
    return item
