from fastapi import FastAPI
from app.database.db import engine, Base
from app.routes.batchRoute import router as batch_router
from app.routes.authRoute import router as auth_router
from app.routes.accessRoute import router as user_router

# Initialize FastAPI app
app = FastAPI()

# Create all database tables if they don't exist
Base.metadata.create_all(bind=engine)

# Include routes with proper prefixes and tags
app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(batch_router, prefix="/batch", tags=["batch"])
app.include_router(user_router, prefix="/users", tags=["users"])


# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Avatar"}
