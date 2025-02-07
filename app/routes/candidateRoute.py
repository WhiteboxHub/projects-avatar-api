from fastapi import APIRouter, HTTPException, Request, Depends
from sqlalchemy.orm import Session
from typing import List
from sqlalchemy import select
from pydantic import BaseModel
from app.models import Candidate
from app.schemas import CandidateBase
from app.database.db import get_db
from app.models import Placement
from app.middleware.admin_validation import admin_validation, ALGORITHM
from datetime import datetime

router = APIRouter()
# Route to get candidates with pagination and search
@router.get('/candidates', response_model=List[CandidateBase])
def get_candidates(
    db: Session = Depends(get_db), 
    page: int = 1, 
    page_size: int = 100, 
    search: str = '', 
    admin_validation: bool = Depends(admin_validation)
):
    offset = (page - 1) * page_size
    query = f"""
        SELECT 
            candidateid, name, email, phone, course, batchname, enrolleddate, status, diceflag, 
            education, workstatus, dob, portalid, agreement, driverslicense, 
            workpermit, wpexpirationdate, offerletterurl, ssnvalidated, address, 
            city, state, country, zip, emergcontactname, emergcontactemail, 
            emergcontactphone, emergcontactaddrs, guidelines, term, referralid, 
            salary0, salary6, salary12, originalresume, notes 
        FROM candidate
        ORDER BY candidateid DESC
    """
    count_query = "SELECT COUNT(*) AS total FROM candidate"
    query_params = []
    count_params = []

    if search:
        query += " WHERE name LIKE ? OR candidateid LIKE ?"
        count_query += " WHERE name LIKE ? OR candidateid LIKE ?"
        query_params.append(f"%{search}%")
        count_params.append(f"%{search}%")

    query += " LIMIT ? OFFSET ?"
    query_params.extend([page_size, offset])

    # Get candidates data with pagination
    try:
        db.execute(query, query_params)
        results = db.fetchall()
        db.execute(count_query, count_params)
        count_results = db.fetchall()
        total_rows = count_results[0]['total']
        return {"data": results, "totalRows": total_rows}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database query error: {str(e)}")

# Route to insert a new candidate
@router.post('/candidates/insert', response_model=CandidateBase)
def insert_candidate(new_candidate: CandidateBase, db: Session = Depends(get_db)):
    try:
        # Insert the new candidate
        candidate_data = new_candidate.dict(exclude_unset=True)
        new_candidate = Candidate(**candidate_data)
        db.add(new_candidate)
        db.commit()
        db.refresh(new_candidate)

        return {**candidate_data, "candidateid": new_candidate.candidateid}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database insert error: {str(e)}")

# Route to update an existing candidate
@router.put('/candidates/update/{candidate_id}', response_model=CandidateBase)
def update_candidate(candidate_id: int, updated_candidate: CandidateBase, db: Session = Depends(get_db), admin_validation: bool = Depends(admin_validation)):
    try:
        # Check if candidate exists
        candidate = db.execute(select(Candidate).where(Candidate.candidateid == candidate_id)).scalar_one_or_none()
        if not candidate:
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
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database update error: {str(e)}")

# Route to delete a candidate
@router.delete('/candidates/delete/{candidate_id}')
def delete_candidate(candidate_id: int, db: Session = Depends(get_db), admin_validation: bool = Depends(admin_validation)):
    try:
        # Check if candidate exists
        candidate = db.execute(select(Candidate).where(Candidate.candidateid == candidate_id)).scalar_one_or_none()
        if not candidate:
            raise HTTPException(status_code=404, detail="Candidate not found")

        # Delete related marketing records
        db.execute(f"DELETE FROM candidatemarketing WHERE candidateid = {candidate_id}")
        db.commit()

        # Delete the candidate record
        db.delete(candidate)
        db.commit()

        return {"message": "Candidate deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database delete error: {str(e)}")

# Route to search candidates with pagination
@router.get('/candidates/search', response_model=List[CandidateBase])
def search_candidates(
    search: str = '', 
    page: int = 1, 
    page_size: int = 10, 
    db: Session = Depends(get_db), 
    admin_validation: bool = Depends(admin_validation)
):
    offset = (page - 1) * page_size
    search_query = f"SELECT * FROM candidate WHERE CONCAT_WS(' ', name) LIKE ? LIMIT ? OFFSET ?;"
    count_query = "SELECT COUNT(*) AS totalRows FROM candidate WHERE CONCAT_WS(' ', name) LIKE ?;"

    try:
        # Get total rows matching search query
        db.execute(count_query, [f"%{search}%"])
        total_results = db.fetchall()
        total_rows = total_results[0]['totalRows']

        # Get the candidates based on the search query and pagination
        db.execute(search_query, [f"%{search}%", page_size, offset])
        results = db.fetchall()

        return {"data": results, "totalRows": total_rows}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Search query error: {str(e)}")

