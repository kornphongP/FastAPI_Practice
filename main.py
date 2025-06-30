from typing import Union
from fastapi import FastAPI, Request

# pydantic > BaseModel ใช้ในการทำ Type Checking และ Validation
from pydantic import BaseModel


# เหมือนทำ Schema
class Item(BaseModel):
    name: str
    price: float


app = FastAPI()


@app.get("/fetch")
def hello_world():
    return {"message": "Hello, World!"}


# parameter ( http://127.0.0.1:8000/items/1 )
@app.get("/items/{item_id}")
def read_item(item_id: int):  # กำหนด Type ที่จะ Convert และ Validate ไปในตัว
    return {"item_id": item_id}


# query string (?) USE Union ( http://127.0.0.1:8000/records/1?q=test )
@app.get("/records/{record_id}")
def read_item2(record_id: int, q: Union[str, None] = None):
    return {"record_id": record_id, "q": q}


# Request จะทำงานแบบ Asynchronus จึงต้องใช้ async def
@app.post("/records")
async def create_item(request: Request):
    body = await request.json()
    return {"request.body": body}


# สารมารถไปใช้ BaseModel Item ที่ทำไว้ได้ เอา Async ออกได้เลยเพราะโดนไปทำงานเบื้องหลัง
@app.post("/items")
def create_item(item: Item):
    # print(item.name)
    return {"request.body": item}


@app.put("/items/{item_id}")
def edit_item(item_id: int, item: Item):
    return {"id": item_id, "request body": item}


@app.delete("/items/{item_id}")
def delete_item(item_id: int, item: Item):
    return {"message": f"Item {item_id} - {item.name} deleted"}
