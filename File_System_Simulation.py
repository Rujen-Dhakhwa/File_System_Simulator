from Commands import Status  # Assuming Status class or enum is defined elsewhere

# Simulated file system structure
file_structure_dict = {
    "root": ["c", "d"],  # Root contains two directories
    "c": ["hello.jpg", "welcome.txt"],
    "d": ["print.jpg", "WEEKEND.COM"]
}

current_dir = "root"


def change_directory(dir_name):
    """Change the current directory."""
    global current_dir
    if dir_name == "..":
        if current_dir != "root":
            current_dir = "/".join(current_dir.split("/")[:-1]) or "root"
        else:
            print("Error: Already at the root directory.")
    elif dir_name in file_structure_dict.get(current_dir, []):
        current_dir = f"{current_dir}/{dir_name}"
    else:
        print(f"Error: Directory '{dir_name}' not found in {current_dir}.")


def list_directory():
    """List contents of the current directory."""
    last_dir = current_dir.split("/")[-1]
    contents = file_structure_dict.get(last_dir, [])
    if contents:
        print(" ".join(contents))
    else:
        print("This directory is empty.")


def create_directory(dir_name):
    """Create a new directory inside the current directory."""
    if dir_name in file_structure_dict.get(current_dir, []):
        print(f"Error: Directory '{dir_name}' already exists.")
    else:
        file_structure_dict.setdefault(current_dir, []).append(dir_name) # creating new directory
        file_structure_dict[f"{current_dir}/{dir_name}"] = []
        print(f"Directory '{dir_name}' created.")



def remove_directory(dir_name):
    """Remove a directory inside the current directory."""
    if dir_name in file_structure_dict.get(current_dir, []):
        # Remove directory from current directory
        file_structure_dict[current_dir].remove(dir_name)
        # Also remove its entry from the file structure dictionary
        del file_structure_dict[f"{current_dir}/{dir_name}"]
        print(f"Directory '{dir_name}' removed.")
    else:
        print(f"Error: Directory '{dir_name}' not found in {current_dir}.")

def remove_file(file_name):
    """Remove a file inside the current directory."""
    if file_name in file_structure_dict.get(current_dir, []):
        file_structure_dict[current_dir].remove(file_name)
        print(f"File '{file_name}' removed.")
    else:
        print(f"Error: File '{file_name}' not found in {current_dir}.")


def rename_directory(old_name, new_name):
    """Rename a directory inside the current directory."""
    if old_name in file_structure_dict.get(current_dir, []):
        # Rename the directory in the current directory list
        file_structure_dict[current_dir].remove(old_name)
        file_structure_dict[current_dir].append(new_name)

        # Rename the full path entry in the file structure dictionary
        file_structure_dict[f"{current_dir}/{new_name}"] = file_structure_dict.pop(f"{current_dir}/{old_name}")

        print(f"Directory '{old_name}' renamed to '{new_name}'.")
    else:
        print(f"Error: Directory '{old_name}' not found in {current_dir}.")


def rename_file(old_name, new_name):
    """Rename a file inside the current directory."""
    if old_name in file_structure_dict.get(current_dir, []):
        # Rename the file in the current directory list
        file_structure_dict[current_dir].remove(old_name)
        file_structure_dict[current_dir].append(new_name)

        print(f"File '{old_name}' renamed to '{new_name}'.")
    else:
        print(f"Error: File '{old_name}' not found in {current_dir}.")


def show_help():
    """Display available commands."""
    print("\n".join([status.get_help() for status in Status]))


if __name__ == '__main__':
    print("Welcome to File and Command System.")
    print("Type 'help' for available commands and 'quit' to exit.")

    while True:
        user_input = input(f"{current_dir}> ").strip().lower()
        user_input_arr = user_input.split()
        if not user_input_arr:
            continue  # Ignore empty input

        command = user_input_arr[0]
        command_param = user_input_arr[1] if len(user_input_arr) > 1 else ""

        if command == Status.QUIT.command:
            print("Exited!")
            break
        elif command == Status.CHANGE_DIRECTORY.command:
            change_directory(command_param)
        elif command == Status.LIST_ITEM.command:
            list_directory()
        elif command ==Status.MAKE_DIRECTORY.command:
            if command_param:
                create_directory(command_param)
            else:
                print("Error: Missing directory name. Usage: mkdir <name>")
        elif command == Status.REMOVE_DIRECTORY.command:
            if command_param:
                remove_directory(command_param)
            else:
                print("Error: Missing directory name. Usage: rmdir <name>")
        elif command == Status.REMOVE_FILES.command:
            if command_param:
                remove_file(command_param)
            else:
                print("Error: Missing file name. Usage: rm <file>")
        elif command == "rename":
            if len(user_input_arr) == 3:
                old_name, new_name = user_input_arr[1], user_input_arr[2]
                if new_name in file_structure_dict.get(current_dir, []):
                    print(f"Error: '{new_name}' already exists. Please choose another name.")
                else:
                    rename_directory(old_name, new_name)
            else:
                print("Error: Usage: rename <old_name> <new_name>")
        elif command == Status.RENAME.command:
            if len(user_input_arr) == 3:
                old_name, new_name = user_input_arr[1], user_input_arr[2]
                if new_name in file_structure_dict.get(current_dir, []):
                    print(f"Error: '{new_name}' already exists. Please choose another name.")
                else:
                    rename_file(old_name, new_name)
            else:
                print("Error: Usage: renamefile <old_name> <new_name>")
        elif command in ["h", "help"]:
            show_help()
        else:
            print(f"Error: Unknown command '{command}'. Type 'help' for options.")






