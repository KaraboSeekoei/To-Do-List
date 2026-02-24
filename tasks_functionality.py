import csv
tasks = [] 
def new_page():
    task = input("Enter a new task:")
    tasks.append(task)
    with open('tasks.csv', mode = 'a', newline = '') as file:
        writer = csv.writer(file)
        writer.writerow(tasks)
        print(f"{task} has been added")
        
def view_tasks():
    with open("tasks.csv", "r") as file:
        reader = csv.reader(file)
        tasks = list(reader)

        if not tasks:
            print("No tasks found.")
        else:
            for index, row in enumerate(tasks, start=1):
                print(f"{index}. {row[0]}")

def delete_task():
    view_tasks()
    d_input = input('Which task do you want to delete? : ')
