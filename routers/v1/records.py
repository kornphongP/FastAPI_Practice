from typing import Union
from fastapi import APIRouter, Request

router = APIRouter(prefix="/records", tags=["records"])


# query string (?) USE Union ( http://127.0.0.1:8000/records/1?q=test )
@router.get("/{record_id}")
def read_item2(record_id: int, q: Union[str, None] = None):
    return {"record_id": record_id, "q": q}


# Request จะทำงานแบบ Asynchronus จึงต้องใช้ async def
@router.post("")
async def create_item(request: Request):
    body = await request.json()
    return {"request.body": body}
