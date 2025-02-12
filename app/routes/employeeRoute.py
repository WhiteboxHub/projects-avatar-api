from fastapi import APIRouter, HTTPException,Query,Depends,Body
from sqlalchemy.orm import Session
from app.models import Employee
from app.schemas import EmployeeCreate, EmployeeUpdate, EmployeeInDB
from logger import logger
from typing import List, Optional
from sqlalchemy import text
from app import schemas, models, database
from app.database.db import get_db
import traceback

logger.error(traceback.format_exc())

router = APIRouter()
# logger=logging.getLogger()


@router.get("/employees", response_model=List[EmployeeInDB])
def get_employees(
    db: Session = Depends(get_db),
    page: int = Query(1, ge=1),
    page_size: int = Query(100, ge=1, le=200),
    search: Optional[str] = Query("")
):
    try:
        offset = (page - 1) * page_size
        search_param = f"%{search}%" if search else "%"

        query = text("""
            SELECT id, name, email, phone, status, startdate, mgrid, designationid, personalemail,
            personalphone, dob, address, city, state, country, zip, skypeid, salary, commission, 
            commissionrate, type, empagreementurl, offerletterurl, dlurl, workpermiturl, contracturl, 
            enddate, loginid, responsibilities, notes 
            FROM employee
            WHERE (:search = '%' OR name LIKE :search OR CAST(id AS CHAR) LIKE :search)
            ORDER BY startdate DESC
            LIMIT :page_size OFFSET :offset
        """)

        result = db.execute(query, {"search": search_param, "page_size": page_size, "offset": offset}).fetchall()

        if not result:
            return []

        employees = [
            EmployeeInDB(
                id=row[0], name=row[1], email=row[2], phone=row[3], status=row[4], startdate=row[5],
                mgrid=row[6], designationid=row[7], personalemail=row[8], personalphone=row[9],
                dob=row[10], address=row[11], city=row[12], state=row[13], country=row[14],
                zip=row[15], skypeid=row[16], salary=row[17], commission=row[18], commissionrate=row[19],
                type=row[20], empagreementurl=row[21], offerletterurl=row[22], dlurl=row[23],
                workpermiturl=row[24], contracturl=row[25], enddate=row[26], loginid=row[27],
                responsibilities=row[28], notes=row[29]
            )
            for row in result
        ]

        return employees

    except Exception as e:
        logger.error(f"Error fetching employees: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

@router.get("/employees/{employee_id}", response_model=EmployeeInDB)
def get_employee_by_id(
    employee_id: int,
    db: Session = Depends(get_db)
):
    try:
        logger.info(f"Fetching employee with id={employee_id}")

        # Query to fetch a single employee by ID
        query = text("""
            SELECT id, name, email, phone, status, startdate, mgrid, designationid, personalemail,
            personalphone, dob, address, city, state, country, zip, skypeid, salary, commission, 
            commissionrate, type, empagreementurl, offerletterurl, dlurl, workpermiturl, contracturl, 
            enddate, loginid, responsibilities, notes 
            FROM employee
            WHERE id = :employee_id
        """)

        result = db.execute(query, {"employee_id": employee_id}).fetchone()

        # If no employee is found, raise a 404 error
        if not result:
            raise HTTPException(status_code=404, detail="Employee not found")

        # Map the result to the EmployeeInDB model
        employee = EmployeeInDB(
            id=result[0], name=result[1], email=result[2], phone=result[3], status=result[4], startdate=result[5],
            mgrid=result[6], designationid=result[7], personalemail=result[8], personalphone=result[9],
            dob=result[10], address=result[11], city=result[12], state=result[13], country=result[14],
            zip=result[15], skypeid=result[16], salary=result[17], commission=result[18], commissionrate=result[19],
            type=result[20], empagreementurl=result[21], offerletterurl=result[22], dlurl=result[23],
            workpermiturl=result[24], contracturl=result[25], enddate=result[26], loginid=result[27],
            responsibilities=result[28], notes=result[29]
        )

        return employee

    except HTTPException as http_err:
        # Re-raise HTTP exceptions (e.g., 404)
        raise http_err
    except Exception as e:
        # Log and handle unexpected errors
        import traceback
        error_details = traceback.format_exc()
        logger.error(f"Error fetching employee with id={employee_id}: {e}\n{error_details}")
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")




@router.post("/employees/insert", response_model=EmployeeInDB)
async def insert_employee(employee: EmployeeCreate = Body(...), db: Session = Depends(get_db)):
    try:
        # Log the incoming payload
        logger.info(f"Received payload: {employee.dict()}")
        
        # Create a new employee
        new_employee = Employee(**employee.dict())
        db.add(new_employee)
        db.commit()
        db.refresh(new_employee)
        return new_employee
    except Exception as e:
        logger.error(f"Error inserting employee: {e}")
        raise HTTPException(status_code=500, detail=str(e))
    
    
@router.put("/employees/update/{employee_id}", response_model=EmployeeInDB)
def update_employee(
    employee_id: int, 
    employee_data: EmployeeUpdate, 
    db: Session = Depends(get_db)
):
    db_employee = db.query(Employee).filter(Employee.id == employee_id).first()

    if not db_employee:
        raise HTTPException(status_code=404, detail=f"Employee with ID {employee_id} not found. Please create it first.")

    for key, value in employee_data.dict(exclude_unset=True).items():
        setattr(db_employee, key, value)

    db.commit()
    db.refresh(db_employee)
    return db_employee

# DELETE endpoint to remove an employee by ID
@router.delete("/employees/{employee_id}", response_model=dict)
async def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    try:
        db_employee = db.query(Employee).filter(Employee.id == employee_id).first()
        
        if not db_employee:
            raise HTTPException(status_code=404, detail="Employee not found")
        
        db.delete(db_employee)
        db.commit()
        return {"message": "Employee deleted successfully"}
    except Exception as e:
        logger.error(f"Error deleting employee {employee_id}: {e}")
        raise HTTPException(status_code=500, detail=str(e))

