# Define Task Structure
class Task:
    def __init__(self, name, status="Incomplete", due_date=None):
        self.name = name
        self.status = status
        self.due_date = due_date

# Store Tasks (as a list)
tasks = []

# Add Task
def add_task():
    name = input("Enter task name: ")
    due_date = input("Enter due date (optional): ")
    task = Task(name, due_date=due_date)
    tasks.append(task)
    print("Task added successfully!")

# View Tasks
def view_tasks():
    print("Tasks:")
    for idx, task in enumerate(tasks, 1):
        print(f"{idx}. {task.name} - {task.status} - Due: {task.due_date}")

# ... (Implement Update, Delete, Save, Load functions)

# User Interaction (CLI)
while True:
    print("\n1. Add Task\n2. View Tasks\n3. Exit")
    choice = input("Enter choice: ")
    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        break
    else:
        print("Invalid choice! Please try again.")
