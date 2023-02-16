# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# CMiyake,2023.02.15,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"  # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""  # A menu of user options
strChoice = ""  # A Capture the user option selection

# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# TODO: Add Code Here
data = open(objFile, "w")  # open the file in write mode
dicHeader = {"Task": 'TASK', "When": "WHEN SHOULD THE TASK BE DONE?"}
dicRow = {"Task": "Make Dinner", "When": "5:00PM"}  # add a task
lstTable.append(dicHeader)
lstTable.append(dicRow)
data.write(dicHeader['Task'] + ':' + dicHeader['When'] + '\n')
data.write(dicRow['Task'] + ':' + dicRow['When'] + '\n')
data.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):

        read = open(objFile, "r")
        for dicRow in lstTable:
            print(dicRow['Task'], ':', dicRow['When'])
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        newRow = {}  # new dictionary for user input
        newRow['Task'] = input("Enter a Task: ")  # user input task
        newRow['When'] = input("When should this task be completed? ")
        lstTable.append(newRow)
        print() # adding a space
        # Show the updated table
        read = open(objFile, "r")
        for dicRow in lstTable:
            print(dicRow['Task'], ':', dicRow['When'])
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        lstTable.pop()
        print("The last task has been removed.\n")
        read = open(objFile, "r")
        for dicRow in lstTable:
            print(dicRow['Task'], ':', dicRow['When'])
        print()

        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        save = open(objFile, "w")
        for row in lstTable:
            save.write(row["Task"] + ':' + row["When"] + '\n')
        save.close()
        print("Tasks have been saved to file.")
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print("Good Bye")
        break  # and Exit the program

    else:
        print("Please input a valid option!")
