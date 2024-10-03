import string
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException

class Image(BaseModel):
        url: str
        name: str

class Item(BaseModel):
        name:str
        description:str | None = None
        price: float
        tax: float | None = None
        tags: set[str] = set()
        image: Image | None = None


app = FastAPI()

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
        result = {"item_id": item_id, "item": item}
        return result
