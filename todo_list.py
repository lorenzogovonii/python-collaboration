class ToDoList:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task):
        self.tasks.append(task)
        print(f'Task "{task}" added!')
    
    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")
    
    def delete_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            print(f'Task "{self.tasks.pop(task_number - 1)}" deleted!')
        else:
            print("Invalid task number.")
    
    def run(self):
        while True:
            choice = input("1. Add Task\n2. View Tasks\n3. Delete Task\n4. Exit\nChoose: ")
            if choice == '1':
                self.add_task(input("Enter task: "))
            elif choice == '2':
                self.view_tasks()
            elif choice == '3':
                self.view_tasks()
                self.delete_task(int(input("Task number to delete: ")))
            elif choice == '4':
                print("Goodbye!")
                break
            else:
                print("Invalid choice.")

if __name__ == "__main__":
    ToDoList().run()
