#-------------------------------------------------#
# Title: Working with Dictionaries
# Dev:   RRoot
# Date:  July 16, 2012
# ChangeLog: (Who, When, What)
#   RRoot, 11/02/2016, Created starting template
#   Alexandra, 11/12/2018, Added code to complete assignment 5
#   Alexandra, 11/12/2018, Added code to complete assignment 6
#https://www.tutorialspoint.com/python/python_dictionary.htm
#-------------------------------------------------#

#-- Data --#
# declare variables and constants
# objFile = An object that represents a file
# strData = A row of text data from the file
# dicRow = A row of data separated into elements of a dictionary {Task,Priority}
# strMenu = A menu of user options
# strChoice = Capture the user option selection

#-- Input/Output --#
# User can see a Menu (Step 2)
# User can see data (Step 3)
# User can insert or delete data(Step 4 and 5)
# User can save to file (Step 6)

class toDoList(object):
    fileName = None
    dictRows = {}

    def listFromFile(self):
        fileData = open(self.fileName, "r")
        lines = fileData.read().split('\n')
        fileData.close()
        for line in lines:
            try:
               task, priority = line.split(',')
               self.dictRows[task] = str(priority)
            except: #if there's no tasks already in the list then we can just move on
                pass
        
    def printList(self): #prints the tasks and priorities in the list
        for key in self.dictRows:
            print('Task: ',key, ',', 'Priority:',self.dictRows[key])

    def add(self, task, priority): #adds an item to the list
        self.dictRows[task] = priority

    def remove(self, toRemove): #removes an item from the list
        if toRemove.strip() in self.dictRows.keys():
            del self.dictRows[toRemove]
        else:
            print("The task you typed isn't in the list. Please try again.")
    
    def writeToFile(self): #writes the data to the file
        fileData = open(self.fileName, "w")
        for key in self.dictRows:
            fileData.write(key + ',' + self.dictRows[key] + '\n')
        fileData.close()
        print('List saved!')

newList = toDoList() 
newList.fileName = "C:\_PythonClass\Assignment05\ToDo.txt"

# Step 1 - Load data from a file
    # When the program starts, load each "row" of data 
    # in "ToDo.txt" into a python Dictionary.
    # Add the each dictionary "row" to a python list "table"
newList.listFromFile()
print(str(newList.dictRows))

# Step 2 - Display a menu of choices to the user
while(True):
    print ("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] --> "))
    print()#adding a new line

    # Step 3 -Show the current items in the table
    if (strChoice.strip() == '1'):
        newList.printList()
        
    # Step 4 - Add a new item to the list/Table
    elif(strChoice.strip() == '2'):
        task = input("Enter a new task:  ")
        priority = input("What is the priority of this task? (1: High, 2:Medium, 3:Low)  ")
        newList.add(task, priority)
        
    # Step 5 - Remove an item from the list/Table
    elif(strChoice == '3'):
        print("Which task do you wish to remove? ")
        print("Current List of Tasks: ")
        newList.printList()
        toRemove = input("Item to remove:")
        newList.remove(toRemove)

    # Step 6 - Save tasks to the ToDo.txt file
    elif(strChoice == '4'):
        newList.writeToFile()
              
    elif (strChoice == '5'):
        break #and Exit the program
    


