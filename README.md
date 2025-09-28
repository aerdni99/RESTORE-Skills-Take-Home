# RESTORE-Skills-Take-Home
FastAPI take home assignment for RESTORE-Skills Junior Integrations Engineer Application

### Schemas
```json
Therapists {
    "id": "Int (Primary Key)",
    "name": "String (Not Null)",
    "patients": "List[Patient] (Relationship: all patients assigned to this therapist)"
}
```
```json
Patients {
    "id": "Int (Primary Key)",
    "name": "String (Not Null)",
    "therapist_id": "Int (Foreign Key, Therapists.id, Nullable)"
}   
```

### Routes
```python
### General Routes
"/"                                     # GET: root - return root message
"/clear/"                               # DELETE: Clear Tables

### Therapist Routes
"/therapists/"                          # GET: List Therapists
"/therapists/"                          # POST: Create Therapist
"/therapists/{therapist_id}"            # GET: Get Therapist by ID
"/therapists/{therapist_id}"            # DELETE: Delete Therapist by ID

### Patient Routes
"/patients/"                            # GET: List Patients
"/patients/"                            # POST: Create Patient
"/patients/{patient_id}"                # GET: Get Patient by ID
"/patients/{patient_id}"                # DELETE: Delete Patient by ID
"/patients/{patient_id}/{therapist_id}" # POST: Assign Therapist to Patient
```

### Files
| File Name | Description |
|--------------------|---|
| dockerfile         | Makes a Python container, installs the dependencies listed in requirements.txt, copies project source files, runs the project. |
| docker-compose.yml | Builds a container out of the dockerfile in this directory as well as a postgres image. |
| requirements.txt   | list of python modules I use for this project, dockerfile reads this. |
| database.py        | Constructs DB connection engine, Session creator, and ORM Base class for inheritance. |
| models.py          | Defines the structure of tables in my DB. |
| schemas.py         | Defines expected I/O datatypes for database interactions in my API. |
| crud.py            | Constructs DB Queries using SQLAlchemy. |
| main.py            | Define API routes and send args down to logic/validation files (crud.py and schemas.py). |


### Requirements.txt
| Dependency Name | Usage |
|-------------------|---|
| fastapi           | Used in main.py to create my api app, I also use "Depends" function to wait for database sessions, and HTTPException for error handling. |
| uvicorn[standard] | Launch command for running my app, handles HTTP requests. |
| psycopg2-binary   | Used by sqlalchemy to connect to the database. |
| sqlalchemy        | My ORM of choice. |
| pydantic          | Ensures expected datatypes for input output of database functions in my API. Used in Schemas.py |

### Notes


