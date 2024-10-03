from fastapi import FastAPI, File, UploadFile
from typing_extensions import Annotated

app = FastAPI()

@app.post("/file/")
async def use_file(file: Annotated[bytes, File()]):
        return {"file_size": len(file)}

@app.post("/upload_file/")
async def use_upload_file(file: UploadFile):
        return {"file_name": file.filename}