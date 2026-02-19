import tasks_functionality
user_input = input("What are we doing today?\n1. Enter new task\n2. View task \n3. Exit\n\n1,2 or 3:")
def features():
        if user_input == "1":
            tasks_functionality.new_page()
        # return
features()
