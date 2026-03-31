# function clear_screen():
    # print function to clear the screen, take this from another project

# function continue_screen():
    # print something like "Press Enter to Continue", put an input() statement after that

# function after_action():
    # combine clear_screen and continue_screen


def clear_screen():
    print("\033c", end="")

def continue_screen():
    print("Press Enter to continue.")
    input()

def after_action():
    continue_screen()
    clear_screen()

def find_object_index(list_of_objects,value):
    for i in list_of_objects:
        if i.id.strip() == value.strip():
            return list_of_objects.index(i)
    return -1