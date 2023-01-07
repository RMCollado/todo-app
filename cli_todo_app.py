from functions import *
import time

date_and_time = time.strftime("%b %d, %Y %H:%M:%S")
print(f'It is {date_and_time}')
while True:
    user_action = input("Type add, show, edit, complete, or exit: ").strip()

    if user_action.lower().startswith('add'):
        todo = user_action[4:]
        todos = get_todos()

        todos.append(todo + '\n')

        write_todos(todos)

    elif user_action.lower().startswith('show'):
        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            print(f"{index + 1}-{item}")

    elif user_action.lower().startswith("exit"):
        break

    elif user_action.lower().startswith("edit"):
        try:
            number = int(user_action[5:]) - 1

            todos = get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"

            write_todos(todos)
        except ValueError:
            print("The command should be edit then the number")
            continue

    elif user_action.lower().startswith('complete'):
        try:
            number = int(user_action[9:]) - 1

            todos = get_todos()

            todo_to_remove = todos[number].strip("\n")
            todos.pop(number)

            write_todos(todos)

            message = f"Todo {todo_to_remove} was removed"
            print(message)
        except IndexError:
            print("There is no item with that number")
            continue

    else:
        print("Command was not valid")


print("Bye Bye!")
