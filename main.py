import tasks_functionality
import sys
user_input = input("What are we doing today?\n1. Enter new task\n2. View task\n3. Delete task\n4. Exit\n\n1, 2, 3 or 4:")
def features():
        if user_input == "1":
            tasks_functionality.new_page()
        elif user_input == "2":
              tasks_functionality.view_tasks()
        elif user_input == "3":
              tasks_functionality.delete_task()
        elif user_input == "4":
              print('Goodbye!')
              sys.exit()
              
        # return
features()
