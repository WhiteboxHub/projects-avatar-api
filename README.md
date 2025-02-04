
# Project Avatar API

This is the backend for the **Project Avatar API**, built with **FastAPI** and connected to an existing **MySQL** database. The API allows for basic batch management (get, insert, and delete operations) and is intended to be tested with **Postman**.

## Requirements

- Python 3.9 or higher
- FastAPI
- MySQL
- Postman (for testing the API)

## Setup and Installation

1. Clone this repository to your local machine:
   ```bash
   git clone <repository-url>
   cd project-avatar-api
   ```

2. Install the required Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure your MySQL database is up and running. Update the `DATABASE_URL` connection string in your code to point to the existing database.

4. To run the app locally, execute:
   ```bash
   uvicorn main:app --reload
   ```

5. The app should now be running at `http://127.0.0.1:8000`.

## Testing the API with Postman

1. **Get Batches:**

   - **Method**: `GET`
   - **Endpoint**: `/batch/batches`
   - **Description**: Fetches all the existing batches from the database.
   - **Response**: A list of batches.

2. **Insert New Batch:**

   - **Method**: `POST`
   - **Endpoint**: `/batch/insert`
   - **Description**: Inserts a new batch into the database.
   - **Body**: JSON with batch details (example):
     ```json
     {
       "batch_name": "New Batch",
       "batch_code": "NB001"
     }
     ```

   - **Response**: Confirmation of the inserted batch.

3. **Delete a Batch:**

   - **Method**: `DELETE`
   - **Endpoint**: `/batch/delete/{batch_id}`
   - **Description**: Deletes a batch with the specified `batch_id`.
   - **Response**: Confirmation of deletion.

## Example Endpoints

### Get Batches
```http
GET /batch/
```
- Response Example:
```json
[
  {
    "id": 1,
    "batch_name": "Batch 1",
    "batch_code": "B001"
  },
  {
    "id": 2,
    "batch_name": "Batch 2",
    "batch_code": "B002"
  }
]
```

### Insert New Batch
```http
POST /batch/
```
- Body:
```json
{
  "batch_name": "New Batch",
  "batch_code": "NB001"
}
```
- Response Example:
```json
{
  "message": "Batch inserted successfully",
  "batch": {
    "id": 3,
    "batch_name": "New Batch",
    "batch_code": "NB001"
  }
}
```

### Delete a Batch
```http
DELETE /batch/3
```
- Response Example:
```json
{
  "message": "Batch deleted successfully"
}
```

## Notes
- Make sure to update the database connection details according to your setup.
- This API is intended for basic batch operations and can be extended with additional routes as needed.
