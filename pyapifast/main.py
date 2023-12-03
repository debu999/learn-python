"""
    fast api main call to run with uvicorn

Returns:
    Does not return anything: Have rest endpoints
"""
from typing import Union
from pyapifast.apis import userapi
from anyio import CapacityLimiter
from anyio.lowlevel import RunVar
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
app.include_router(userapi.router)


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.on_event("startup")
def startup():
    print("start")
    # The line `RunVar("_default_thread_limiter").set(CapacityLimiter(2))` is setting the default
    # thread limiter to a `CapacityLimiter` object with a capacity of 2.
    RunVar("_default_thread_limiter").set(CapacityLimiter(2))


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}
