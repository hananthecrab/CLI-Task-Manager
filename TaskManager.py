import json
import os
import sys

#configurable path
taskPath = r"C:\Users\zp_al\Downloads\Python projects\Tasks.json"
#loading up tasks first
def loadtask():
    if os.path.exists(taskPath):
        with open(taskPath, "r") as f:
            return json.load(f)
    return []
#saving tasks
def saveTasks(tasks):
    with open(taskPath, "w") as p:
        json.dump(tasks, p, indent=2)

if len(sys.argv) < 2:
    print("Usage: python tasks.py [add | list | delete]")
    sys.exit()

tasks = loadtask()
command = sys.argv[1].lower() # refers to the first command-line argument passed to a script when it is executed from the terminal

if command == "add":
    if len(sys.argv) >= 3:
        dictionary = {"task": sys.argv[2], "done": False}
        tasks.append(dictionary)
        saveTasks(tasks)
        print("Task added")
    else:
        print("Error: Please provide a task description.")

elif command == "list":
    if not tasks:
        print("No tasks!")
    else:
        for num, item in enumerate(tasks, start=1):
            status = "[x]" if item["done"] else "[ ]"
            print(f"{num}. {status} {item['task']}")

elif command == "delete":
    if len(sys.argv) >= 3:
        temp = int(sys.argv[2]) - 1
        tasks.pop(temp)
        saveTasks(tasks)
        print("Task deleted")
    else:
        print("Error: Please provide a task number.")

else:
    print("Unknown command")
