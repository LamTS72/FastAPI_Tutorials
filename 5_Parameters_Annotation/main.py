from typing import Annotated
from gguf import Path
from pydantic import BaseModel
from fastapi import FastAPI, Path, Query
app = FastAPI()

@app.get("/items/{item_id}")
async def get_item(
        item_id: Annotated[int, Path(title="The ID of item to get")], 
        q: Annotated[str | None, Query(alias="Item to get")] = None
        ):
        result = {"item_id": item_id}
        if q:
                result.update({"q":q})
        return result
