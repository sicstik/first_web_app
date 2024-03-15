# this is a function
def get_todos(todos_file="todos.txt"):
    """ Read all items as a list from the todos.txt file"""
    with open(todos_file) as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(list_local, todos_file="todos.txt"):
    """" Writes a whole new list of your choice into the file path todos.txt """
    with open(todos_file, "w") as file_local:
        file_local.writelines(list_local)

if __name__ == "__main__":
    print("hello from functions")
