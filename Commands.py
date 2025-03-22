from enum import Enum

class Status(Enum):
    LIST_ITEM = ("ls", "Lists directory contents.")
    CHANGE_DIRECTORY = ("cd", "Changes the current directory.")
    PRINT_DIRECTORY = ("pwd", "Prints the current working directory.")
    RENAME=("rename","Renames the file .")
    MAKE_DIRECTORY = ("mkdir", "Makes new  directories.")
    REMOVE_DIRECTORY = ("rmdir", "Removes directories.")
    REMOVE_FILES = ("rm", "Removes directories.")
    QUIT = ("quit", "Quits from the file system")

    def __init__(self, command, description):
        self.command = command
        self.description = description

    def get_help(self):
        return f"Command: {self.command}\nDescription: {self.description}"


