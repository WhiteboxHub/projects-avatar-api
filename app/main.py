from fastapi import FastAPI
from app.database.db import engine, Base
from app.routes.authRoute import router as auth_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth_router, prefix="/auth", tags=["auth"])

@app.get("/")
def read_root():
    return {"Welcome to the Avatar"}
