from fastapi import FastAPI
from database import create_db_tables
from routers.animals import router

app = FastAPI()

create_db_tables()

app.include_router(router)

@app.get("/")
async def root():
    return {"message": "Hello World"}