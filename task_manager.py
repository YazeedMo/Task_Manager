# Define function "main_loop" - loops the over the whole programme
def main_loop():
    # Import datetime module
    import datetime

    print("\n\n===== TASK MANAGER =====\n")

    dashes = "--------------------------------------------------"

    # Assign empty list to variable "username_stored" - used to store the username once a person has logged in
    username_stored = []

    # Define function "commands" - contains the main menu
    def commands():

        # If admin logged in - display all options
        if username_stored[0] == "admin":
            command = input("""Select one of the following options:
r  --> Register user
a  --> Add task
va --> View all tasks
vm --> View my tasks
gr --> Generate reports
ds --> Display statistics
e  --> exits

> """).lower()

            # Call the appropriate function once the user has entered an option.
            if command == "r":
                reg_user()
            elif command == "a":
                add_task()
            elif command == "va":
                view_all()
            elif command == "vm":
                view_mine()
            elif command == "gr":
                reports()
            elif command == "ds":
                stats()
            elif command == "e":
                print(f"\n{dashes}\n")
                main_loop()
            else:
                print(f"{command} is not an option.\n")
                commands()

        # If the user is not admin - allow access to only certain options
        else:
            command = input("""Select one of the following options:
a  --> Add task
va --> View all tasks
vm --> View my tasks
e  --> exit

> """).lower()

            # Call appropriate function after user has entered an option.
            if command == "a":
                add_task()
            elif command == "va":
                view_all()
            elif command == "vm":
                view_mine()
            elif command == "e":
                print(f"\n{dashes}\n")
                main_loop()
            else:
                print(f"{command} is not an option.\n")
                commands()

    # Define function "reg_user" - used to register a new user
    def reg_user():

        # Read the content from "user.txt" and store all usernames and passwords in variable "users_list"
        with open("user.txt", "r") as users:
            users = users.read()

        users_list = users.replace(",", "").replace("\n", " ").split(" ")

        # In a while loop, request username of user to be registered.
        # Check if the username already exist. If it does tell user that it already exists and request username again
        while True:
            new_username = input("Username: ")

            if new_username in users_list:
                print(f"{new_username} is already registered.\n")
            else:

                # In a while loop, request password of new user.
                # Request password confirmation. If confirmed password does not match original password - request
                # password again
                # If confirmed password matched original password - break out of while loop
                while True:
                    new_password = input("Password: ")
                    new_password_confirm = input("Confirm password: ")

                    if new_password_confirm != new_password:
                        print("Passwords do not match.\n")
                    else:
                        break
                break

        # Open "user.txt" and append the new username and password.
        with open("user.txt", "a") as users:
            users.write(f"\n{new_username}, {new_password}")

        print(f"\n{new_username} has been registered.\n")
        print(f"{dashes}\n")

        commands()

    # Define function "add_task" - used to add a new task
    def add_task():

        # Open "user.txt". Read the contents and store it as a list in variable "user_list"
        with open("user.txt", "r") as users:
            users = users.read()

        users_list = users.replace(",", "").replace("\n", " ").split(" ")

        # In a while loop request user to which the task will be assigned
        # If the username is not in "user_list" (not registered) - request assigned user again
        while True:
            assigned_user = input("Assigned to: ")

            if assigned_user not in users_list:
                print(f"{assigned_user} has not been registered.\n")
            else:
                break

        # Request all information about the new added task
        task = input("Task: ")
        date_assigned = input("Date assigned (d/m/y): ")
        due_date = input("Due date (d/m/y): ")
        description = input("Task description: ")

        # Open "tasks.txt" and append all the tasks information
        with open("tasks.txt", "a") as tasks:
            tasks.write(f"\nAssigned to:       {assigned_user},Task:              {task},"
                        f"Date assigned:     {date_assigned},Due date:          {due_date},"
                        f"Task description:  {description},Task completed:    No")

            print("\nTask added")
            print(f"{dashes}\n")

        commands()

    # Define function "view_all" - used to view all tasks
    def view_all():

        # Open "tasks.txt" - read all its contents and store it as a list in "ll_tasks_list"
        with open("tasks.txt", "r") as tasks:
            tasks = tasks.read()

        all_tasks_list = tasks.replace("\n", "\n\n").replace(",", "\n").split("\n\n")

        tasks_string = ""

        # Display all the tasks
        for task in all_tasks_list:
            tasks_string += task + "\n\n" + "**************************************************" + "\n\n"

        print(f"\n\n{tasks_string}")
        print(f"\n{dashes}")
        print()

        commands()

    # Define function "view_ine" - used to view only the logged in user's tasks
    def view_mine():

        # Open "tasks.txt" and store its contents in a list in variable "all_tasks_list
        with open("tasks.txt", "r") as tasks:
            tasks = tasks.read()

        # Loop through "all_tasks_list" and extract only tasks belonging to the logged in user
        # Store all the extracted tasks in "my_tasks_list"
        # Display all the user's tasks
        all_tasks_list = tasks.replace("\n", "\n\n").replace(",", "\n").split("\n\n")
        my_tasks_list = [my_tasks for my_tasks in all_tasks_list if username_stored[0] in my_tasks]
        my_tasks_list_length = len(my_tasks_list)
        my_tasks_string = ""

        count = 1
        for each_task in my_tasks_list:
            my_tasks_string += f"{count})\n{each_task}\n\n"
            count += 1

        print(f"\n{username_stored[0]}'s Tasks:")
        print(f"\n{my_tasks_string}")

        print(dashes)

        # In a while loop, allow user to edit any of their tasks
        # Also allow option to return to main menu ("commands()")
        while True:
            view_mine_commands = input(f"\n-1     --> Return to main menu."
                                       f"\n1 to {my_tasks_list_length} --> Select task."
                                       f"\n\n> ")

            if view_mine_commands == "-1":
                print(f"{dashes}\n")
                commands()

            elif int(view_mine_commands) <= my_tasks_list_length:

                chosen_index = int(view_mine_commands) - 1

                all_tasks_list = tasks.split("\n")
                my_tasks_list = [my_tasks for my_tasks in all_tasks_list if username_stored[0] in my_tasks]
                task_to_edit = my_tasks_list[chosen_index]
                task_details = task_to_edit.split(",")

                all_tasks_list_index = all_tasks_list.index(task_to_edit)

                # If user wants to change task status to complete - update the task in [all_tasks_list]
                if task_details[5] == "Task completed:    Yes":
                    print("\n>>> Task completed.")
                    print(f"\n{dashes}")
                    view_mine()
                else:
                    while True:
                        edit_command = input("1 --> Mark as complete.\n2 --> Change assigned user"
                                             "\n3 --> Change due date"
                                             "\n\n> ")

                        # Define function "task_detail_update" - used to update any changes done to a task
                        def task_detail_update():
                            task_details_string = ""
                            counter = 0
                            for each_detail in task_details:
                                if counter <= 4:
                                    task_details_string += each_detail + ","
                                    counter += 1
                                else:
                                    task_details_string += each_detail

                            all_tasks_list[all_tasks_list_index] = task_details_string

                            all_tasks_list_string = ""
                            counter = 0
                            for every_task in all_tasks_list:
                                if counter <= len(all_tasks_list) - 2:
                                    all_tasks_list_string += every_task + "\n"
                                    counter += 1
                                else:
                                    all_tasks_list_string += every_task

                            with open("tasks.txt", "w") as add_edited_task:
                                add_edited_task.write(all_tasks_list_string)

                        if edit_command == "1":
                            task_details[5] = "Task completed:    Yes"
                            task_detail_update()
                            print(f"\n>>> Task has been edited.\n\n{dashes}")
                            view_mine()

                        # If the user chooses to change assigned user - Request assigned user and update the task
                        elif edit_command == "2":
                            with open("user.txt", "r") as users:
                                users = users.read()

                            users_list = users.replace(",", "").replace("\n", " ").split(" ")

                            while True:
                                edit_detail = input("Assigned user: ")

                                if edit_detail not in users_list:
                                    print(f"{edit_detail} has not been registered.\n")
                                else:
                                    task_details[0] = f"Assigned to:       {edit_detail}"
                                    task_detail_update()
                                    print(f"\n>>> Task has been edited.\n\n{dashes}")
                                    break
                            view_mine()

                        # If the user chooses to change the due date - Request due date and update the task
                        elif edit_command == "3":
                            edit_detail = input("Due date: ")
                            task_details[3] = f"Due date:          {edit_detail}"

                            task_detail_update()
                            print(f"\n>>> Task has been edited.\n\n{dashes}")
                            view_mine()
                        else:
                            print(f"{edit_command} is not an option.\n")

            else:
                print(f"{view_mine_commands} is not an option.")

    # Define function "reports" - used to generate reports
    def reports():

        # Use datetime module to get the current date
        current_date = datetime.datetime.today()

        # Define function "task_overview" - used to get an overview of all the tasks
        def task_overview():

            # Open "tasks.txt" and store its contents in a list in variable "all_tasks_list"
            with open("tasks.txt", "r") as tasks:
                tasks = tasks.read()

            all_tasks_list = tasks.split("\n")

            # Separate all incomplete tasks and store in in variable "incomplete_tasks_list" as a list
            incomplete_tasks_list = []
            for task in all_tasks_list:
                if "Task completed:    No" in task:
                    incomplete_tasks_list.append(task)

            # Use datetime module to check if a task is overdue - use "overdue_task_count" to count all overdue tasks
            overdue_task_count = 0
            for task in incomplete_tasks_list:
                details = task.split(",")
                edit_detail = details[3]
                date_string = edit_detail[19:]
                date = datetime.datetime.strptime(date_string, "%d/%m/%y")
                if current_date > date:
                    overdue_task_count += 1

            total_num_tasks = len(all_tasks_list)
            total_num_uncompleted = len(incomplete_tasks_list)
            total_num_completed = total_num_tasks - total_num_uncompleted
            total_num_overdue = overdue_task_count
            percent_incomplete = round((100 / total_num_tasks) * total_num_uncompleted, 2)
            percent_overdue = round((100 / total_num_tasks) * total_num_overdue, 2)

            # Open "task_overview.txt" and overwrite it with all new task overview information
            with open("task_overview.txt", "w") as blank_overview:
                blank_overview.write(f"""===== Task Overview =====

Total number of tasks:   {total_num_tasks}
Completed tasks:         {total_num_completed}
Incomplete tasks:        {total_num_uncompleted}
Incomplete and overdue:  {total_num_overdue}
Percentage incomplete:   {percent_incomplete}%
Percentage overdue:      {percent_overdue}%""")

            with open("task_overview.txt", "r") as task_overview_content:
                task_overview_content = task_overview_content.read()

            print(f"\n{task_overview_content}\n")
            print(dashes)
            print()

        # Define function "user_overview" - used to get an overview of all the users
        def user_overview():
            with open("user.txt", "r") as users:
                users = users.read()

            users_list = users.replace(",", "").replace("\n", " ").split(" ")
            name_list = [name for name in users_list if users_list.index(name) % 2 == 0]

            with open("tasks.txt", "r") as tasks:
                tasks = tasks.read()
            all_tasks_list = tasks.split("\n")

            with open("user_overview.txt", "w") as blank_overview:
                blank_overview.write(f"""===== User Overview =====
Total number of users: {len(name_list)}
Total number of tasks: {len(all_tasks_list)}
""")
            # Use while loop and for loops to get all information about each user
            index = 0
            while index <= len(name_list) - 1:
                user_tasks = [user_tasks for user_tasks in all_tasks_list if name_list[index] in user_tasks]

                # Get number of completed tasks
                completed_tasks = 0
                for each_task in user_tasks:
                    if "Task completed:    Yes" in each_task:
                        completed_tasks += 1

                # Get list of all uncompleted tasks
                uncompleted_tasks = []
                for each_task in user_tasks:
                    if "Task completed:    No" in each_task:
                        uncompleted_tasks.append(each_task)

                # Get number of all overdue tasks
                overdue_tasks_count = 0
                for each_task in uncompleted_tasks:
                    details = each_task.split(",")
                    detail = details[3]
                    date_string = detail[19:]
                    date_string = datetime.datetime.strptime(date_string, "%d/%m/%y")
                    if current_date > date_string:
                        overdue_tasks_count += 1

                total_num_tasks = len(all_tasks_list)
                user_num_tasks = len(user_tasks)
                percent_all_tasks = round((100 / total_num_tasks) * user_num_tasks, 2)
                percent_complete = round((100 / user_num_tasks) * completed_tasks, 2)
                percent_incomplete = round((100 / user_num_tasks) * len(uncompleted_tasks), 2)
                percent_overdue = round((100 / user_num_tasks) * overdue_tasks_count, 2)

                # Open "user_overview.txt" and overwrite it with all user overview information
                with open("user_overview.txt", "a") as blank_overview:
                    blank_overview.write(f"""
>>> {name_list[index]} <<<
Total number of assigned tasks:  {user_num_tasks}
Total tasks as a percentage:     {percent_all_tasks}%
Assigned tasks completed:        {percent_complete}%
Assigned tasks incomplete:       {percent_incomplete}%
Assigned tasks overdue:          {percent_overdue}%\n""")

                index += 1

            with open("user_overview.txt", "r") as user_overview_content:
                user_overview_content = user_overview_content.read()

            print(user_overview_content)
            print(f"{dashes}\n")

        task_overview()

        user_overview()

        commands()

    # Define function "stats" - used to view task manager statistics
    def stats():

        # Open "user.txt" - Determine number of users
        with open("user.txt", "r") as users:
            users = users.read()

        users_list = users.split("\n")
        num_users = len(users_list)
        print(f"\nTotal number of users: {num_users}")

        # Open "tasks.txt" - Determine number of tasks
        with open("tasks.txt", "r") as tasks:
            tasks = tasks.read()

        tasks_list = tasks.split("\n")
        num_tasks = len(tasks_list)
        print(f"Total number of tasks: {num_tasks}\n")

        print(f"{dashes}\n")

        commands()

    # Define function "login" - used to log into taskmanager
    def login():
        print("Please login\n")

        # In a while loop - Request username and password
        # If username or password is not in "user.txt" - Request username and password and again
        # If username and password is correct - allow user to login
        entry = False
        while not entry:

            with open("user.txt", "r") as users:
                users = users.read()

            users_list = users.replace(",", "").replace("\n", " ").split(" ")

            username = input("Username: ")
            password = input("Password: ")

            if username not in users_list or password != users_list[users_list.index(username) + 1]:
                print("Incorrect username or password.\n")
            else:
                print(f"\nWelcome back {username}!\n")
                username_stored.append(username)
                print(f"{dashes}\n")
                entry = True

        commands()

    login()


main_loop()
