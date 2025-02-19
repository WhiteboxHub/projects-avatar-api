# from sqlalchemy.orm import Session
# from sqlalchemy import or_
# from app.models import PO , Placement, Candidate
# from app.schemas import POListResponse, POCreate, POResponse

# # # ✅ GET all POs with pagination & search
# # def get_po_list(db: Session, page: int, limit: int, search: str = None):
# #     query = db.query(PO)

# #     if search:
# #         query = query.filter(
# #             or_(
# #                 PO.polink.ilike(f"%{search}%"),
# #                 PO.notes.ilike(f"%{search}%")
# #             )
# #         )

# #     total = query.count()
# #     po_list = query.offset((page - 1) * limit).limit(limit).all()

# #     return POListResponse(
# #         total=total,
# #         page=page,
# #         limit=limit,
# #         data=po_list
# #     )

# def get_po_list(db: Session, page: int, limit: int, search: str = None):
#     query = db.query(PO).join(Placement, PO.placementid == Placement.placementid).join(Candidate, Placement.candidateid == Candidate.candidateid)

#     if search:
#         query = query.filter(
#             or_(
#                 PO.polink.ilike(f"%{search}%"),
#                 PO.notes.ilike(f"%{search}%"),
#                 Candidate.name.ilike(f"%{search}%")  # ✅ Allow searching by candidate name
#             )
#         )

#     total = query.count()
#     po_list = query.offset((page - 1) * limit).limit(limit).all()

#     return POListResponse(
#         total=total,
#         page=page,
#         limit=limit,
#         data=po_list  # ✅ Ensure schema supports nested relationships
#     )
    
    

# # ✅ GET a single PO by ID
# def get_po_by_id(db: Session, id: int):
#     return db.query(PO).filter(PO.id == id).first()

# # ✅ CREATE a new PO
# def create_po(db: Session, po_data: POCreate):
#     new_po = PO(**po_data.dict())
#     db.add(new_po)
#     db.commit()
#     db.refresh(new_po)
#     return new_po

# # ✅ UPDATE an existing PO
# def update_po(db: Session, id: int, po_data: POCreate):
#     po = db.query(PO).filter(PO.id == id).first()
#     if not po:
#         return None
    
#     for key, value in po_data.dict().items():
#         setattr(po, key, value)

#     db.commit()
#     db.refresh(po)
#     return po

# # ✅ DELETE a PO
# def delete_po(db: Session, id: int):
#     po = db.query(PO).filter(PO.id == id).first()
#     if not po:
#         return False
    
#     db.delete(po)
#     db.commit()
#     return True



# _______________________________________
# from sqlalchemy.orm import Session
# from sqlalchemy import or_
# from sqlalchemy.sql import text
# from app.models import PO, Placement, Candidate, Vendor, Client
# from app.schemas import POListResponse, POCreate, POResponse

# # ✅ GET a paginated list of POs with search functionality
# def get_po_list(db: Session, page: int, limit: int, search: str = None):
#     offset = (page - 1) * limit

#     query = (
#         db.query(
#             PO.id.label("POID"),
#             Candidate.name.label("CandidateName"),
#             Vendor.companyname.label("VendorName"),
#             Client.companyname.label("ClientName"),
#             PO.begindate.label("StartDate"),
#             PO.enddate.label("EndDate"),
#             PO.rate.label("Rate"),
#             PO.overtimerate.label("OvertimeRate"),
#             PO.freqtype.label("FreqType"),
#             PO.frequency.label("InvoiceFrequency"),
#             PO.invoicestartdate.label("InvoiceStartDate"),
#             PO.invoicenet.label("InvoiceNet"),
#             PO.polink.label("POUrl"),
#             PO.notes.label("Notes"),
#         )
#         .join(Placement, PO.placementid == Placement.id)
#         .join(Candidate, Placement.candidateid == Candidate.id)
#         .join(Vendor, Placement.vendorid == Vendor.id)
#         .join(Client, Placement.clientid == Client.id)
#     )

#     # ✅ Search functionality (matches candidate name, PO link, or notes)
#     if search:
#         query = query.filter(
#             or_(
#                 PO.polink.ilike(f"%{search}%"),
#                 PO.notes.ilike(f"%{search}%"),
#                 Candidate.name.ilike(f"%{search}%")
#             )
#         )

#     # ✅ Fetch total count for pagination
#     total = query.count()

#     # ✅ Fetch paginated results
#     po_list = query.order_by(PO.id.desc()).offset(offset).limit(limit).all()

#     # ✅ Convert results to a list of dicts
#     results = [
#         {
#             "POID": po.POID,
#             "PlacementDetails": f"{po.CandidateName}---{po.VendorName}---{po.ClientName}",
#             "StartDate": po.StartDate,
#             "EndDate": po.EndDate,
#             "Rate": po.Rate,
#             "OvertimeRate": po.OvertimeRate,
#             "FreqType": po.FreqType,
#             "InvoiceFrequency": po.InvoiceFrequency,
#             "InvoiceStartDate": po.InvoiceStartDate,
#             "InvoiceNet": po.InvoiceNet,
#             "POUrl": po.POUrl,
#             "Notes": po.Notes,
#         }
#         for po in po_list
#     ]

#     return POListResponse(
#         total=total,
#         page=page,
#         limit=limit,
#         data=results  # ✅ Returns a list of dictionaries
#     )


# # ✅ GET a single PO by ID
# def get_po_by_id(db: Session, id: int):
#     return db.query(PO).filter(PO.id == id).first()


# # ✅ CREATE a new PO
# def create_po(db: Session, po_data: POCreate):
#     new_po = PO(**po_data.dict())
#     db.add(new_po)
#     db.commit()
#     db.refresh(new_po)
#     return new_po


# # ✅ UPDATE an existing PO
# def update_po(db: Session, id: int, po_data: POCreate):
#     po = db.query(PO).filter(PO.id == id).first()
#     if not po:
#         return None

#     for key, value in po_data.dict().items():
#         setattr(po, key, value)

#     db.commit()
#     db.refresh(po)
#     return po


# # ✅ DELETE a PO
# def delete_po(db: Session, id: int):
#     po = db.query(PO).filter(PO.id == id).first()
#     if not po:
#         return False

#     db.delete(po)
#     db.commit()
#     return True



from sqlalchemy.orm import Session
from sqlalchemy import or_
from app.models import PO
from app.schemas import POListResponse, POCreate, POResponse

# ✅ GET all POs with pagination & search
def get_po_list(db: Session, page: int, limit: int, search: str = None):
    query = db.query(PO)

    if search:
        query = query.filter(
            or_(
                PO.polink.ilike(f"%{search}%"),
                PO.notes.ilike(f"%{search}%")
            )
        )

    total = query.count()
    po_list = query.offset((page - 1) * limit).limit(limit).all()

    return POListResponse(
        total=total,
        page=page,
        limit=limit,
        data=po_list
    )

# ✅ GET a single PO by ID
def get_po_by_id(db: Session, id: int):
    return db.query(PO).filter(PO.id == id).first()

# ✅ CREATE a new PO
def create_po(db: Session, po_data: POCreate):
    new_po = PO(**po_data.dict())
    db.add(new_po)
    db.commit()
    db.refresh(new_po)
    return new_po

# ✅ UPDATE an existing PO
def update_po(db: Session, id: int, po_data: POCreate):
    po = db.query(PO).filter(PO.id == id).first()
    if not po:
        return None
    
    for key, value in po_data.dict().items():
        setattr(po, key, value)

    db.commit()
    db.refresh(po)
    return po

# ✅ DELETE a PO
def delete_po(db: Session, id: int):
    po = db.query(PO).filter(PO.id == id).first()
    if not po:
        return False
    
    db.delete(po)
    db.commit()
    return True