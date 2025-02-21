from fastapi import FastAPI, Request, HTTPException, Depends
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, Session
import os

database_url = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/whiteboxqa")
engine = create_engine(database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/searchCandidatesByName")
def search_candidates_by_name(name: str, db: Session = Depends(get_db)):
    query = text("""
        SELECT * 
        FROM whiteboxqa.candidate
        WHERE name LIKE :name;
    """)
    
    params = {"name": f"%{name}%"}
    
    try:
        result = db.execute(query, params)
        candidates = result.mappings().all()
        return candidates
    except Exception as e:
        raise HTTPException(status_code=500, detail="Database error")