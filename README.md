# Task_Manager
This task manager programme allows a group of people to manage and organise tasks between themselves.

## How This Programme Works
* The person with the admin role is allowed to:
	- Register a new user
	- Add a new task
	- View all tasks
	- View only his/her tasks
	- Generate reports
	- Display statistics

* Other users are only allowed to:
	- Add new tasks
	- View all tasks
	- View only his/her tasks
	
------------------------------------------------------------------------------------------------------
	
* Registering a new user:
	1. Enter username
	2. Enter password and confirm password
* Once a new user is registered, their username and password is stored in the text file users.txt.
* When a user logs in, the programme checks if the username is in fact in the text file.
If it is, it then checks if the password matches the username.
* More than one user with the same username is not allowed.

------------------------------------------------------------------------------------------------------

* Adding a new task:
	1. Enter the username to which the task is assigned.
	2. Enter the name of the task.
	3. Enter the due date and when the task was assigned.
	4. Give a brief description of the task.
	5. The programme automatically marks the task as incomplete.
* After a new task is added, the programme stores the task in the text file tasks.txt

-------------------------------------------------------------------------------------------------------

* When choosing to view all tasks, the programme reads all tasks from tasks.txt.
* It then displays the task in an easy-to-read list format.

-------------------------------------------------------------------------------------------------------

* If the user chooses to view only his/her tasks, the programme reads tasks.txt and only takes the tasks assigned to user who logged in.
* The user's tasks are displayed in an easy-to-read format.
* There is also an option to edit a selected task:
	* Marking a task as complete.
	* Changed assigned user.
	* Change the due date.
	
-------------------------------------------------------------------------------------------------------

* If the admin chooses to generate reports, the programme calculates and displays a task overview and a user overview.
* The task overview includes:
	* Total number of tasks.
	* Number of completed and incomplete tasks.
	* Number of overdue tasks.
	* Percentage of completed and incomplete tasks.
* The user overview includes:
	* Total number of tasks assigned to each user.
	* Percentage of tasks assigned to each user.
	* Percentage of tasks completed.
	* Percentage of tasks incomplete.
	* Percentage of tasks overdue.

---------------------------------------------------------------------------------------------------------

* If the admin chooses to view statistics, the programme calculates and displays the total number of users and tasks.

----------------------------------------------------------------------------------------------------------
	
