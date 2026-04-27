"""Laboratorio 8 - CLI del gestor de tareas."""

import sys
from todo_manager import read_todo_file, write_todo_file

def main():
    try:
        if len(sys.argv) < 2:
            raise IndexError("Insufficient arguments provided!")

        file_path = sys.argv[1]

        print("Command-line arguments:")
        for arg in sys.argv[1:]:
            print(arg)

        tasks = read_todo_file(file_path)

        print("\nTasks:")
        for task in tasks:
            print(task)

    except IndexError as e:
        print(e)


if __name__ == "__main__":
    main()