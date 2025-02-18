
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Candidate, CandidateMarketing, Placement
from schemas import CandidateCreate, CandidateUpdate, CandidateResponse
from typing import List
from datetime import datetime

router = APIRouter()

@router.get("/candidates", response_model=List[CandidateResponse])
def get_candidates(db: Session = Depends(get_db)):
    candidates = db.query(Candidate).order_by(Candidate.candidateid.desc()).all()
    return candidates

@router.post("/candidates", response_model=CandidateResponse)
def insert_candidate(candidate: CandidateCreate, db: Session = Depends(get_db)):
    new_candidate = Candidate(**candidate.dict())
    db.add(new_candidate)
    db.commit()
    db.refresh(new_candidate)
    return new_candidate

@router.put("/candidates/{id}", response_model=CandidateResponse)
def update_candidate(id: int, candidate_data: CandidateUpdate, db: Session = Depends(get_db)):
    candidate = db.query(Candidate).filter(Candidate.candidateid == id).first()
    if not candidate:
        raise HTTPException(status_code=404, detail="Candidate not found")
    
    for key, value in candidate_data.dict(exclude_unset=True).items():
        setattr(candidate, key, value)
    
    db.commit()
    db.refresh(candidate)
    
    if candidate.status and candidate.status.lower() == "placed":
        placement = Placement(candidateid=id, placementDate=datetime.utcnow())
        db.add(placement)
        db.commit()
        db.refresh(placement)
    
    return candidate

@router.delete("/candidates/{id}")
def delete_candidate(id: int, db: Session = Depends(get_db)):
    candidate = db.query(Candidate).filter(Candidate.candidateid == id).first()
    if not candidate:
        raise HTTPException(status_code=404, detail="Candidate not found")
    
    db.query(CandidateMarketing).filter(CandidateMarketing.candidateid == id).delete()
    db.delete(candidate)
    db.commit()
    
=======
# candidate_controller.py
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from datetime import datetime
from app.models import Candidate, Placement, engine
from app.schemas import CandidateBase
from sqlalchemy import select
from typing import List

# Router instance
router = APIRouter()

# Dependency to get the DB session
def get_db():
    db = Session(bind=engine)
    try:
        yield db
    finally:
        db.close()

# Get all candidates
@router.get("/candidates", response_model=List[CandidateBase])
def get_candidates(db: Session = Depends(get_db)):
    candidates = db.execute(select(Candidate).order_by(Candidate.candidateid.desc())).fetchall()
    return candidates

# Insert a new candidate
@router.post("/candidates", response_model=CandidateBase)
def insert_candidate(new_candidate: CandidateBase, db: Session = Depends(get_db)):
    candidate_data = new_candidate.dict(exclude_unset=True)

    # Insert into the candidate table
    candidate = Candidate(**candidate_data)
    db.add(candidate)
    db.commit()
    db.refresh(candidate)

    return {**candidate_data, "candidateid": candidate.candidateid}

# Update a candidate
@router.put("/candidates/{candidate_id}", response_model=CandidateBase)
def update_candidate(candidate_id: int, updated_candidate: CandidateBase, db: Session = Depends(get_db)):
    candidate = db.execute(select(Candidate).where(Candidate.candidateid == candidate_id)).scalar_one_or_none()

    if candidate is None:
        raise HTTPException(status_code=404, detail="Candidate not found")

    # Update candidate details
    updated_data = updated_candidate.dict(exclude_unset=True)
    for key, value in updated_data.items():
        setattr(candidate, key, value)
    
    db.commit()

    # If status is 'placed', insert into placement table
    if updated_candidate.status and updated_candidate.status.lower() == 'placed':
        placement_data = Placement(candidateid=candidate_id, placementDate=datetime.now())
        db.add(placement_data)
        db.commit()

    return {**updated_data, "candidateid": candidate_id}

# Delete a candidate
@router.delete("/candidates/{candidate_id}")
def delete_candidate(candidate_id: int, db: Session = Depends(get_db)):
    candidate = db.execute(select(Candidate).where(Candidate.candidateid == candidate_id)).scalar_one_or_none()

    if candidate is None:
        raise HTTPException(status_code=404, detail="Candidate not found")

    # Delete related marketing records
    db.execute(f"DELETE FROM candidatemarketing WHERE candidateid = {candidate_id}")
    db.commit()

    # Delete the candidate record
    db.delete(candidate)
    db.commit()
    return {"message": "Candidate deleted successfully"}
