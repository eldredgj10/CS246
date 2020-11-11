//Author: Jeanette Eldredge

import java.util.Scanner;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;

public class ToDoListMaker {
    public static String box = "🔳  ";
    public static String name = "";
    public static ArrayList<String> todo = new ArrayList<String>();
    public static Scanner input = new Scanner(System.in);

    public static void main(String[] args) {
        System.out.println("\nWelcome!\n Please enter the name of the list you want to create: ");
        name = input.nextLine();
        listMaker();
        String choice = "";
        boolean loop = true;
        while (loop) {
            System.out.println("\n \nChoose an option: \n Display list: 1\n Enter more into list: 2\n Export list: 3\n");
            choice = input.nextLine();
            if (choice.equals("1")) {
                display();
            } else if (choice.equals("2")) {
               listMaker();
            } else if (choice.equals("3")) {
                createFile();
                loop = false;
            }
            else{
                System.out.println("Invalid response.");
            }
        }
        input.close();
    }

    public static void display() {
        DateTimeFormatter date = DateTimeFormatter.ofPattern("MM/dd/yyyy HH:mm:ss");
        LocalDateTime dateCreated = LocalDateTime.now();
        System.out.println("\n");
        System.out.println(name + "\t" + (date.format(dateCreated)));
        System.out.println("------------------------------------------------------------");
        for (int i = 0; i < todo.size(); i++) {

            System.out.printf("%-50s %s\n",todo.get(i), box);
        }

    }

    public static void createFile() {
        DateTimeFormatter date = DateTimeFormatter.ofPattern("MM/dd/yyyy HH:mm:ss");
        LocalDateTime dateCreated = LocalDateTime.now();
        File list = new File(name + ".txt");
        try {
            if (list.createNewFile()) {
                System.out.println("New File Created!");
                System.out.println(name + ".txt");
            } else {
                System.out.println("Please rename list: ");
                Scanner input = new Scanner(System.in);
                name = input.nextLine();
                input.close();
            }
        } catch (IOException e1) {
            e1.printStackTrace();
        }
        try 
        {
            FileWriter export = new FileWriter(name + ".txt");
            PrintWriter writer= new PrintWriter(export);
            writer.print(name + "\t" + (date.format(dateCreated))+ "\n");
            writer.print("------------------------------------------------------------\n");
            for (int i = 0; i < todo.size(); i++) 
            {
                writer.printf("%-50s %s\n",todo.get(i), box);
            }
            writer.close();
        }
        catch (IOException e)
        {
            e.printStackTrace();
        }
        System.out.println("\nList complete!");
    }
    public static void listMaker()
    {
        System.out.println("\nEnter things needed to be done. Enter 'q' when done. ");
        while(input.hasNext())
        {
            String in = input.nextLine();
            if(!in.equalsIgnoreCase("q"))
            {
                todo.add(in);
            }
            else{break;}
        }
    }
}