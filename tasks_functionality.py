import csv
tasks = [] 
def new_page():
    task = input("Enter a new task:")
    tasks.append(task)
    with open('tasks.csv', mode='a', newline='') as file:
    # Create a CSV writer object
        writer = csv.writer(file)
        writer.writerow(tasks)

    # Write the list as a new row
        print(f"{task} has been added")
        

# def view_task():
#     view = readfile()