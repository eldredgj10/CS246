# Author: Jeanette Eldredge

from classFile import Items


# This function counts how many of each group there are. 
def howMany(choice):
    if choice == 1:
        global gItems 
        gItems = gItems + 1
    if choice == 2:
        global tItems
        tItems += 1
    if choice == 3:
        global oItems
        oItems += 1

# This function displays the list organized in each catagory
def display (listItems):
    if len(listItems) != 0:
        if gItems !=0:
            print("\nGroceries:\n --------------\n")  
            for item in listItems:
                if item.choice == 1:
                    print(item.name, "   ", item.amount)
        if tItems != 0:
            print("\nToilitries:\n--------------\n")
            for item in listItems:
                if item.choice == 2:
                    print(item.name, "   ", item.amount)
        if oItems !=0:
            print("\nOthers:\n--------------\n")
            for item in listItems:
                if item.choice == 3:
                    print(item.name, "   ", item.amount)

# This function organizes the list and writes it to a file.                  
def write(filename, listItems):
        newfile = open(filename, 'w')
        if gItems !=0:
            newfile.write("Groceries:\n--------------\n")
            for item in listItems:
                if item.choice == 1:
                    newfile.write(item.name)
                    newfile.write("   ")
                    newfile.write(str(item.amount))
                    newfile.write("\n")
        if tItems !=0:
            newfile.write("\nToilitries:\n --------------\n")
            for item in listItems:
                if item.choice == 2:
                    newfile.write(item.name)
                    newfile.write("   ")
                    newfile.write(str(item.amount))
                    newfile.write("\n")
        if oItems !=0:   
            newfile.write("\nOthers:\n --------------\n")
            for item in listItems:
                if item.choice == 3:
                    newfile.write(item.name)
                    newfile.write("   ")
                    newfile.write(str(item.amount))
                    newfile.write("\n")

# This function creates the list by gathering input from the user in a loop. Hitting enter will exit the function
def makinglist():
    while True:
        iteminput = input("\n \nEnter Item. Hit enter to stop list: ")
        if iteminput == '':
            break
        try:
            amount = int(input("How many do you need? "))
        except ValueError:
            print("Invalid response.")
            amount = int(input("Please enter a number: "))
        print("Is this item Groceries, Toilitries, or Other?")
        print("Type 1 for Groceries.")
        print("Type 2 for Toilitries.")
        print("Type 3 for Other.")
        try:
            choice = int(input())
        except ValueError:
            print("Invalid response.")
            choice = int(input("Please print a number: "))
        while choice != 1 and choice != 2 and choice != 3:
            print("Invalid response.")
            choice = int(input("Please print a number: "))
        howMany(choice)
        item = Items(iteminput,amount, choice)
        listItems.append(item)

#Initilizing variables
filename = ''
listItems = []
amount = 0
choice = 0
iteminput = ''
gItems = 0
tItems = 0
oItems= 0

#Beginning of the program
print("\n \n \nWelcome! I am here to help prepare your shopping list!")
makinglist() # Starts the make list loop

# This loop asks the user what they want to do with the new list created. They can either display the list,
# export the list into a file, add more to the list, or end the program.
while True:
    print("\n \n \nYou can now display your list, add more too your list, or export it in a new file.")
    print("Type 1 to display.\nType 2 to export file. \nType 3 to add more to your list.\nType 4 to stop.")
    whatsnext = input()
    while whatsnext != '1' and whatsnext != '2' and whatsnext != '3' and whatsnext != '4':
        print("Invalid response.")
        whatsnext = input("Please print a number: ")
    whatsnext = int(whatsnext)
    if whatsnext == 1:
        display(listItems)
    if whatsnext == 2:
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
        write(outputfile_name, listItems)
    if whatsnext == 3:
        makinglist()
    if whatsnext == 4:
        print("Thank you! Enjoy your shopping trip!")
        break
    
