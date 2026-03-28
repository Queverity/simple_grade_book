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
        students = load_students()

        current_gradebook = Gradebook()

        for i in students:
            student_object = create_student(i['name'],i['id'],i['academic_standing'],i['grade_level'],i['grades'],i['grade_average'])
            current_gradebook.catalog.append(student_object)

        if students == False:
            continue

        print("What would you like to do?\n1. View All Students\n2. Add Student\n3. Remove Student\n4. Search Gradebook\n5. Edit Student\n6. Class Statistics\n7. Save Gradebook\n8. Exit")
        choice = input("Enter number 1 - 8:\n").strip()

        clear_screen()

        match choice:
            case '1':
                current_gradebook.view_all()
                continue
            case '2':
                current_gradebook.add_student()
                continue
            case '3':
                current_gradebook.remove_student()
                continue
            case '4':
                while True:
                    mode = input("Would you like to search by student name or student ID?").lower().strip()
                    if mode != 'name' and mode != 'id':
                        print("Please enter a valid answer.")
                        after_action()
                        continue

                    query = input("Enter ID or name of student(s) you want to search for:\n").strip()
                    
                    found_students = current_gradebook.search_student(query,mode)

                    for i in found_students:
                        print(i)

                    after_action()
            case '5':
                current_gradebook.edit_student()
                continue
            case '6':
                average = current_gradebook.find_average()
                high, low = current_gradebook.find_high_low()
                print(f"Class Grade Average: {average}%\nHighest Grade: {high.average}%\nLowest Grade: {low.average}")
                after_action()
                continue
            case '7':
                save_students(students)
                print("File saved.")
                after_action
            case '8':
                print("Goodbye!")
                return
            case _:
                print("Please enter a number between 1 and 8.")
                after_action()


        

