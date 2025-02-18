from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from datetime import datetime
from app.models import Candidate, Placement, engine
from app.schemas import CandidateBase
from sqlalchemy import select
from typing import List

router = APIRouter()

def get_db():
    db = Session(bind=engine)
    try:
        yield db
    finally:
        db.close()


@router.get("/candidates", response_model=List[CandidateBase])
def get_candidates(db: Session = Depends(get_db)):
    candidates = db.execute(select(Candidate).order_by(Candidate.candidateid.desc())).fetchall()
    return candidates

@router.post("/candidates", response_model=CandidateBase)
def insert_candidate(new_candidate: CandidateBase, db: Session = Depends(get_db)):
    candidate_data = new_candidate.dict(exclude_unset=True)

   
    candidate = Candidate(**candidate_data)
    db.add(candidate)
    db.commit()
    db.refresh(candidate)

    return {**candidate_data, "candidateid": candidate.candidateid}


@router.put("/candidates/{candidate_id}", response_model=CandidateBase)
def update_candidate(candidate_id: int, updated_candidate: CandidateBase, db: Session = Depends(get_db)):
    candidate = db.execute(select(Candidate).where(Candidate.candidateid == candidate_id)).scalar_one_or_none()

    if candidate is None:
        raise HTTPException(status_code=404, detail="Candidate not found")

    updated_data = updated_candidate.dict(exclude_unset=True)
    for key, value in updated_data.items():
        setattr(candidate, key, value)
    
    db.commit()

    if updated_candidate.status and updated_candidate.status.lower() == 'placed':
        placement_data = Placement(candidateid=candidate_id, placementDate=datetime.now())
        db.add(placement_data)
        db.commit()

    return {**updated_data, "candidateid": candidate_id}

@router.delete("/candidates/{candidate_id}")
def delete_candidate(candidate_id: int, db: Session = Depends(get_db)):
    candidate = db.execute(select(Candidate).where(Candidate.candidateid == candidate_id)).scalar_one_or_none()

    if candidate is None:
        raise HTTPException(status_code=404, detail="Candidate not found")

    db.execute(f"DELETE FROM candidatemarketing WHERE candidateid = {candidate_id}")
    db.commit()

    db.delete(candidate)
    db.commit()

    return {"message": "Candidate deleted successfully"}
