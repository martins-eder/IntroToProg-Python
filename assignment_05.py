# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   Eder Martins,8/28/2024,Created Script
# ------------------------------------------------------------------------------------------ #

import re  # Importing the regular expression module

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.csv"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
csv_data: str = ''  # Holds combined string data separated by a comma.
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.
student_data: dict = {} # dictionary rows of student data
students: list = []  # a two-dimensional list table (a list of dictionary rows)
student_info: list = []   # Temporary list to hold data read from file.
name_pattern = re.compile(r"^[A-Za-z-]+$") # Regular expression pattern to validate names (only letters and hyphens)

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
try:
    file = open(FILE_NAME, "r") # Open file in read mode
    for row in file.readlines():
        # Transform the data from the file into a dictionary
        student_info = row.strip().split(',')
        student_data = {"First Name": student_info[0], "Last Name": student_info[1], "Course": student_info[2]}
        # Load it into our collection (list of dictionaries)
        students.append(student_data)
    file.close()
except FileNotFoundError:
    print(f"{FILE_NAME} not found. Starting with an empty list.")
except Exception as e:
    print(f"An error occurred while reading the file: {e}")

# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        try:
            student_first_name = input("Enter the student's first name: ").strip()
            if not student_first_name:
                raise ValueError("First name cannot be empty.")
            if not name_pattern.match(student_first_name):
                raise ValueError("First name cannot contain numbers, spaces, or special characters "
                                 "(except hyphens).")

            student_last_name = input("Enter the student's last name: ").strip()
            if not student_last_name:
                raise ValueError("Last name cannot be empty.")
            if not name_pattern.match(student_last_name):
                raise ValueError("Last name cannot contain numbers, spaces, or special characters "
                                 "(except hyphens).")

            course_name = input("Please enter the name of the course: ").strip()
            if not course_name:
                raise ValueError("Course name cannot be empty.")

            # Create a dictionary for student data
            student_data = {"First Name": student_first_name, "Last Name": student_last_name, "Course": course_name}
            students.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")

        except ValueError as e:
            print(f"Input Error: {e}")
        continue

    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        print("-"*50)
        for student in students:
            print(f"Student {student['First Name']} {student['Last Name']} is enrolled in {student['Course']}")
        print("-"*50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, "w")
            for student in students:
                csv_data = f"{student['First Name']},{student['Last Name']},{student['Course']}\n"
                file.write(csv_data)
            file.close()
            print("The following data was saved to file!")
            for student in students:
                print(f"Student {student['First Name']} {student['Last Name']} is enrolled in {student['Course']}")
        except Exception as e:
            print(f"An error occurred while writing to the file: {e}")
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
