from fastapi import APIRouter, HTTPException, Depends, Query
from sqlalchemy.orm import Session
from typing import List
from app.models import Candidate  # Ensure Candidate model has __tablename__ = "candidate"
from app.schemas import CandidateResponse, CandidateCreate, CandidateUpdate
from app.database.db import get_db
from app.middleware.admin_validation import admin_validation

router = APIRouter()

@router.get("/candidates", response_model=dict)
def get_candidates(
    page: int = Query(1, alias="page"),
    pageSize: int = Query(100, alias="pageSize"),
    search: str = Query(None, alias="search"),
    db: Session = Depends(get_db),
    _: bool = Depends(admin_validation)
):
    offset = (page - 1) * pageSize
    query = db.query(Candidate)
    
    if search:
        query = query.filter(Candidate.name.ilike(f"%{search}%"))

    totalRows = query.count()
    candidates = query.order_by(Candidate.candidateid.desc()).offset(offset).limit(pageSize).all()
    
    return {"data": candidates, "totalRows": totalRows}

@router.post("/candidates/insert", response_model=CandidateResponse)
def insert_candidate(
    candidate: CandidateCreate,
    db: Session = Depends(get_db)
):
    new_candidate = Candidate(**candidate.dict())
    db.add(new_candidate)
    db.commit()
    db.refresh(new_candidate)
    return new_candidate

@router.put("/candidates/update/{id}", response_model=CandidateResponse)
def update_candidate(
    id: int,
    candidate_update: CandidateUpdate,
    db: Session = Depends(get_db),
    _: bool = Depends(admin_validation)
):
    candidate = db.query(Candidate).filter(Candidate.candidateid == id).first()
    
    if not candidate:
        raise HTTPException(status_code=404, detail="Candidate not found")
    
    for key, value in candidate_update.dict(exclude_unset=True).items():
        setattr(candidate, key, value)
    
    db.commit()
    db.refresh(candidate)
    return candidate

@router.delete("/candidates/delete/{id}")
def delete_candidate(
    id: int,
    db: Session = Depends(get_db),
    _: bool = Depends(admin_validation)
):
    candidate = db.query(Candidate).filter(Candidate.candidateid == id).first()
    
    if not candidate:
        raise HTTPException(status_code=404, detail="Candidate not found")
    
    db.delete(candidate)
    db.commit()
    return {"message": "Candidate deleted successfully"}

@router.get("/candidates/search", response_model=dict)
def search_candidates(
    search: str = Query(None, alias="search"),
    page: int = Query(1, alias="page"),
    pageSize: int = Query(10, alias="pageSize"),
    db: Session = Depends(get_db),
    _: bool = Depends(admin_validation)
):
    offset = (page - 1) * pageSize
    query = db.query(Candidate).filter(Candidate.name.ilike(f"%{search}%"))
    
    totalRows = query.count()
    candidates = query.offset(offset).limit(pageSize).all()
    
    return {"data": candidates, "totalRows": totalRows}
