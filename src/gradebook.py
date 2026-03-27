# CB 1st Gradebook Class

from student import *
from helper import *

# class Gradebook():
    # def __init__(self, catalog = []):
        # catalog is just a list

    # search_student(self):
        # ask user if they would like to search by name or id
        # if name, have user enter name, then iterate through catalog to see which names match, and print those, along with more specific details
        # if id, have user enter id, then iterate through catalog to see which id matches, then print that out

    # edit_student(self):
        # iterate through catalog and print out
        # have user choose student
        # ask user if they would like to edit name, id, add a grade, or remove a grade
        # for name or id, just have user input something new
        # for grades, call methods built into student class

    # add_student(self):
        # have user enter student name and id
        # create student object and save to csv

    # remove_student(self):
        # go through catalog and print out student names and ids
        # ask user who they would like to remove
        # remove that student from catalog

    # view_all()

    # find_average(self):
        # go through catalog, and add each grade in each students list to one big list
        # sum that list and divide by length to find average

    # find_high_low(self):
        # use lambda function to sort catalog list
        # highest will be last index, lowest will be first index (sort based on average)

# def initialize_catalog(students):
    # iterate through students list after loading from CSV and add them one by one to the catalog
    # okay so actually since you can save lists to CSVs, just set it to that

grade_levels = ["9th","10th","11th","12th"]

class Gradebook():

    def __init__(self,catalog):
        self.catalog = catalog
    
    def search_student(self,query,mode):
        students = []
        if mode == "name":
            for i in self.catalog:
                if query.title() == i.name.title():
                    students.append(i)
                else:
                    pass
        else:
            for i in self.catalog:
                if query.title() == i.id:
                    students.append(i)
                    break
                else:
                    pass
        
        return students

    def edit_student(self):
        if bool(self.catalog) == False:
            print("You have no students saved in your gradebook.")
            return
        while True:
            for i in self.catalog:
                print(f"Name: {i.name} | ID {i.id}")
                      
            choice = input("Enter ID of student you want to edit:\n").strip()

            found = False
            for i in self.catalog:
                if choice == i.id.strip():
                    found = True
                    while True:
                        print(f"How would you like to edit student {self.id}?\n1. Add Grade\n2. Remove Grade\n3. Change Name\n4. Change ID\n5. Return to Gradebook Menu")

                        choice = input("Enter number:\n").strip()

                        clear_screen()

                        match choice:
                            case "1":
                                i.add_grade()
                                continue
                            case '2':
                                i.remove_grade()
                                continue
                            case '3':
                                while True:
                                    new_name = input(f"What would you like to change student {i.id}'s name to?").strip()
                                    if new_name.lower() == i.name.lower():
                                        print("That is the same name.")
                                        continue
                                    else:
                                        i.name = new_name
                                        break
                                after_action()
                                continue
                            case '4':
                                while True:
                                    new_id = input(f"What would you like to change {i.name}'s ID to?").strip()
                                    if new_id.lower() == i.id.lower():
                                        print("That is the same ID.")
                                        continue
                                    else:
                                        i.id = new_id
                                        break
                                after_action()
                                continue
                            case '5':
                                return
                            case _:
                                print("Please enter 1, 2, 3, 4, or 5.")

                else:
                    pass
            
            if found == False:
                print("Please enter a valid ID.")
                continue
            else:
                pass

    def add_student(self):
        student_name = input("Enter name for new student:\n").strip()
        while True:
            student_level = input("Enter grade level (9th,10th,11th,12th) for new student:\n").strip()
            if student_level not in grade_levels:
                print("Please enter a grade level of 9th, 10th, 11th, or 12th.")
                continue

            student_id = input("Enter ID for new student:\n").strip()
            for i in self.catalog:
                if i.id == student_id:
                    print("There is already a student with that ID saved in your gradebook.")
                    continue
                else:
                    pass
            academic_standing = "N/A"
            create_student(student_name,student_id,academic_standing,student_level,grades=[])
    
    def remove_student(self):
        for i in self.catalog:
                print(f"Student Name: {i.name} | Student ID: {i.id}")
        while True:
            delete_student = input("Enter ID of student you want to remove.").strip()

            for i in self.catalog:
                if i.id == delete_student:
                    student_index = find_dict_index(self.catalog,"id",i.id)
                    self.catalog.pop(student_index)
                    print("Student succesfully removed.")
                    after_action
                    return
            
            print("That student could not be found.")
            continue

    def view_all(self):
        for i in self.catalog:
            print(i + f" | Letter Grade: {i.calculate_letter}")

        after_action()

    def find_average(self):
        class_grades = []
        for i in self.catalog:   
            for num in i:
                class_grades.append(num)

        class_sum = sum(class_grades)
        class_average = sum(class_sum)

        return class_average
    
    def find_high_low(self):
        sorted_catalog = sorted(self.catalog,key=lambda student: student.average)
        high_student = sorted_catalog[0]
        low_student = sorted_catalog[-1]
        return high_student,low_student