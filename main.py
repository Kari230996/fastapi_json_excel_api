from fastapi import FastAPI, Request, Form
from fastapi.responses import JSONResponse, StreamingResponse
from pydantic import BaseModel
from typing import List, Optional
import io 
import pandas as pd

app = FastAPI()

storage = []

class Item(BaseModel):
    name: str
    age: int
    email: str

@app.post("/items/")
async def create_item(item: Item, format: Optional[str] = None):
    storage.append(item.dict())
    if format == "excel":
        df = pd.DataFrame([item.dict()])
        stream = io.BytesIO()
        df.to_excel(stream, index=False)
        stream.seek(0)

        return StreamingResponse(stream, media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                                 headers={"Content-Disposition": "attachment; filename=item.xlsx"})

    return item

@app.get("/items/")
async def get_items(format: Optional[str] = None):
    if format == "excel":
        df = pd.DataFrame(storage)
        stream = io.BytesIO()
        df.to_excel(stream, index=False)
        stream.seek(0)
        return StreamingResponse(stream, media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                                 headers={"Content-Disposition": "attachment; filename=items.xlsx"})
    return JSONResponse(content={"data": storage})