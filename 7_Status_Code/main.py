from fastapi import FastAPI

app = FastAPI()

@app.get("/", status_code=201)
async def root():
        return "Hello world!"