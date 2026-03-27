# CB 1st Gradebook Class

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

    # find_average(self):
        # go through catalog, and add each grade in each students list to one big list
        # sum that list and divide by length to find average

    # find_high_low(self):
        # use lambda function to sort catalog list
        # highest will be last index, lowest will be first index (sort based on average)

# def initialize_catalog(students):
    # iterate through students list after loading from CSV and add them one by one to the catalog
    # okay so actually since you can save lists to CSVs, just set it to that

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
                    print(f"How would you like to edit student {self.id}?")
                else:
                    pass
            
            if found == False:
                print("Please enter a valid ID.")
                continue
            else:
                pass

