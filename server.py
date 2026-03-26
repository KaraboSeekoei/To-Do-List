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

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return {"task": task}
    return {"message": "Task not found"}

@app.delete("/tasks/{task_id}")
def delete_task(task_id):
    global tasks
    original_len = len(tasks)
    tasks = [task for task in tasks if task["id"] != task_id]
    
    if len(tasks) == original_len:
        return {"message": "Task not found"}
    return {"message": "Task deleted successfully"}