from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.database.db import get_db
from app.controllers.access_controller import update_user, delete_user
from app.middleware.admin_validation import admin_validation
from app.schemas import UserCreate, UserResponse
from app.models import User

router = APIRouter()

@router.get("/users", dependencies=[Depends(admin_validation)])
def get_users(
    db: Session = Depends(get_db),
    page: int = Query(1, alias="page"),
    page_size: int = Query(100, alias="pageSize"),
    search: str = Query(None, alias="search")
):
    offset = (page - 1) * page_size
    
    query = db.query(User)
    
    if search:
        query = query.filter(User.uname.ilike(f"%{search}%") | User.id.ilike(f"%{search}%"))
    
    total_rows = query.count()
    users = query.order_by(User.id.desc()).offset(offset).limit(page_size).all()
    
    return {"data": users, "totalRows": total_rows}

@router.post("/users/search", response_model=UserResponse)
def insert_user(new_user: UserCreate, db: Session = Depends(get_db)):
    user = User(**new_user.dict())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@router.put("/users/update/{id}", dependencies=[Depends(admin_validation)])
def update_user_route(id: int, user_update: UserCreate, db: Session = Depends(get_db)):
    return update_user(id, user_update, db)

@router.delete("/users/delete/{id}", dependencies=[Depends(admin_validation)])
def delete_user_route(id: int, db: Session = Depends(get_db)):
    return delete_user(id, db)

@router.get("/users/search", dependencies=[Depends(admin_validation)])
def search_users(
    db: Session = Depends(get_db),
    search: str = Query(None, alias="search"),
    page: int = Query(1, alias="page"),
    page_size: int = Query(10, alias="pageSize")
):
    offset = (page - 1) * page_size
    
    query = db.query(User)
    if search:
        query = query.filter(User.uname.ilike(f"%{search}%"))
    
    total_rows = query.count()
    users = query.order_by(User.id.desc()).offset(offset).limit(page_size).all()
    
    return {"data": users, "totalRows": total_rows, "page": page, "pageSize": page_size}
