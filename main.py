from fastapi import FastAPI
from routers import items, records


app = FastAPI()
app.include_router(items.router, prefix="/test")
app.include_router(records.router, prefix="/test")


@app.get("/fetch")
def hello_world():
    return {"message": "Hello, World!"}
