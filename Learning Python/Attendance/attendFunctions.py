# Author: Jeanette Eldredge
import os

# Initializing global variables that most functions use or have access to.
inputfile_name = ''
outputfile_name = ''
studentsTotal = 0
inputfilelist =[]
attendancelist = []
absentList = []

# This is the beginning of the program. It asks for the path of the class list file and calls numbofstudents to calculate
# how many members are in the class. This function sets up the program.
def welcome():
    print("\n \n \n \nWelcome to the attendance documentery program!")
    print("\nThis program works with a txt file of all the students names.")
    inputfile_name = input("Please enter the path of your class list txt file: ")
    print("Calculating amount of students from file...")
    studentsTotal= numbofstudents(inputfile_name)
    print(studentsTotal)
    print("\nThank you! Program ready for your students.")
    
# This function checks to see if the file is existant. If it is then it will open the file put
# each line into a list of class students. It will also count how many students there are. If the
# File doesn't exist then it will ask for a new file path   
def numbofstudents(inputfile_name):
    os.path.isfile(inputfile_name)
    while os.path.isfile(inputfile_name) == False:
        print("Invalid file path.")
        inputfile_name = input("Please enter the path of your class list txt file: ")

    inputfile = open(inputfile_name, "r")

    numberStudents = 0
    for line in inputfile:
        line = line.strip("\n")
        numberStudents += 1
        inputfilelist.append(line)
    inputfile.close()
    return numberStudents


# This function will loop through as the students each enter their name and check to be sure their
# name is on the list imported from the class list. If it is the name is added to the present list.
def studentattend():
    loopcontinue = ''
    for count in inputfilelist:
        studentName = input("\nPlease enter your First and Last name: ")
        loop = 0
        for student in inputfilelist:
            if studentName == student:
                loop = 1
                break
            else:
                loop = 0
        while loop == 0:
                print("That name isn't in the class list.")
                studentName = input("Please input First and Last name: ")
                for student in inputfilelist:
                    if studentName == student:
                         loop = 1
                         break
                    else:
                         loop = 0

        attendancelist.append(studentName)
        for name in absentList:
            if studentName == name:
                absentList.remove(studentName)

        print("Welcome to class!")
        loopcontinue = input("\n \nAre there more students? Y/N ")
        while loopcontinue.upper() != 'N'  and loopcontinue.upper() != 'Y':
            print("Invalid response.")
            loopcontinue = input("Are there more students? Y/N ")
        if loopcontinue.upper() == 'N':
            return

# This function will compare the list of people attending and the list of the class students.
# If the student in the list of the class students isn't found in the attendance list then the 
# name is added to the absent list.
def whoAbsent():
    for who in inputfilelist:
        isthere = 0
        for student in attendancelist:
            if student == who:
                isthere = 1
                break
            if student != who:
                isthere = 0
        if isthere == 0:
            absentList.append(who)


# Functions ask for name of exported file and checks to be sure that it will export a txt file. It then
# creates a file with that name and then writes the List of students absent to the file.
def exportAbsent():
    filename = input("Please name your absent export file. Do not include '.txt': ")
    for letter in filename:
        if letter == '.':
            filenamecheck = 0
            break
        else: 
                filenamecheck = 1
    while filenamecheck == 0:
        filename = input("Enter valid name with no '.txt' : ")
        for letter in filename:
            if letter == '.':
                filenamecheck = 0
                break
            else:
                filenamecheck = 1

    outputfile_name = filename + '.txt'
    outputfile = open(outputfile_name, 'w')
    outputfile.write("Absent list:\n")
    for who in absentList:
        outputfile.write(who)
        outputfile.write("\n")
    outputfile.close()

# Functions ask for name of exported file and checks to be sure that it will export a txt file. It then
# creates a file with that name and then writes the List of students present to the file.
def exportPresent():
    filename = input("Please name your absent export file. Do not include '.txt': ")
    for letter in filename:
        if letter == '.':
            filenamecheck = 0
            break
        else: 
                filenamecheck = 1
    while filenamecheck == 0:
        filename = input("Enter valid name with no '.txt' :")
        for letter in filename:
            if letter == '.':
                filenamecheck = 0
                break
            else:
                filenamecheck = 1

    outputfile_name = filename + '.txt'
    outputfile = open(outputfile_name, 'w')
    outputfile.write("Attendance list:\n")
    for who in attendancelist:
        outputfile.write(who)
        outputfile.write("\n")
    outputfile.close()


# The function handles the different choices and calls their respective functions for each choice. This function
# calls studentattend(), exportAbsent(), and exportPresent(). It also ends the program when user chooses too.
def choicehandle(choice):
    if choice == 1:
        print(attendancelist)
    if choice == 2:
        print(absentList)
    if choice == 3:
        studentattend()
    if choice == 4:
        exportAbsent()
    if choice == 5:
        exportPresent()
    if choice == 6:
        return