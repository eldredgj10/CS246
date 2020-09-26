# Author: Jeanette Eldredge
# Project: Game Time!

from random import randint #inporting specific function from random library as example in python book

print("\nGame time!")

stillPlay = " " # Loop the code initialized
bool = True

while stillPlay != 'N': # continuing the loop of the program if the game is not finished
    
    dice = " " # Name of dice needed initialized
    numRolls = 1 # number of a specific dice needed to roll initialized
    randomRoll = 0 # Value of each roll initialized
    listOfValues = [] # list of Roll values initialized
    listOfDice = [] # list of dice input strings
    listOfRolls =[] #List of how many dice each needs to roll
    sumRolls = 0 # Sum of the dice initialized

# While loop promps user and checks for errors in the input it recieves
    while True: 
        print("\nD4, D6, D8, D10, D12, D20, D100")
        dice = input("Please enter which dice you need! Enter 'Done' when finished: ")
        dice = dice.upper() # Set the input uppercase for comparison.
        
        # Checks that the correct input is put in to the terminal.
        while dice != 'D4' and dice != 'D6' and dice != 'D8' and dice != 'D10' and dice != 'D12' and dice != 'D20' and dice != 'D100' and dice != 'DONE':
            dice = input("Sorry. Invalid response. Please enter D4, D6, D8, D10, D12, D20, or D100. Enter 'Done' if finished: ")
            dice = dice.upper()
        
        # Quites While loop to begin the calculations.
        if dice == "DONE":
            break

        # Adds the dice name to the list of Dice.
        listOfDice.append(dice)
        
        # Checks to be sure that a number was entered.
        try:
            numRolls = int(input("How many do you need?: "))
        except ValueError:
             numRolls = int(input("Invalid response. Please enter an number: "))
        
        # Adds number to the list of Rolls.
        listOfRolls.append(numRolls)

    index = 0 # Initializes Index to access the number of rolls in the List Of Rolls for each die.

    # For loop goes through list of Dice needed and rolls the correct amount for each dice input and adds them to a list of Values
    for count in listOfDice: 
        
        if count == "D4":
            for counter in range(0,listOfRolls[index]):
                randomRoll = randint(1,4)
                listOfValues.append(randomRoll)
       
        if  count== "D6":
            for counter in range(0,listOfRolls[index]):
                randomRoll = randint(1,6)
                listOfValues.append(randomRoll)
       
        if count == "D8":
            for counter in range(0,listOfRolls[index]):
                randomRoll = randint(1,8)
                listOfValues.append(randomRoll)
        
        if count == "D10":
            for counter in range(0,listOfRolls[index]):
                randomRoll = randint(1,10)
                listOfValues.append(randomRoll)
        
        if count == "D12":
            for counter in range(0, listOfRolls[index]):
                randomRoll = randint(1,12)
                listOfValues.append(randomRoll)

        if count == "D20":
            for counter in range(0,listOfRolls[index]):
                randomRoll = randint(1,20)
                listOfValues.append(randomRoll)

        if count == "D100":
            for counter in range(0,listOfRolls[index]):
                randomRoll = randint(1,100)
                listOfValues.append(randomRoll)
        
        index = index +1 # loops the index

# Displays the list of rolled Values from previous loop
    print("\nRolled dice Values:")
    print(listOfValues)

# Adds the list of values together and sets it equal to sumRolls
    for display in listOfValues: 
        sumRolls = sumRolls + display

# Displays the total amount of the roll
    print("\nSum of Dice:")
    print(sumRolls)
    sumRollsOriginal = sumRolls
# Adds, subtracts, or divides to do appropriate modifiers.    
    while True:
        modify = input("\nModifiers? +, -, /, or enter to skip calculation: ")
        while modify != '+' and modify != '-' and modify != '/' and modify != '':
            modify = input("Invalid response. Please type +, -, /, or hit enter to skip calculation: ")
            
        if modify != '':
            try:
                amount = int(input("How much? "))
            except ValueError:
                amount = int(input("Please enter a valid number: "))
            
            # Adds the modifier
            if modify == '+':
                sumRolls = sumRolls + amount
                print(sumRolls)
            
            # Subtracts the modifier
            if modify == '-':
                sumRolls = sumRolls - amount
                print(sumRolls)

            # Divides the modifier
            if modify == '/':
                sumRolls = int(sumRolls / amount)
                print(sumRolls)

            # Asks if it needs to be modified more.
            modifycon = input("Modify more? Y/N ")
            modifycon = modifycon.upper()
            while modifycon != 'N' and modifycon != 'Y': # Checks for correct input
                modifycon = input("Invalid Response. Please enter Y or N:")
                modifycon = modifycon.upper()
            if modifycon == 'N':
                break
            else:
                continue
        if modify == '':
                break

    # Displays new sum that includes the modifiers.
    if modify != '':
        print("\nModified! New total:")
        print(sumRolls)
    if modify == '' and sumRolls != sumRollsOriginal:
        print ("\nNo more Modifications.")
        print(sumRolls)
# Clear the lists to prepare for the new roll
    listOfDice.clear() 
    listOfRolls.clear()
    listOfValues.clear()

# Check to see if the player still needs the dice roller and continues the loop if so. Quits the program if not.
    stillPlay=input("\nStill playing? Y/N  ")
    stillPlay = stillPlay.upper() # Uppercase for comparison

    # Checks for correct input
    while stillPlay != 'N' and stillPlay != 'Y':
        stillPlay = input("Invalid response. Type Y or N: ")
    if stillPlay == "N" or stillPlay == "n":
        bool = False
        print("Thanks for playing! Huzzah Magic Powers!")
    else:
        stillPlay = "Y"
exit()
