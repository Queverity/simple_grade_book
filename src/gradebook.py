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

    # find_average(self):
        # go through catalog, and add each grade in each students list to one big list
        # sum that list and divide by length to find average

    # find_high_low(self):
        # use lambda function to sort catalog list
        # highest will be last index, lowest will be first index (sort based on average)
