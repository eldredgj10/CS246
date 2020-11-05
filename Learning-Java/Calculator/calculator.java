// Author: Jeanette Eldredge

import java.util.Scanner;

public class calculator{
    public static float number = 0;
    public static float secondnumber = 0;
    public static String symbol;
    public static void main(String[] args) throws InterruptedException {
        int errorCheck = 1;
        float solved =0;
        System.out.println("\nWelcome to calculator!");
        Scanner input = new Scanner(System.in);
        // Loop goes through and asks the user for 2 numbers and a symbol, then calls the appropriate function.
        while(errorCheck == 1){
            String error = "";
            System.out.println("Enter two numbers: ");
            if(input.hasNextFloat())
            {
                number = input.nextFloat();
                error = input.next();
            }
            else{
                while(!input.hasNextFloat()){
                    System.out.println("Invalid response. ");
                    error = input.next();
                }
                number = input.nextFloat();
            }
            if(input.hasNextFloat())
            {
                secondnumber = input.nextFloat();
            }
            else{
                while(!input.hasNextFloat()){
                    System.out.println("Invalid response. ");
                    error = input.next();
                }
                secondnumber = input.nextFloat();
            };
            System.out.print("Enter +, -, *, / and hit enter: ");
            symbol = input.nextLine();
            while(!symbol.equals("+") && !symbol.equals("-") && !symbol.equals("*") && !symbol.equals("/")){
                System.out.println("Please enter a correct symbol: ");
                symbol = input.next();
            }
            if (symbol.equals("+"))
            {
                solved = adding();
                errorCheck =0;
            }
            else if (symbol.equals("-"))
            {
                solved = subtracting();
                errorCheck =0;
            }
            else if (symbol.equals("*"))
            {
                solved = multiply();
                errorCheck =0;
            }
            else if (symbol.equals("/"))
            {
                solved = divide();
                errorCheck =0;
            }
            else 
            {
                System.out.println("I'm sorry. I didn't understand. Please enter again: ");
                errorCheck = 1;
                continue;
            }

            display(solved);

            System.out.println("\nCalculate more? Enter Y or N:");
            String contLoop = "";
            while(!input.hasNext() );
            if (input.hasNext())
            {
                contLoop = input.next(); 
            }
            while(!contLoop.equalsIgnoreCase("Y") && !contLoop.equalsIgnoreCase("N"))
            {
                System.out.println("Please enter Y or N:  ");
                contLoop = input.next();
            }
            if(contLoop.equalsIgnoreCase("Y"))
            {
                errorCheck = 1;
            }
            else{
                break;
            }
        } 
        System.out.println("Calculation complete!");
        input.close();

    }

    /*display(solved) takes the answer from main and displays the equation and the answer.*/
    
    public static void display(float solved) {
        
        // Displays the equation correctly depending on if the numbers are an integer number or a float number.
        if((number % 2 == 0 ) && (secondnumber % 2 != 0)){
            System.out.print("Equation: \n \t" + (int)number + " " + symbol + " " + secondnumber);
        }
        else if ((number % 2 != 0 ) && (secondnumber % 2 == 0)){
            System.out.print("Equation: \n \t" + number + " "+ symbol + " " + (int)secondnumber);
        }
        else if ((number % 2 == 0 ) && (secondnumber % 2 == 0)){
            System.out.print("Equation: \n \t" + (int)number + " " + symbol + " " + (int)secondnumber);
        }
        else {
            System.out.print("Equation: \n \t" + number + " " + symbol + " " + secondnumber);
        }

        // Displays the solution depending on whether it is an integer or a float.
        if(solved % 2 == 0 ){
            System.out.print(" = " + (int)solved);
        }
        else
        {
            System.out.print(" = " + solved);
        }
    }

    // Adding() adds the two numbers together and return the answer.
    public static float adding(){ 
        float answer = 0;
        answer = number + secondnumber;
        return answer;
    }

    // subtracting() subtracts the two numbers together and return the answer.
    public static float subtracting(){ 
        float answer = 0;
        answer = number - secondnumber;
        return answer;
    }

    // multiply() multiplies the two numbers together and return the answer.
    public static float multiply(){
        float answer = 0;
        answer = number * secondnumber;
        return answer;
    }

    // divide() divides the two numbers together and return the answer.
    public static float divide(){ 
        float answer = 0;
        answer = number / secondnumber;
        return answer;
    }
}