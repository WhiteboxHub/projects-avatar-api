from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from app.models import Overdue
from app.schemas import  OverdueUpdateSchema

def get_overdue_list(db: Session, skip: int, limit: int):
    query = text("""
        SELECT
            i.id AS pkid,
            (SELECT concat(c.name, ' - ', v.companyname, ' - ', cl.companyname)
             FROM candidate c
             JOIN placement p ON c.candidateid = p.candidateid
             JOIN po o ON o.placementid = p.id
             JOIN vendor v ON p.vendorid = v.id
             JOIN client cl ON p.clientid = cl.id
             WHERE o.id = i.poid) AS poid,
            i.invoicenumber,
            i.invoicedate,
            i.quantity,
            p.rate,
            DATE_ADD(i.invoicedate, INTERVAL p.invoicenet DAY) AS expecteddate,
            ((i.quantity * p.rate) + (i.otquantity * p.overtimerate)) AS amountexpected,
            i.startdate,
            i.enddate,
            i.status,
            i.remindertype,
            i.amountreceived,
            i.receiveddate,
            i.releaseddate,
            i.checknumber,
            i.invoiceurl,
            i.checkurl,
            v.companyname,
            v.fax AS vendorfax,
            v.phone AS vendorphone,
            v.email AS vendoremail,
            v.timsheetemail,
            v.hrname,
            v.hremail,
            v.hrphone,
            v.managername,
            v.manageremail,
            v.managerphone,
            v.secondaryname,
            v.secondaryemail,
            v.secondaryphone,
            c.name AS candidatename,
            c.phone AS candidatephone,
            c.email AS candidateemail,
            pl.wrkemail,
            pl.wrkphone,
            r.name AS recruitername,
            r.phone AS recruiterphone,
            r.email AS recruiteremail,
            i.notes
        FROM
            invoice i
        JOIN
            po p ON i.poid = p.id
        JOIN
            placement pl ON p.placementid = pl.id
        JOIN
            candidate c ON pl.candidateid = c.candidateid
        JOIN
            vendor v ON pl.vendorid = v.id
        JOIN
            recruiter r ON pl.recruiterid = r.id
        WHERE
            i.status NOT IN ('Void', 'Closed') AND
            DATE_ADD(i.invoicedate, INTERVAL p.invoicenet DAY) <= CURDATE()
        ORDER BY
            pkid DESC
        LIMIT :limit OFFSET :skip
    """)

    result = db.execute(query, {"limit": limit, "skip": skip}).mappings().all()
    return result

def get_overdue_by_id(db: Session, overdue_id: int):
    query = text("""
        SELECT
            i.id AS pkid,
            (SELECT concat(c.name, ' - ', v.companyname, ' - ', cl.companyname)
             FROM candidate c
             JOIN placement p ON c.candidateid = p.candidateid
             JOIN po o ON o.placementid = p.id
             JOIN vendor v ON p.vendorid = v.id
             JOIN client cl ON p.clientid = cl.id
             WHERE o.id = i.poid) AS poid,
            i.invoicenumber,
            i.invoicedate,
            i.quantity,
            p.rate,
            DATE_ADD(i.invoicedate, INTERVAL p.invoicenet DAY) AS expecteddate,
            ((i.quantity * p.rate) + (i.otquantity * p.overtimerate)) AS amountexpected,
            i.startdate,
            i.enddate,
            i.status,
            i.remindertype,
            i.amountreceived,
            i.receiveddate,
            i.releaseddate,
            i.checknumber,
            i.invoiceurl,
            i.checkurl,
            v.companyname,
            v.fax AS vendorfax,
            v.phone AS vendorphone,
            v.email AS vendoremail,
            v.timsheetemail,
            v.hrname,
            v.hremail,
            v.hrphone,
            v.managername,
            v.manageremail,
            v.managerphone,
            v.secondaryname,
            v.secondaryemail,
            v.secondaryphone,
            c.name AS candidatename,
            c.phone AS candidatephone,
            c.email AS candidateemail,
            pl.wrkemail,
            pl.wrkphone,
            r.name AS recruitername,
            r.phone AS recruiterphone,
            r.email AS recruiteremail,
            i.notes
        FROM
            invoice i
        JOIN
            po p ON i.poid = p.id
        JOIN
            placement pl ON p.placementid = pl.id
        JOIN
            candidate c ON pl.candidateid = c.candidateid
        JOIN
            vendor v ON pl.vendorid = v.id
        JOIN
            recruiter r ON pl.recruiterid = r.id
        WHERE
            i.id = :overdue_id
    """)

    result = db.execute(query, {"overdue_id": overdue_id}).mappings().first()
    return result

def update_overdue(db: Session, overdue_id: int, overdue_data: OverdueUpdateSchema):
    query = text("""
        UPDATE invoice
        SET
            invoicenumber = :invoicenumber,
            invoicedate = :invoicedate,
            quantity = :quantity,
            amountreceived = :amountreceived,
            receiveddate = :receiveddate,
            releaseddate = :releaseddate,
            checknumber = :checknumber,
            invoiceurl = :invoiceurl,
            checkurl = :checkurl,
            notes = :notes,
            status = :status,
            remindertype = :remindertype
        WHERE id = :overdue_id
    """)

    params = {
        "invoicenumber": overdue_data.invoicenumber,
        "invoicedate": overdue_data.invoicedate,
        "quantity": overdue_data.quantity,
        "amountreceived": overdue_data.amountreceived,
        "receiveddate": overdue_data.receiveddate,
        "releaseddate": overdue_data.releaseddate,
        "checknumber": overdue_data.checknumber,
        "invoiceurl": overdue_data.invoiceurl,
        "checkurl": overdue_data.checkurl,
        "notes": overdue_data.notes,
        "status": overdue_data.status,
        "remindertype": overdue_data.remindertype,
        "overdue_id": overdue_id
    }

    result = db.execute(query, params)
    db.commit()

    if result.rowcount == 0:
        return {"error": "Overdue not found"}

    return {"message": "Overdue updated successfully"}


# from sqlalchemy.orm import Session, aliased
# from sqlalchemy import func, and_, select
# from app.models import Invoice, Placement, Candidate, Vendor, Client, Recruiter
# from app.schemas import OverdueUpdateSchema

# def get_overdue_list(db: Session, skip: int, limit: int):
#     CandidateAlias = aliased(Candidate)
#     VendorAlias = aliased(Vendor)
#     ClientAlias = aliased(Client)

#     query = (
#         db.query(
#             Invoice.id.label('pkid'),
#             func.concat(CandidateAlias.name, ' - ', VendorAlias.companyname, ' - ', ClientAlias.companyname).label('poid'),
#             Invoice.invoicenumber,
#             Invoice.invoicedate,
#             Invoice.quantity,
#             Placement.rate,
#             func.DATE_ADD(Invoice.invoicedate, func.concat(Placement.invoicenet, ' DAY')).label('expecteddate'),
#             ((Invoice.quantity * Placement.rate) + (Invoice.otquantity * Placement.overtimerate)).label('amountexpected'),
#             Invoice.startdate,
#             Invoice.enddate,
#             Invoice.status,
#             Invoice.remindertype,
#             Invoice.amountreceived,
#             Invoice.receiveddate,
#             Invoice.releaseddate,
#             Invoice.checknumber,
#             Invoice.invoiceurl,
#             Invoice.checkurl,
#             VendorAlias.companyname,
#             VendorAlias.fax.label('vendorfax'),
#             VendorAlias.phone.label('vendorphone'),
#             VendorAlias.email.label('vendoremail'),
#             VendorAlias.timsheetemail,
#             VendorAlias.hrname,
#             VendorAlias.hremail,
#             VendorAlias.hrphone,
#             VendorAlias.managername,
#             VendorAlias.manageremail,
#             VendorAlias.managerphone,
#             VendorAlias.secondaryname,
#             VendorAlias.secondaryemail,
#             VendorAlias.secondaryphone,
#             CandidateAlias.name.label('candidatename'),
#             CandidateAlias.phone.label('candidatephone'),
#             CandidateAlias.email.label('candidateemail'),
#             Placement.wrkemail,
#             Placement.wrkphone,
#             Recruiter.name.label('recruitername'),
#             Recruiter.phone.label('recruiterphone'),
#             Recruiter.email.label('recruiteremail'),
#             Invoice.notes
#         )
#         .join(Placement, Invoice.poid == Placement.id)
#         .join(CandidateAlias, Placement.candidateid == CandidateAlias.candidateid)
#         .join(VendorAlias, Placement.vendorid == VendorAlias.id)
#         .join(ClientAlias, Placement.clientid == ClientAlias.id)
#         .join(Recruiter, Placement.recruiterid == Recruiter.id)
#         .filter(
#             and_(
#                 Invoice.status.not_in(['Void', 'Closed']),
#                 func.DATE_ADD(Invoice.invoicedate, func.concat(Placement.invoicenet, ' DAY')) <= func.CURDATE()
#             )
#         )
#         .order_by(Invoice.id.desc())
#         .offset(skip)
#         .limit(limit)
#     )

#     result = query.all()
#     return result

# def get_overdue_by_id(db: Session, overdue_id: int):
#     CandidateAlias = aliased(Candidate)
#     VendorAlias = aliased(Vendor)
#     ClientAlias = aliased(Client)

#     query = (
#         db.query(
#             Invoice.id.label('pkid'),
#             func.concat(CandidateAlias.name, ' - ', VendorAlias.companyname, ' - ', ClientAlias.companyname).label('poid'),
#             Invoice.invoicenumber,
#             Invoice.invoicedate,
#             Invoice.quantity,
#             Placement.rate,
#             func.DATE_ADD(Invoice.invoicedate, func.concat(Placement.invoicenet, ' DAY')).label('expecteddate'),
#             ((Invoice.quantity * Placement.rate) + (Invoice.otquantity * Placement.overtimerate)).label('amountexpected'),
#             Invoice.startdate,
#             Invoice.enddate,
#             Invoice.status,
#             Invoice.remindertype,
#             Invoice.amountreceived,
#             Invoice.receiveddate,
#             Invoice.releaseddate,
#             Invoice.checknumber,
#             Invoice.invoiceurl,
#             Invoice.checkurl,
#             VendorAlias.companyname,
#             VendorAlias.fax.label('vendorfax'),
#             VendorAlias.phone.label('vendorphone'),
#             VendorAlias.email.label('vendoremail'),
#             VendorAlias.timsheetemail,
#             VendorAlias.hrname,
#             VendorAlias.hremail,
#             VendorAlias.hrphone,
#             VendorAlias.managername,
#             VendorAlias.manageremail,
#             VendorAlias.managerphone,
#             VendorAlias.secondaryname,
#             VendorAlias.secondaryemail,
#             VendorAlias.secondaryphone,
#             CandidateAlias.name.label('candidatename'),
#             CandidateAlias.phone.label('candidatephone'),
#             CandidateAlias.email.label('candidateemail'),
#             Placement.wrkemail,
#             Placement.wrkphone,
#             Recruiter.name.label('recruitername'),
#             Recruiter.phone.label('recruiterphone'),
#             Recruiter.email.label('recruiteremail'),
#             Invoice.notes
#         )
#         .join(Placement, Invoice.poid == Placement.id)
#         .join(CandidateAlias, Placement.candidateid == CandidateAlias.candidateid)
#         .join(VendorAlias, Placement.vendorid == VendorAlias.id)
#         .join(ClientAlias, Placement.clientid == ClientAlias.id)
#         .join(Recruiter, Placement.recruiterid == Recruiter.id)
#         .filter(Invoice.id == overdue_id)
#     )

#     result = query.first()
#     return result

# def update_overdue(db: Session, overdue_id: int, overdue_data: OverdueUpdateSchema):
#     invoice = db.query(Invoice).filter(Invoice.id == overdue_id).first()

#     if not invoice:
#         return {"error": "Overdue not found"}

#     for key, value in overdue_data.dict().items():
#         setattr(invoice, key, value)

#     db.commit()
#     return {"message": "Overdue updated successfully"}
