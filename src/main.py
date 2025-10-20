import uuid
from collections.abc import Iterable

from fastapi import FastAPI
from pydantic import BaseModel

from .fib import PositiveInt
from .fib import fib as lib_fib


class Item(BaseModel):
    id: uuid.UUID
    name: str


items: dict[uuid.UUID, Item] = {}

app = FastAPI()


@app.get("/items")
def get_items() -> Iterable[Item]:
    return items.values()


@app.get("/items/{item_id}")
def get_item(item_id: uuid.UUID) -> Item | None:
    return items.get(item_id)


@app.post("/items")
def create_item(name: str) -> uuid.UUID:
    id = uuid.uuid4()
    items[id] = Item(id=id, name=name)
    return id


@app.get("/fib/{n}")
def fib(n: PositiveInt) -> PositiveInt:
    return lib_fib(n)
