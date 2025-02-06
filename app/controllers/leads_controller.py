from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models, schemas
from db import SessionLocal

router = APIRouter()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/leads", response_model=List[schemas.LeadResponse])
def get_leads(db: Session = Depends(get_db)):
    return db.query(models.Lead).all()

@router.post("/leads/insert", response_model=schemas.LeadResponse, status_code=201)
def insert_lead(lead: schemas.LeadCreate, db: Session = Depends(get_db)):
    new_lead = models.Lead(**lead.dict())
    db.add(new_lead)
    db.commit()
    db.refresh(new_lead)
    return new_lead

@router.put("/leads/{id}", response_model=schemas.LeadResponse)
def update_lead(id: int, lead: schemas.LeadUpdate, db: Session = Depends(get_db)):
    db_lead = db.query(models.Lead).filter(models.Lead.leadid == id).first()
    if not db_lead:
        raise HTTPException(status_code=404, detail="Lead not found")

    for key, value in lead.dict(exclude_unset=True).items():
        setattr(db_lead, key, value)

    db.commit()
    db.refresh(db_lead)
    return db_lead

@router.delete("/leads/{id}")
def delete_lead(id: int, db: Session = Depends(get_db)):
    db_lead = db.query(models.Lead).filter(models.Lead.leadid == id).first()
    if not db_lead:
        raise HTTPException(status_code=404, detail="Lead not found")

    db.delete(db_lead)
    db.commit()
    return {"message": "Lead deleted successfully"}
