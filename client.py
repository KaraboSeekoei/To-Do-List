import requests

BASE_URL = "http://127.0.0.1:8000/tasks"

def create_task():
    task_id = input("Enter task ID: ")
    title = input("Enter task title: ")
    completed = input("Is it completed? (y/n): ").lower() == "y"
    task_data = {"id": task_id, "title": title, "completed": completed}
    response = requests.post(BASE_URL, json=task_data)
    print("Response:", response.json())

def get_all_tasks():
    response = requests.get(BASE_URL)
    print("All Tasks:", response.json())

def get_task_by_id():
    task_id = input("Enter task ID: ")
    response = requests.get(f"{BASE_URL}/{task_id}")
    print("Response:", response.json())

def delete_task():
    task_id = input("Enter task ID to delete: ")
    response = requests.delete(f"{BASE_URL}/{task_id}")
    print("Response:", response.json())

def main():
    while True:
        print("\nOptions:")
        print("1. Create task")
        print("2. Get all tasks")
        print("3. Get task by ID")
        print("4. Delete task")
        print("5. Quit")
        choice = input("Choose an option: ")

        if choice == "1":
            create_task()
        elif choice == "2":
            get_all_tasks()
        elif choice == "3":
            get_task_by_id()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()