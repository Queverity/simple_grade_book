# CB 1st Student Class

from helper import *

# class Student:
    # def __init__(self):
        # attributes will be name, student_id, a grades list, academic standing, and grade level. grades_list will have a defualt value of an list with eight entries of 'N/A'

    # def __str__(self):
        # print student name, id, grade average, letter grade, academic standing, and grade level

    # def view_grades(self):
        # iterate through grades list and print items if not equal to 'N/A'
    
    # def calculate_average(self):
        # find both number and letter grade average (maybe also GPA)
        # go through student grades list, add up all items, divide by list length
        # take average and turn it into a letter grade

    # def find_standing(self):
        # take grade average, make a few if statements to find different things


    # def add_grade(self):
        # have user input grade
        # make sure grade is not above 100 or below 0
        # add grade to grades list and recalculate average and standing

    # def remove_grade(self):
        # go through grades list and print out each grade
        # have user input which grade they want to remove
        # if index does not exist, have user try again
        # if index does exist, pop grade from list and recalculate average and standing

# def create_student(name,id,grades):
    # create a student object using name and id, and grades if it is not empty
    # if bool(grades) != False:
        # student_object = Student(name,id,grades)
    # else:
        # student_object = Student(name,id)

class Student:
    def __init__(self,name,student_id,academic_standing,grade_level,average,grades_list = []):
        self.name = name
        self.student_id = student_id
        self.academic_standing = academic_standing
        self.grade_level = grade_level
        self.grades_list = grades_list
        self.average = average

    def __str__(self):
        return f"Student Name: {self.name} | Student ID: {self.id} | Academic Standing: {self.academic_standing} | Grade Level: {self.grade_level}"

    def view_grades(self):
        for i in self.grades_list:
            if i == 'N/A':
                pass
            else:
                print(f"{i}%")

    def calculate_average(self):
        grades_length = len(self.grades_list)
        grades_summed = sum(self.grades_list)

        grade_average = float(grades_summed / grades_length)

        return grade_average
    
    def calculate_letter(self):
        if self.average >= 94:
            return "A"
        elif self.average >= 90:
            return "A-"
        elif self.average >= 87:
            return "B+"
        elif self.average >= 84:
            return "B"
        elif self.average >= 80:
            return "B-"
        elif self.average >= 77:
            return "C+"
        elif self.average >= 74:
            return "C"
        elif self.average >= 70:
            return "C-"
        elif self.average >= 67:
            return "D+"
        elif self.average >= 64:
            return "D"
        elif self.average >= 61:
            return "D-"
        else:
            return "F"

    def find_standing(self,grade_average):
        if grade_average >= 90:
            return "Honor Roll"
        elif grade_average >= 80:   
            return "Good Standing"
        else:
            return "Needs Improvement"
        
    def add_grade(self):
        while True:
            new_grade = input("Enter grade you want to add, or type 'exit' to return to gradebook menu:\n").strip().lower()

            if new_grade == 'exit':
                return
            else:
                try:
                    new_grade = float(new_grade)
                except:
                    print("Please enter an actual number.")
                    after_action()
                    continue
                else:
                    if new_grade > 100 or new_grade < 0:
                        print("Please enter a number between 100 and 0.")
                        continue
                    else:
                        self.grades_list.append(new_grade)
                        print("Grade added!")
                        average = self.calculate_average()
                        self.academic_standing = self.find_standing(average)
                        after_action()
                        
    
    def remove_grade(self):
        while True:
            count = 0
            for i in self.grades_list:
                count += 1
                print(f"{count}. {i}")

            grade = input("Enter the number by the grade you want to remove:\n").strip()

            try:
                grade = int(grade)
            except:
                print("Please enter a valid number.")
            else:
                if grade > count - 1:
                    print("Please enter a valid number.")
                else:
                    self.grades_list.pop(grade)
                    print("Grade removed.")
                    self.average = self.calculate_average()
                    self.academic_standing = self.find_standing(self.average)
                    after_action()
                    return

                
def create_student(name,id,academic_standing,grade_level,grades):
    if bool(grades) == False:
        student_object = Student(name,id,academic_standing,grade_level)
    else:
        student_object  = Student(name,id,academic_standing,grade_level,grades)

    return student_object


