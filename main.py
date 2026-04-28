"""Laboratorio 8 - CLI del gestor de tareas."""

import sys
from todo_manager import read_todo_file, write_todo_file

def main():
    try:
        if len(sys.argv) < 2:
            raise IndexError("Insufficient arguments provided!")

        # Help
        if sys.argv[1] == "--help":
            print("""Usage: python main.py <file_path> <command> [arguments]...

Commands:
  add "task"    - Add a task to the list.
  remove "task" - Remove a task from the list.
  view          - Display all tasks.

Examples:
  python main.py tasks.txt add "Buy groceries"
  python main.py tasks.txt remove "Do laundry"
  python main.py tasks.txt view
  python main.py tasks.txt add "Call mom" remove "Take out trash" view""")
            return

        file_path = sys.argv[1]

        # Si no hay comando → termina silenciosamente
        if len(sys.argv) == 2:
            return

        # Leer tareas UNA sola vez
        tasks = read_todo_file(file_path)

        i = 2  # empezamos desde el comando

        while i < len(sys.argv):
            command = sys.argv[i]

            # -------- VIEW --------
            if command == "view":
                print("Tasks:")
                for task in tasks:
                    print(task)
                i += 1

            # -------- ADD --------
            elif command == "add":
                try:
                    task = sys.argv[i + 1]
                except IndexError:
                    raise IndexError('Task description required for "add".')

                tasks.append(task)
                print(f'Task "{task}" added.')
                i += 2

            # -------- REMOVE --------
            elif command == "remove":
                try:
                    task = sys.argv[i + 1]
                except IndexError:
                    raise IndexError('Task description required for "remove".')

                try:
                    tasks.remove(task)
                    print(f'Task "{task}" removed.')
                except ValueError:
                    print(f'Task "{task}" not found.')

                i += 2

            # -------- INVALID COMMAND --------
            else:
                raise ValueError("Command not found!")

        # Escribir UNA sola vez al final
        write_todo_file(file_path, tasks)

    except IndexError as e:
        print(e)
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()