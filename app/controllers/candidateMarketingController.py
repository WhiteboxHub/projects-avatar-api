# from sqlalchemy.orm import Session
# from sqlalchemy.sql import text
# from app.models import Candidate, CandidateMarketing
# from app.schemas import CandidateMarketingUpdateSchema 


# def get_candidate_marketing_list(db: Session, skip: int, limit: int):
#     query = text("""
#         SELECT
#             cm.id,
#             cm.startdate,
#             c.name,
#             c.email,
#             c.phone,
#             cm.candidateid,
#             e.name AS instructor,
#             cm.mmid,
#             cm.instructorid,
#             cm.submitterid,
#             c.secondaryemail,
#             c.secondaryphone,
#             c.workstatus,
#             cm.status,
#             cm.locationpreference,
#             cm.priority,
#             cm.technology,
#             cm.resumeid,
#             cm.minrate,
#             cm.ipemailid,
#             cm.currentlocation,
#             cm.relocation,
#             cm.skypeid,
#             (SELECT link FROM resume WHERE id = cm.resumeid) AS resumelink,
#             (SELECT phone FROM ipemail WHERE id = cm.ipemailid) AS ipphone,
#             cm.closedate,
#             cm.suspensionreason,
#             cm.intro,
#             cm.notes
#         FROM
#             candidatemarketing cm
#         JOIN
#             candidate c ON cm.candidateid = c.candidateid
#         JOIN
#             employee e ON cm.instructorid = e.id
#         order by cm.id desc
#         LIMIT
#             :limit OFFSET :skip
#     """)

#     result = db.execute(query, {"limit": limit, "skip": skip}).mappings().all()
#     return result

# def get_candidate_marketing_by_id(db: Session, candidate_marketing_id: int):
#     query = text("""
#         SELECT
#             cm.id,
#             cm.candidateid,
#             cm.startdate,
#             cm.mmid,
#             cm.instructorid,
#             cm.status,
#             cm.submitterid,
#             cm.priority,
#             cm.technology,
#             cm.minrate,
#             cm.currentlocation,
#             cm.relocation,
#             cm.locationpreference,
#             cm.skypeid,
#             cm.ipemailid,
#             cm.resumeid,
#             cm.coverletter,
#             cm.intro,
#             cm.closedate,
#             cm.closedemail,
#             cm.notes,
#             cm.suspensionreason,
#             cm.yearsofexperience
#         FROM candidatemarketing cm
#         WHERE cm.id = :candidate_marketing_id
#     """)

#     result = db.execute(query, {"candidate_marketing_id": candidate_marketing_id}).mappings().first()
#     return result


# def update_candidate_marketing(db: Session, candidate_marketing_id: int, candidate_marketing_data: CandidateMarketingUpdateSchema):

#     candidate_id = candidate_marketing_data.candidateid
#     if candidate_id is not None:
#         candidate_exists = db.query(Candidate).filter(Candidate.candidateid == candidate_id).first()
#         if not candidate_exists:
#             return {"error": f"Candidate with ID {candidate_id} does not exist."}

#     existing_candidate_marketing = db.query(CandidateMarketing).filter(CandidateMarketing.id == candidate_marketing_id).first()
#     if not existing_candidate_marketing:
#         return {"error": "Candidate Marketing not found"}

    
#     fields_to_update = [
#         "candidateid", "startdate", "mmid", "instructorid", "status",
#         "submitterid", "priority", "technology", "minrate", "currentlocation",
#         "relocation", "locationpreference", "skypeid", "ipemailid", "resumeid",
#         "coverletter", "intro", "closedate", "closedemail", "notes",
#         "suspensionreason", "yearsofexperience"
#     ]

#     for key in fields_to_update:
#         if key in candidate_marketing_data.dict(exclude_unset=True):
#             value = candidate_marketing_data.dict(exclude_unset=True)[key]
#             if key == 'relocation' and value is not None:
#                 value = value[:200]  
#             if key == 'yearsofexperience' and value is not None:
#                 value = value[:3]  
#             setattr(existing_candidate_marketing, key, value)

#     db.commit()
#     db.refresh(existing_candidate_marketing)
#     return {"message": "Candidate Marketing updated successfully"}

# def delete_candidate_marketing(db: Session, candidate_marketing_id: int):
#     candidate_marketing = db.query(CandidateMarketing).filter(CandidateMarketing.id == candidate_marketing_id).first()
#     if not candidate_marketing:
#         return {"error": "Candidate Marketing not found"}

#     db.delete(candidate_marketing)
#     db.commit()
#     return {"message": "Candidate Marketing deleted successfully"}

from sqlalchemy.orm import Session
from app.models import Candidate, CandidateMarketing
from app.schemas import CandidateMarketingUpdateSchema

def get_candidate_marketing_list(db: Session, skip: int, limit: int):
    """
    Retrieve a paginated list of candidate marketing records.
    """
    return (
        db.query(CandidateMarketing)
        .order_by(CandidateMarketing.id.desc())
        .offset(skip)
        .limit(limit)
        .all()
    )

def get_candidate_marketing_by_id(db: Session, candidate_marketing_id: int):
    """
    Retrieve a single candidate marketing record by ID.
    """
    return db.query(CandidateMarketing).filter(CandidateMarketing.id == candidate_marketing_id).first()

def update_candidate_marketing(db: Session, candidate_marketing_id: int, candidate_marketing_data: CandidateMarketingUpdateSchema):
    """
    Update an existing candidate marketing record.
    """
    candidate_id = candidate_marketing_data.candidateid
    if candidate_id is not None:
        candidate_exists = db.query(Candidate).filter(Candidate.candidateid == candidate_id).first()
        if not candidate_exists:
            return {"error": f"Candidate with ID {candidate_id} does not exist."}

    existing_candidate_marketing = db.query(CandidateMarketing).filter(CandidateMarketing.id == candidate_marketing_id).first()
    if not existing_candidate_marketing:
        return {"error": "Candidate Marketing not found"}

    # Update only the provided fields
    update_data = candidate_marketing_data.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        if key == 'relocation' and value is not None:
            value = value[:200]  # Truncate if necessary
        if key == 'yearsofexperience' and value is not None:
            value = value[:3]  # Truncate if necessary
        setattr(existing_candidate_marketing, key, value)

    db.commit()
    db.refresh(existing_candidate_marketing)
    return {"message": "Candidate Marketing updated successfully", "candidate_marketing": existing_candidate_marketing}

def delete_candidate_marketing(db: Session, candidate_marketing_id: int):
    """
    Delete a candidate marketing record by ID.
    """
    candidate_marketing = db.query(CandidateMarketing).filter(CandidateMarketing.id == candidate_marketing_id).first()
    if not candidate_marketing:
        return {"error": "Candidate Marketing not found"}

    db.delete(candidate_marketing)
    db.commit()
    return {"message": "Candidate Marketing deleted successfully"}