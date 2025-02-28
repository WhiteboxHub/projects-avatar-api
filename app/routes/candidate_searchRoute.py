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

