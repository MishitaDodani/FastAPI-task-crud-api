# Task API with FastAPI and sqlite3

## How to Run

### 1. Clone the repository
```bash
git clone https://github.com/MishitaDodani/FastAPI-task-crud-api.git
cd FastAPI-task-crud-api
```

### 2. Create a virtual environment
python -m venv venv
source venv/bin/activate  
or 
venv\Scripts\activate on Windows

### 3. Install dependencies
pip install -r requirements.txt

### 4. Run the API
uvicorn main:app --reload

### 5. Visit the API documentation
Go to: http://127.0.0.1:8000/docs

## API Endpoints

- `POST /tasks` – Create a task
- `GET /tasks` – Get all tasks
- `GET /tasks?is_completed=true` – Filter tasks by status
- `GET /tasks/{id}` – Get task by ID
- `PUT /tasks/{id}` – Update task
- `DELETE /tasks/{id}` – Delete task
