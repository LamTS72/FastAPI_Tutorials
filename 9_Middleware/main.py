from re import S
from fastapi import FastAPI, Request
import time
app = FastAPI()

@app.get("/")
async def root():
        return {
                "msg":"Hello, world"
        }

@app.middleware("http")
async def add_process_time(request: Request, call_next):
        start = time.time()     
        response = await call_next(request)
        process_time = time.time() - start
        response.headers["X-Process-Time"] = str(process_time)

        return response