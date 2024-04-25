import time
import json
import os

def load_tasks(filename='tasks.json'):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks, filename='tasks.json'):
    with open(filename, 'w') as file:
        json.dump(tasks, file, indent=2)

def main():
    tasks = load_tasks()

    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Display Tasks")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task : ")
            tasks.append(task)
            save_tasks(tasks)
            print("Task added successfully!")
        elif choice == "2":
            if tasks:
                print("Tasks:")
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")
                index = int(input("Enter index of task to delete: ")) - 1
                if 0 <= index < len(tasks):
                    del tasks[index]
                    save_tasks(tasks)
                    print("Task deleted successfully!")
                else:
                    print("Invalid index.")
            else:
                print("No tasks to delete.")
        elif choice == "3":
            if tasks:
                print("Tasks:")
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")
            else:
                print("No tasks to display.")
        elif choice == "4":
            print("Exiting Task Manager.")
            break
        else:
            print("Invalid choice. Please try again.")