from fastapi import FastAPI
from routers.v1 import routers


app = FastAPI()
for router, prefix in routers:
    app.include_router(router, prefix=prefix)


@app.get("/fetch")
def hello_world():
    return {"message": "Hello, World!"}
