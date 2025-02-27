from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database.db import engine, Base


from app.routes.batchRoute import router as batch_router
from app.routes.accessRoute import router as access_router
from app.routes.authRoute import router as auth_router
from app.routes.accessRoute import router as user_router
from app.routes.leadsRoute import router as leads_router
from app.routes.candidateRoute import router as candidate_router
from app.routes.candidate_searchRoute import router as candidate_search_router
from app.routes.poRoute import router as po_router  
from app.routes.candidateMarketingRoute import router as candidate_marketing_router  


app = FastAPI()

origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],  
)

Base.metadata.create_all(bind=engine)


app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(access_router, prefix="/access", tags=["access"])
app.include_router(batch_router, prefix="/batch", tags=["batch"]) 
app.include_router(user_router, prefix="/admin", tags=["users"])
app.include_router(leads_router, prefix="/leads", tags=["leads"])  
app.include_router(candidate_router, prefix="/candidates", tags=["candidates"])
app.include_router(candidate_search_router, prefix="/candidate_search", tags=["candidate_search"])
app.include_router(po_router,tags=["po"])
app.include_router(candidate_marketing_router, tags=["candidate_Marketing"])  


@app.get("/")
def read_root():
    return {"message": "Welcome to the Avatar"}