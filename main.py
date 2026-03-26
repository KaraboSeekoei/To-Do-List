import json
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Load tasks from file at startup
try:
    with open("tasks.json", "r") as f:
        tasks = json.load(f)
except FileNotFoundError:
    tasks = []

class Task(BaseModel):
    title: str
    completed: bool = False

def save_tasks():
    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent=4)

@app.post("/tasks")
def create_task(task: Task):
    new_task = {
        "id": len(tasks) + 1,
        "title": task.title,
        "completed": task.completed
    }
    tasks.append(new_task)
    save_tasks()  # save to file
    return {"message": "Task created successfully", "task": new_task}

@app.get("/tasks")
def get_tasks():
    return {"tasks": tasks}