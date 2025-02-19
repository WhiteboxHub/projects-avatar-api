# from fastapi import APIRouter, Depends, Query, HTTPException
# from sqlalchemy.orm import Session
# from app.database.db import get_db
# from app.controllers.po_controller import (
#     get_po_list, get_po_by_id, create_po, update_po, delete_po
# )
# from app.schemas import POCreate, POResponse, POListResponse

# router = APIRouter()

# # # ✅ GET all POs (with pagination & search)
# # @router.get("/", response_model=POListResponse)
# # def get_po(
# #     page: int = Query(1, alias="page", description="Page number"),
# #     limit: int = Query(10, alias="limit", description="Number of items per page"),
# #     search: str = Query(None, alias="search", description="Search term"),
# #     db: Session = Depends(get_db)
# # ):
# #     return get_po_list(db, page, limit, search)


# @router.get("/", response_model=POListResponse)
# def get_po(
#     page: int = Query(1, alias="page", description="Page number"),
#     limit: int = Query(10, alias="limit", description="Number of items per page"),
#     search: str = Query(None, alias="search", description="Search term"),
#     db: Session = Depends(get_db)
# ):
#     return get_po_list(db, page, limit, search)

# # ✅ GET a single PO by ID
# @router.get("/{id}", response_model=POResponse)
# def get_po_by_id_route(id: int, db: Session = Depends(get_db)):
#     po = get_po_by_id(db, id)
#     if not po:
#         raise HTTPException(status_code=404, detail="PO not found")
#     return po

# # ✅ POST (Create a new PO)
# @router.post("/", response_model=POResponse)
# def create_po_route(po_data: POCreate, db: Session = Depends(get_db)):
#     return create_po(db, po_data)



# # ✅ PUT (Update an existing PO)
# @router.put("/{id}", response_model=POResponse)
# def update_po_route(id: int, po_data: POCreate, db: Session = Depends(get_db)):
#     updated_po = update_po(db, id, po_data)
#     if not updated_po:
#         raise HTTPException(status_code=404, detail="PO not found")
#     return updated_po

# # ✅ DELETE (Remove a PO by ID)
# @router.delete("/{id}")
# def delete_po_route(id: int, db: Session = Depends(get_db)):
#     success = delete_po(db, id)
#     if not success:
#         raise HTTPException(status_code=404, detail="PO not found")
#     return {"message": "PO deleted successfully"}





from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from app.database.db import get_db
from app.controllers.po_controller import (
    get_po_list, get_po_by_id, create_po, update_po, delete_po
)
from app.schemas import POCreate, POResponse, POListResponse

router = APIRouter()

# ✅ GET all POs (with pagination & search)
@router.get("/", response_model=POListResponse)
def get_po(
    page: int = Query(1, alias="page", description="Page number"),
    limit: int = Query(10, alias="limit", description="Number of items per page"),
    search: str = Query(None, alias="search", description="Search term"),
    db: Session = Depends(get_db)
):
    return get_po_list(db, page, limit, search)

# ✅ GET a single PO by ID
@router.get("/{id}", response_model=POResponse)
def get_po_by_id_route(id: int, db: Session = Depends(get_db)):
    po = get_po_by_id(db, id)
    if not po:
        raise HTTPException(status_code=404, detail="PO not found")
    return po

# ✅ POST (Create a new PO)
@router.post("/", response_model=POResponse)
def create_po_route(po_data: POCreate, db: Session = Depends(get_db)):
    return create_po(db, po_data)

# ✅ PUT (Update an existing PO)
@router.put("/{id}", response_model=POResponse)
def update_po_route(id: int, po_data: POCreate, db: Session = Depends(get_db)):
    updated_po = update_po(db, id, po_data)
    if not updated_po:
        raise HTTPException(status_code=404, detail="PO not found")
    return updated_po

# ✅ DELETE (Remove a PO by ID)
@router.delete("/{id}")
def delete_po_route(id: int, db: Session = Depends(get_db)):
    success = delete_po(db, id)
    if not success:
        raise HTTPException(status_code=404, detail="PO not found")
    return {"message": "PO deleted successfully"}
