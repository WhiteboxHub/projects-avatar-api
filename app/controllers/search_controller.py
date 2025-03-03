# from fastapi import FastAPI, Request, HTTPException, Depends
# from sqlalchemy import create_engine, text
# from sqlalchemy.orm import sessionmaker, Session
# import os

# database_url = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/whiteboxqa")
# engine = create_engine(database_url)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# app = FastAPI()

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# @app.get("/searchCandidatesByName")
# def search_candidates_by_name(name: str, db: Session = Depends(get_db)):
#     query = text("""
#         SELECT * 
#         FROM wbl_db.candidate
#         WHERE name LIKE :name;
#     """)
    
#     params = {"name": f"%{name}%"}
    
#     try:
#         result = db.execute(query, params)
#         candidates = result.mappings().all()
#         return candidates
#     except Exception as e:
#         raise HTTPException(status_code=500, detail="Database error")


from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.db import get_db  # Importing the DB session dependency
from app.models import Candidate  # Importing the ORM model

app = FastAPI()

@app.get("/searchCandidatesByName")
def search_candidates_by_name(name: str, db: Session = Depends(get_db)):
    """
    Search for candidates by name using SQLAlchemy ORM.
    """
    try:
        candidates = db.query(Candidate).filter(Candidate.name.ilike(f"%{name}%")).all()
        return candidates
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")