# CB 1st User Interface

from student import *
from gradebook import *
from helper import *
from saving_parsing import *

# main_interface():
    # have user enter file path for students csv
    # if it does not exist, call initialize_students from saving_parsing
    # if it does, call load_students form saving_parsing
    # while True:
        # give user options from gradebook methods, such as edit student, add student, remove student, search student, class statistics, and other stuff (also a save option)
        # use match-case to see what user entered
        # call appropiate methods

def main_interface():
    while True:
        file_path = input("Enter file path of gradebook you want to load:\n").strip()
        succesful_load = load_students(file_path)
        if succesful_load == False:
            continue

        

