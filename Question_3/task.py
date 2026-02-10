import sys
import os
from datetime import datetime

TODO_FILE = "todo.txt"
DONE_FILE = "done.txt"


def read_file(filename):
    if not os.path.exists(filename):
        return []
    with open(filename, "r") as f:
        return [line.strip() for line in f.readlines()]


def write_file(filename, lines):
    with open(filename, "w") as f:
        for line in lines:
            f.write(line + "\n")


def add(task):
    todos = read_file(TODO_FILE)

    if task not in todos:
        with open(TODO_FILE, "a") as f:
            f.write(task + "\n")
    else:
        todos = [t for t in todos if t != task]
        todos.append(task)
        write_file(TODO_FILE, todos)

    print(f'Added todo : "{task}"')


def delete(k):
    todos = read_file(TODO_FILE)

    if k < 1 or k > len(todos):
        print(f"ERROR...! task #{k} does not exist! No task is deletd!")
        return

    del todos[k - 1]
    write_file(TODO_FILE, todos)
    print(f"Deleted todo #{k}")


def done(k):
    todos = read_file(TODO_FILE)

    if k < 1 or k > len(todos):
        print(f"ERROR...! task #{k} doesn't exist!")
        return

    task = todos[k - 1]
    del todos[k - 1]
    write_file(TODO_FILE, todos)

    today = datetime.now().strftime("%Y-%m-%d")
    with open(DONE_FILE, "a") as f:
        f.write(f"x {today} {task}\n")

    print(f"Marked todo #{k} as done.")


def ls():
    todos = read_file(TODO_FILE)

    if len(todos) == 0:
        print("There are no pending todos.")
        return

    for i in range(len(todos) - 1, -1, -1):
        print(f"[{i + 1}] {todos[i]}")


def help_cmd():
    print("How to use this TODO APP :-")
    print('$ python todoapp.py add "todo item"  # Add a new todo')
    print("$ python todoapp.py del NUMBER       # Delete a todo")
    print("$ python todoapp.py done NUMBER      # Complete a todo")
    print("$ python todoapp.py ls               # Show pending todos")
    print("$ python todoapp.py help             # Show help")
    print("$ python todoapp.py report           # Show statistics")


def report():
    pending = len(read_file(TODO_FILE))
    completed = len(read_file(DONE_FILE))
    today = datetime.now().strftime("%Y-%m-%d")

    print(
        f"{today} Pending Tasks : {pending} "
        f"Completed Tasks : {completed}"
    )


def main():
    if len(sys.argv) == 1 or sys.argv[1] == "help":
        help_cmd()
        return

    cmd = sys.argv[1]

    if cmd == "add":
        if len(sys.argv) < 3:
            print("ERROR...! Missing todo string! Nothing Added!")
        else:
            add(sys.argv[2])

    elif cmd == "del":
        if len(sys.argv) < 3:
            print("ERROR...! Missing task number! No task is deletd!")
        else:
            delete(int(sys.argv[2]))

    elif cmd == "done":
        if len(sys.argv) < 3:
            print("ERROR...! Missing task number! No task is marked completed!")
        else:
            k = int(sys.argv[2])
            if k > 0:
                done(k)
            else:
                print("ERROR...! todo #0 does not exist!")

    elif cmd == "ls":
        ls()

    elif cmd == "report":
        report()

    else:
        help_cmd()


if __name__ == "__main__":
    main()
