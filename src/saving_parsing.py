# CB 1st Saving Parsing Files

import csv
from helper import *

# def load_students():
    # use with open to load the file so it will close on its own
    # for name, id, academic_standing, and grade_level, just read them normally
    # for grades, put them each into a list, and then add that to the dictionary (if a grade is N/A, that just means no grade has been entered)

# def save_students():
    # use with open to the load the file so it will close on its own
    # for name, id, academic_standing, and grade_level, just write them normally
    # iterate through grades list and write that

# def initialize_students():
    # to be used if user enters a file path that leads to a non-existent file
    # create the file with the proper fieldnames, found in students.csv

def load_students():
    
    with open("documents/students.csv", mode="r") as students:
        fieldnames = ['name','id','academic_standing','grade_level','grades','grade_average']
        reader = csv.DictReader(students,fieldnames)
        next(students)

        students = []

        for i in reader:
            i['grades'] = list([i['grades']])
            students.append(i)

        for i in students:
            print(i['grade_average'])

        after_action()

        return students
    
    
def save_students(students):
    with open("documents/students.csv",mode="w",newline="") as students:
        fieldnames = ['name','id','academic_standing','grade_level','grades','grade_average']
        writer = csv.DictWriter(students)
        basic_writer = csv.writer(students)

        basic_writer.write(fieldnames)

        for i in students:
            writer.write(i)


        


