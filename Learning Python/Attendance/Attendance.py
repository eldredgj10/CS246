# Author: Jeanette Eldredge
from attendFunctions import choicehandle, studentattend, welcome, whoAbsent

#main control code That runs the program
welcome() # Beginning program and set up
studentattend() # Adds students to the class
whoAbsent() # Sees who is here and who isn't

# Loop checks to see what the teacher wants done with that information and checks to be sure that a valid choice 
# was entered.
while True:
    print("\nWhat would you like to do?")
    print("Type 1 to see who is here.")
    print("Type 2 to see who is absent.")
    print("Type 3 to add more students that arrived.")
    print("Type 4 to export absent list in a txt file.")
    print("Type 5 to export present list in a txt file.")
    print("Type 6 to end program.\n")
    choice = int(input())
    print('\n')
    while choice != 1 and choice != 2 and choice != 3 and choice != 4 and choice != 5 and choice != 6:
        choice = int(input("Please enter valid number: "))
    choicehandle(choice)
    if choice == 6:
        print("\nThank you! Have a wonderful day!")
        break

        

    