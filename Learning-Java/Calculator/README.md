# Overview

This program is a simple calculator that can handle two number equations. It supports adding, subtracting, 

# Development Environment

* Visual Studio Code 
* Java 11
* github
* git

# Execution

To execute the code hit run in visual studio code or on your JAVA coding software.


## Beginning and setup
The beginning welcomes the user to the calculator program and then it begins the loop code that asks for 2 numbers and a symbol.

![Beginning and first choice](Beginningandprompt.JPG)

## Number input
The prompt accepts any type of number because it is stored as a float in the program. This means that the numbers could be real numbers and decimals.
The program handles the display of the numbers according to their remainders. For example, If 10.0 is inputed the computer will write it as 10. This is shown in the displays of the equation.


## Choice selection
After entering the numbers in the prompt, the next prompt asks for a symbol that represents the type of math the computer needs to do. The symbols are +, -, *, and /. 

Symbol + :

![Symbol +](adding.JPG)

Symbol - :

![Symbol -](subtracting.JPG)

Symbol * :

![Symbol *](multiply.JPG)

Symbol / :

![Symbol /](divide.JPG)

## Continuing the loop

After completing one prompt, the program will ask if the user would like to continue calculating. The user can type Y or N.

Typing Y will continue the program and redisplay the prompt.

![Continuing the loop](Y.JPG)

Typing N will end the program.

![Ending the program](N.JPG)

## Protection
The number, symbol, and the loop input choices are protected to be sure that the correct input is put in. There is one bug on number input error check I am trying to fix.
![Protection in the number](Protectiononnum.JPG)
![Protection in code](Protectiononinput.JPG)


# Useful Websites and other Resources
* 