# from sqlalchemy.orm import Session
# from app import models

# def search_candidates(db: Session, search: str, page_size: int, offset: int):
#     query = db.query(models.CandidateSearch)
    
#     # Apply search filter if search term is provided
#     if search:
#         query = query.filter(models.CandidateSearch.name.ilike(f"%{search}%"))
    
#     total_rows = query.count()  # Get total number of rows for pagination
#     candidates = query.offset(offset).limit(page_size).all()
    
#     return {"data": candidates, "totalRows": total_rows}

from sqlalchemy.orm import Session
from app.models import CandidateSearch
from app.schemas import CandidateSearchBase

def search_candidates_by_name(db: Session, search_params: CandidateSearchBase):
    if not search_params.name:
        return []  # If no name is provided, return an empty list.
    
    candidates = db.query(CandidateSearch).filter(CandidateSearch.name.ilike(f"%{search_params.name}%")).all()
    
    return candidates