import os

__isrunning_file_location__ = os.path.realpath(os.path.join(
    os.getcwd(), os.path.dirname(__file__), "isrunning.txt"))

def mark_as_not_running():
    with open(__isrunning_file_location__, "w") as file:
        file.write("no")

def mark_as_running():
    with open(__isrunning_file_location__, "w") as file:
        file.write("yes")

def is_running() -> bool:
    with open(__isrunning_file_location__, "r") as file:
        return file.read() == "yes"