import csv
import sys
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

def delete_task(tasks):
    print("These are all the tasks you have:")
    view_tasks()
    for t in tasks:
        d_input = input('Which task do you want to delete? : ')
        if d_input == t:
            tasks.append('')
        print(f'{d_input} deleted')


def close():
    print("Goodbye!")
    sys.exit()
