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
    students = load_students()

    current_gradebook = Gradebook()

    for i in students:
        
        current_gradebook.catalog.append(create_student(i['name'],i['id'],i['academic_standing'],i['grade_level'],i['average'],i['grade1'],i['grade2'],i['grade3'],i['grade4'],i['grade5'],i['grade6'],i['grade7'],i['grade8'],))
        
    while True:
        

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
                    mode = input("Would you like to search by student name or student ID? ID/Name:\n").lower().strip()
                    if mode != 'name' and mode != 'id':
                        print("Please enter a valid answer.")
                        after_action()
                        continue

                    query = input("Enter ID or name of student(s) you want to search for:\n").strip()
                    
                    found_students = current_gradebook.search_student(query,mode)

                    print("Students Found:")

                    for i in found_students:
                        print(i)
                        print(i.view_grades())

                    after_action()
                    break
                continue
            case '5':
                current_gradebook.edit_student()
                continue
            case '6':
                average = current_gradebook.find_average()
                average = round(average,2)
                high, low = current_gradebook.find_high_low()
                print(f"Number of students in class: {len(current_gradebook.catalog)}")
                print(f"Class Grade Average: {average}%\nHighest Grade: {high}%\nLowest Grade: {low}%")
                after_action()
                continue
            case '7':
                current_gradebook.save_students()
                print("File saved.")
                after_action
            case '8':
                print("Goodbye!")
                return
            case _:
                print("Please enter a number between 1 and 8.")
                after_action()


        

