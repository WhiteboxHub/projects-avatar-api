from fastapi import APIRouter, HTTPException, Depends, Query
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from models import Employee
from schemas import EmployeeCreate, EmployeeInDB 
from schemas import EmployeeInDB  #  Import schemas properly
from fastapi.logger import logger
from . import models, schemas, database
from datetime import datetime
from employeeController import router as employee_router  # Import employeeController routes
from typing import List, Optional
# router = APIRouter()
# router.include_router(employee_router, prefix="/employees", tags=["Employees"])

# #Function to Fix Invalid MySQL Dates (`0000-00-00`)
# def safe_date(date_value):
#     """ Convert MySQL invalid date '0000-00-00' into None. """
#     if not date_value or str(date_value).startswith("0000"):
#         return None  # Convert invalid dates to None
#     if isinstance(date_value, str):  # If it's a string, try converting
#         try:
#             return datetime.strptime(date_value, "%Y-%m-%d").date()
#         except ValueError:
#             return None  # Handle any other invalid formats
#     return date_value  # If already a valid date, return as is



# # #  Fetch All Employees (GET)
# # @router.get("/employees", response_model=List[EmployeeInDB])
# # def get_employees(
# #     page: int = Query(1, ge=1),
# #     page_size: int = Query(100, ge=1, le=1000),
# #     db: Session = Depends(get_db)
# # ):
# #     try:
# #         offset = (page - 1) * page_size  # Pagination logic
        
# #         employees = db.query(Employee).order_by(Employee.startdate.desc()).offset(offset).limit(page_size).all()
        
# #         if not employees:
# #             return []  # Return empty list if no employees found

# #         return employees
# #     except Exception as e:
# #         logger.error(f"Error fetching employees: {str(e)}")
# #         raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")



# @router.get("/employees", response_model=List[EmployeeInDB])
# def get_employees(
#     page: int = Query(1, ge=1, description="Page number (starting from 1)"),
#     page_size: int = Query(100, ge=1, le=1000, description="Number of items per page"),
#     search: Optional[str] = Query(None, description="Search term for filtering employees"),
#     db: Session = Depends(get_db)
# ):
#     try:
#         # Calculate offset for pagination
#         offset = (page - 1) * page_size

#         # Build base query
#         query = db.query(Employee).order_by(Employee.startdate.desc())

#         # Apply search filter if search term is provided
#         if search:
#             query = query.filter(
#                 (Employee.name.ilike(f"%{search}%")) |  # Case-insensitive search for name
#                 (Employee.email.ilike(f"%{search}%"))   # Case-insensitive search for email
#             )

#         # Apply pagination
#         employees = query.offset(offset).limit(page_size).all()

#         # Handle empty result
#         if not employees:
#             return []

#         return employees

#     except Exception as e:
#         logger.error(f"Error fetching employees: {str(e)}")
#         raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

# from fastapi import APIRouter, HTTPException, Depends
# from sqlalchemy.orm import Session
# from database import get_db
# from models import Employee
# from schemas import EmployeeInDB
# import logging

# router = APIRouter()
# logger = logging.getLogger(__name__)

# @router.get("/employees/{employee_id}", response_model=EmployeeInDB)
# def get_employee(employee_id: int, db: Session = Depends(get_db)):
#     try:
#         employee = db.query(Employee).filter(Employee.id == employee_id).first()
        
#         if not employee:
#             raise HTTPException(status_code=404, detail="Employee not found")

#         #  Ensure numeric values (fixing 'N' issue)
#         def safe_float(value):
#             try:
#                 return float(value)
#             except (ValueError, TypeError):
#                 return 0.0  # Replace invalid values with 0.0

#         employee.salary = safe_float(employee.salary)
#         employee.commission = safe_float(employee.commission)
#         employee.commissionrate = safe_float(employee.commissionrate)

#         return employee  #  Return the employee data safely
#     except Exception as e:
#         logger.error(f"Error fetching employee with ID {employee_id}: {e}")
#         raise HTTPException(status_code=500, detail="Internal Server Error")






# # @router.post("/employees/insert", response_model=schemas.EmployeeInDB)
# # def create_employee(employee: schemas.EmployeeCreate, db: Session = Depends(database.get_db)):
# #     try:
# #         db_employee = models.Employee(**employee.dict())
# #         db.add(db_employee)
# #         db.commit()
# #         db.refresh(db_employee)
# #         return db_employee
# #     except Exception as e:
# #         logger.error(f"Error creating employee: {e}")
# #         raise HTTPException(status_code=500, detail="Internal Server Error")




# @router.post("/employees/insert", response_model=EmployeeInDB)
# def create_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
#     try:
#         db_employee = Employee(**employee.dict())
#         db.add(db_employee)
#         db.commit()
#         db.refresh(db_employee)
#         return db_employee
#     except Exception as e:
#         logger.error(f"Error creating employee: {e}")
#         raise HTTPException(status_code=500, detail="Internal Server Error")


# @router.put("/employees/update/{employee_id}", response_model=schemas.EmployeeInDB)
# def update_employee(employee_id: int, employee: schemas.EmployeeUpdate, db: Session = Depends(database.get_db)):
#     try:
#         db_employee = db.query(models.Employee).filter(models.Employee.id == employee_id).first()
#         if db_employee is None:
#             raise HTTPException(status_code=404, detail="Employee not found")
        
#         for key, value in employee.dict(exclude_unset=True).items():
#             setattr(db_employee, key, value)
        
#         db.commit()
#         db.refresh(db_employee)
#         return db_employee
#     except Exception as e:
#         logger.error(f"Error updating employee with ID {employee_id}: {e}")
#         raise HTTPException(status_code=500, detail="Internal Server Error")

# @router.delete("/employees/{employee_id}")
# def delete_employee(employee_id: int, db: Session = Depends(database.get_db)):
#     try:
#         db_employee = db.query(models.Employee).filter(models.Employee.id == employee_id).first()
#         if db_employee is None:
#             raise HTTPException(status_code=404, detail="Employee not found")
        
#         db.delete(db_employee)
#         db.commit()
#         return {"message": "Employee deleted successfully"}
#     except Exception as e:
#         logger.error(f"Error deleting employee with ID {employee_id}: {e}")
#         raise HTTPException(status_code=500, detail="Internal Server Error")
    





from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from app.models import Employee
from app.schemas import EmployeeCreate, EmployeeUpdate, EmployeeInDB
from logger import logger
from typing import List, Optional
from sqlalchemy import text
from app.database.db import get_db
import traceback

# Function to get a list of employees with pagination and search
def get_employees(
    db: Session,
    page: int = 1,
    page_size: int = 100,
    search: Optional[str] = ""
) -> List[EmployeeInDB]:
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


# Function to get an employee by ID
def get_employee_by_id(
    employee_id: int,
    db: Session
) -> EmployeeInDB:
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
        error_details = traceback.format_exc()
        logger.error(f"Error fetching employee with id={employee_id}: {e}\n{error_details}")
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")


# Function to insert a new employee
def create_employee(
    employee: EmployeeCreate,
    db: Session
) -> EmployeeInDB:
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


# Function to update an existing employee
def update_employee(
    employee_id: int,
    employee_data: EmployeeUpdate,
    db: Session
) -> EmployeeInDB:
    db_employee = db.query(Employee).filter(Employee.id == employee_id).first()

    if not db_employee:
        raise HTTPException(status_code=404, detail=f"Employee with ID {employee_id} not found. Please create it first.")

    for key, value in employee_data.dict(exclude_unset=True).items():
        setattr(db_employee, key, value)

    db.commit()
    db.refresh(db_employee)
    return db_employee


# Function to delete an employee
def delete_employee(
    employee_id: int,
    db: Session
) -> dict:
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