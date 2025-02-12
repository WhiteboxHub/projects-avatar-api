from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database.db import engine, Base
from app.routes.batchRoute import router as batch_router
from app.routes.authRoute import router as auth_router
from app.routes.accessRoute import router as user_router
from app.routes.leadsRoute import router as leads_router
from app.routes.candidateRoute import router as candidate_router
from app.routes.employeeRoute import router as employee_router

# Initialize FastAPI app
app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Change to your frontend URL for security
#     allow_credentials=True,
#     allow_methods=["*"],  # Allow all HTTP methods
#     allow_headers=["*"],  # Allow all headers
# )


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Change to your frontend URL for security
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)


# Create all database tables if they don't exist
Base.metadata.create_all(bind=engine)

# Include routes with proper prefixes and tags
app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(batch_router, prefix="", tags=["batch"])
app.include_router(user_router, prefix="/admin", tags=["users"])
app.include_router(leads_router, prefix="", tags=["leads"])
app.include_router(candidate_router, prefix="/candidates", tags=["candidates"])
app.include_router(employee_router)

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Avatar"}
