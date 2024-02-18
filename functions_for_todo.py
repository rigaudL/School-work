def read_todos_from_file(filepath = "logs.txt"):
        with open("logs.txt", "r") as f:
            todos = f.readlines()
        return todos


def write_todos_to_file(todos, filepath="logs.txt"):
    with open(filepath, "a") as f:  # Open file in write mode to overwrite existing content
        for todo_item in todos:
            x = todo_item
        f.write(x)  # Write each todo to a new line in the file
