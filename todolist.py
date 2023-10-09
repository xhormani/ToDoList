class Task:
    def __init__(self, name, due_date):
        self.name = name
        self.due_date = due_date
        self.completed = False
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def update_task(self, task_name, new_name, new_due_date):
        for task in self.tasks:
            if task.name == task_name:
                task.name = new_name
                task.due_date = new_due_date

    def complete_task(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                task.completed = True

    def list_tasks(self):
        for task in self.tasks:
            status = "Completed" if task.completed else "Incomplete"
            print(f"{task.name} (Due: {task.due_date}) - {status}")
def main():
    todo_list = ToDoList()

    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. Update Task")
        print("3. Complete Task")
        print("4. List Tasks")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Task name: ")
            due_date = input("Due date (YYYY-MM-DD): ")
            task = Task(name, due_date)
            todo_list.add_task(task)
        elif choice == "2":
            task_name = input("Enter task name to update: ")
            new_name = input("New task name: ")
            new_due_date = input("New due date (YYYY-MM-DD): ")
            todo_list.update_task(task_name, new_name, new_due_date)
        elif choice == "3":
            task_name = input("Enter task name to mark as complete: ")
            todo_list.complete_task(task_name)
        elif choice == "4":
            print("\nTasks:")
            todo_list.list_tasks()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
