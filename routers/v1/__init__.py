from .items import router as items_router
from .records import router as records_router

routers = [
    (items_router, "/v1"),
    (records_router, "/v1"),
]
