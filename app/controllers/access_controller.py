from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.db import get_db  
from app.models import User, Candidate, Batch  
from datetime import datetime
from typing import List

router = APIRouter()

@router.get("/users", response_model=List[User])
def get_users(db: Session = Depends(get_db)):   
    users = db.query(User).all()
    return users

@router.post("/users", response_model=dict)
def insert_user(user: User, db: Session = Depends(get_db)):
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"id": user.id, **user.__dict__}

@router.put("/users/{user_id}", response_model=dict)
def update_user(user_id: int, updated_user: User, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    for key, value in updated_user.__dict__.items():
        setattr(user, key, value)
    
    db.commit()
    db.refresh(user)
    
    if user.status == 'active':
        batch = db.query(Batch).filter(Batch.current == 'Y', Batch.subject == 'ML').first()
        batchname = batch.batchname if batch else 'default'
        
        candidate_data = {
            "name": user.fullname or 'NA',
            "enrolleddate": user.registereddate.strftime('%Y-%m-%d') if user.registereddate else 'NA',
            "email": user.uname or 'NA',
            "phone": user.phone or 'NA',
            "address": user.address or 'NA',
            "city": user.city or 'NA',
            "zip": user.zip or 'NA',
            "state": user.state or 'NA',
            "country": user.country or 'NA',
            "status": user.status or 'NA',
            "course": 'ML',
            "agreement": 'N',
            "promissory": 'N',
            "driverslicense": 'N',
            "workpermit": 'N',
            "batchname": batchname,
            "processflag": 'N',
            "defaultprocessflag": 'N'
        }
        
        candidate = Candidate(**candidate_data)
        db.add(candidate)
        db.commit()
        db.refresh(candidate)
        
        return {"message": "User updated and inserted into candidate table", "userId": user_id, "candidateId": candidate.id}
    
    return {"id": user_id, **updated_user.__dict__}

@router.delete("/users/{user_id}", response_model=dict)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}
