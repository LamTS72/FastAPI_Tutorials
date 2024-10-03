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

@app.get("/items", response_model=list[Item])
async def update_item():
        result = [
                {"name":"A", "price": 42.0},
                {"name":"B", "price":92.3}
        ]
        return result