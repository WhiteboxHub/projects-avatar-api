# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# from typing import List
# from app.models import Lead  # Import the Lead model from models.py
# from app.schemas import LeadCreate, LeadInDB, LeadUpdate  # Import schemas from schemas.py
# from app.database.db import get_db
# # import crud  # Optionally, create a separate CRUD file to handle operations

# router = APIRouter()

# @router.get("/leads")
# async def get_leads(page: int = 1, page_size: int = 100, search: str = "", db: Session = Depends(get_db)):
#     # Implement the logic to retrieve leads with pagination and search
#     # return crud.get_leads(db, page, page_size, search)
#     return 'this is working'

# @router.post("/leads/insert")
# async def create_lead(lead: LeadCreate, db: Session = Depends(get_db)):
#     # Insert a new lead
#     return crud.create_lead(db, lead)

# @router.put("/leads/update/{id}")
# async def update_lead(id: int, lead: LeadUpdate, db: Session = Depends(get_db)):
#     # Update an existing lead
#     return crud.update_lead(db, id, lead)

# @router.delete("/leads/delete/{id}")
# async def delete_lead(id: int, db: Session = Depends(get_db)):
#     # Delete a lead
#     return crud.delete_lead(db, id)


from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.models import Lead  # Import the Lead model from models.py
from app.schemas import LeadCreate, LeadInDB, LeadUpdate  # Import schemas from schemas.py
from app.database.db import get_db

router = APIRouter()

@router.get("/leads", response_model=List[LeadInDB])
async def get_leads(page: int = 1, page_size: int = 100, search: str = "", db: Session = Depends(get_db)):
    # Implement the logic to retrieve leads with pagination and search
    skip = (page - 1) * page_size
    query = db.query(Lead)
    if search:
        query = query.filter(Lead.name.contains(search) | Lead.email.contains(search))
    leads = query.offset(skip).limit(page_size).all()
    return leads

@router.post("/leads/insert", response_model=LeadCreate)
async def create_lead(lead: LeadCreate, db: Session = Depends(get_db)):
    # Insert a new lead
    db_lead = Lead(**lead.dict())
    db.add(db_lead)
    db.commit()
    db.refresh(db_lead)
    return db_lead

@router.put("/leads/update/{id}", response_model=LeadUpdate)
async def update_lead(id: int, lead: LeadUpdate, db: Session = Depends(get_db)):
    # Update an existing lead
    db_lead = db.query(Lead).filter(Lead.leadid  == id).first()
    if not db_lead:
        raise HTTPException(status_code=404, detail="Lead not found")
    for key, value in lead.dict().items():
        setattr(db_lead, key, value)
    db.commit()
    db.refresh(db_lead)
    return db_lead

@router.delete("/leads/delete/{id}", response_model=LeadInDB)
async def delete_lead(id: int, db: Session = Depends(get_db)):
    # Delete a lead
    db_lead = db.query(Lead).filter(Lead.leadid == id).first()
    if not db_lead:
        raise HTTPException(status_code=404, detail="Lead not found")
    db.delete(db_lead)
    db.commit()
    return db_lead 