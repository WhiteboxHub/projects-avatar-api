# from fastapi import APIRouter, Depends, Query
# from sqlalchemy.orm import Session
# from app.controllers.candidate_search_controller import search_candidates
# from app.models import Candidate
# from app.schemas import CandidateInDB
# from app.database.db import get_db

# candidateSearch_router = APIRouter()

# @candidateSearch_router.get("/candidateSearch", response_model=dict)
# async def search_candidates_route(
#     page: int = Query(1, description="Page number"),
#     page_size: int = Query(10, description="Number of candidates per page"),
#     search: str = Query(None, description="Search term"),  # Allow None instead of empty string
#     db: Session = Depends(get_db),
# ):
#     """
#     Search candidates by name with pagination.
#     """
#     offset = (page - 1) * page_size
    
#     # Call controller to search candidates
#     result = search_candidates(db, search, page_size, offset)

#     return result




from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.db import get_db
from app.schemas import CandidateSearchBase
from app.controllers.candidate_search_controller import search_candidates_by_name

router = APIRouter()

@router.post("/search")
def search_candidates_route(search_params: CandidateSearchBase, db: Session = Depends(get_db)):
    results = search_candidates_by_name(db=db, search_params=search_params)
    return results