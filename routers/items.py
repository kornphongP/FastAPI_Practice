from typing import Union
from fastapi import APIRouter, Request

# pydantic > BaseModel ใช้ในการทำ Type Checking และ Validation
from pydantic import BaseModel

router = APIRouter(prefix="/items", tags=["items"])


class Item(BaseModel):
    name: str
    price: float


# parameter ( http://127.0.0.1:8000/items/1 )
@router.get("/{item_id}")
def read_item(item_id: int):  # กำหนด Type ที่จะ Convert และ Validate ไปในตัว
    return {"item_id": item_id}


# สารมารถไปใช้ BaseModel Item ที่ทำไว้ได้ เอา Async ออกได้เลยเพราะโดนไปทำงานเบื้องหลัง
@router.post("/")
def create_item(item: Item):
    # print(item.name)
    return {"request.body": item}


@router.put("/{item_id}")
def edit_item(item_id: int, item: Item):
    return {"id": item_id, "request body": item}


@router.delete("/{item_id}")
def delete_item(item_id: int, item: Item):
    return {"message": f"Item {item_id} - {item.name} deleted"}
