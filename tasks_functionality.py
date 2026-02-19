tasks = [] 
def new_page():
    task = input("Enter a new task:")
    tasks.append(task)
    print(f"{task} has been added")