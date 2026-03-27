# CB 1st Saving Parsing Files

import csv

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

def initalize_students(file_path):
    try:
        with open(file_path, mode = "w") as students:
            fieldnames = ['name','id','academic_standing','grade_level','grades','grade_average']
            writer = csv.writer(students)
            writer.write(fieldnames)
    except:
        print("Invalid file name")
        return False
    else:
        students = []
        return students

def load_students(file_path):
    try:
        with open(file_path, mode="r") as students:
            fieldnames = ['name','id','academic_standing','grade_level','grades','grade_average']
            reader = csv.DictReader()
            next(students)

            students = []

            for i in reader:
                i['grades'] = list[i['grades']]
                i['grade_average'] = float[i['grade_average']]
                students.append(i)
    except:
        students = initalize_students(file_path)
        return students
    else:
        return students
    
def save_students(file_path,students):
    with open(file_path,mode="w",newline="") as students:
        fieldnames = ['name','id','academic_standing','grade_level','grades','grade_average']
        writer = csv.DictWriter(students)
        basic_writer = csv.writer(students)

        basic_writer.write(fieldnames)

        for i in students:
            writer.write(i)


        


