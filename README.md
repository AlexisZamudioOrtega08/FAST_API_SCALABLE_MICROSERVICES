# FAST_API_SCALABLE_MICROSERVICES

## This is a sample of API microservice comsumption.

### The API (Employees) support the following operations:
    READ: Return a json with employees details.
    CREATE: Create a new employee.

### GET an employee by id:
```http
  method: GET 
  localhost:8001/api/v1/employee/?emp_id=1
```
| Parameter      | Type     | Description                         |
| :------------- | :------- | :---------------------------------  |
| `emp_id`       | `int`    | **Required**. Employee id           |

#### GET all employees
```http
  method: GET
  localhost:8001/api/v1/employee/all
```

#### POST employee
```http
  method: POST
  localhost:8001/api/v1/employee/add
```

| Parameter      | Type     | Description                         |
| :------------- | :------- | :---------------------------------  |
| `id`           | `int`    | **Required**. Employee id           |
| `first_name`   | `string` | **Required**. Employee first_name   |
| `surname`      | `string` | **Required**. Employee surname      |

```http
    {
        "id": 1,
        "first_name": "John",
        "surname": "Doe"
    }
```

#### GET all timesheet entries
```http
  method: GET
  localhost:8000/api/v1/timesheet/all
```

#### POST timesheet entry
```http
  method: POST
  localhost:8000/api/v1/timesheet/add/?emp_id=1
```

| URL parameter  | Type     | Description                         |
| :------------- | :------- | :---------------------------------  |
| `emp_id`       | `int`    | **Required**. Employee id           |


| Body params    | Type     | Description                         |
| :------------- | :------- | :---------------------------------  |
| `id`           | `int`    | **Required**. Entry id              |
| `hours`        | `int`    | **Required**. Hours worked by emp   |
| `description`  | `string` | **Required**. Description           |


```http
    {
    "id": 0,
    "hours": 0,
    "description": "string"
    }
```

### The timesheet API comsumps employee API as microservice, it consults and retreive data to verify if the employee is in the database to fetch emp_id, first_name, surname.

### NOTE: THIS API IS USING A SQLITE AND MYSQL DATABASE TO STORE DATA AND RETRIEVE DATA (as separate microservices).

### Prior to run any steps, you must have installed a mysql database.

    In timesheet_api folder:
        Create a file called .env
        with the following content:
            MYSQL_HOST=<host>
            MYSQL_USER=<user>
            MYSQL_PASSWORD=<password>
            MYSQL_PORT=<port>
            MYSQL_DB=<database_name>

### For the API usage, please create a python virtual environment and install requirements.txt.

    pip install -r requirements.txt

### Once installated and activated, run 2 simultaneous terminal and execute below.
    On terminal 1:
       Go to src/employee_api and run:
           export API_PREFIX=/api/v1/
           uvicorn main:app --reload --port 8001
    
    On terminal 2:
        Go to src/timesheet_api and run:
            export API_PREFIX=/api/v1/
            uvicorn main:app --reload --port 8000

#### If the step before was completed successfully, you must have running the server on your local host.

    In order to test the API, you can use the following URL:
            localhost:8001/docs (for the employee API documentation)
            localhost:8000/docs (for the timesheet API documentation)
