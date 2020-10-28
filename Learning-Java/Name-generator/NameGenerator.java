import java.util.Scanner;

import java.io.File;
import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Random;

public class NameGenerator {
    public static ArrayList<String> female = new ArrayList<String>();
    public static ArrayList<String> male = new ArrayList<String>();
    public static ArrayList<String> lastname = new ArrayList<String>();

    public static void main(String[] args){
        Scanner userInput = new Scanner(System.in);
        System.out.println("\nWelcome to Name generator!\n");

        System.out.println("Would you like a male, female, or last name?\n");

        String gender = userInput.nextLine();
        gender = gender.toUpperCase();

        while (!gender.equals("MALE") && !gender.equals("FEMALE") && !gender.equals("LAST")){
            System.out.println("Invalid response. Please enter 'male' or 'female': " );
            gender = userInput.nextLine();
            gender = gender.toUpperCase();
        }
        System.out.println("\n");
        try {
            importlists();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        System.out.println("Hit 'g' to continue generating names. Type 'q' to quit.\n");
        generatename(gender);

        userInput.close();

    }
    
    public static void importlists() throws FileNotFoundException {
        Path list1 = Paths.get("C:/Users/Jeanette/Git/CS246/Learning-Java/Name-generator/malenames.txt");
        Path list2 = Paths.get("C:/Users/Jeanette/Git/CS246/Learning-Java/Name-generator/femalenames.txt");
        Path list3 = Paths.get("C:/Users/Jeanette/Git/CS246/Learning-Java/Name-generator/Lastnames.txt");
        
        Scanner malelist = new Scanner(new File(list1.toString()));
        while(malelist.hasNext()){
            male.add(malelist.next());
        }
        malelist.close();

        Scanner femalelist = new Scanner(new File(list2.toString()));
        while(femalelist.hasNext()){
            female.add(femalelist.next());
        }
        femalelist.close();

        Scanner lastlist = new Scanner(new File(list3.toString()));
        while(lastlist.hasNext()){
            lastname.add(lastlist.next());
        }
        lastlist.close();
    }

    public static void generatename(String gender){
        Random rand = new Random();
        int name = rand.nextInt(1000);
        if(gender.equals("MALE"))
        {
            System.out.println(male.get(name));
        }

        if(gender.equals("FEMALE"))
        {
            System.out.println(female.get(name));
        }

        if(gender.equals("LAST"))
        {
            System.out.println(lastname.get(name));
        }
        
        Scanner input = new Scanner(System.in);
        String enter = " ";

        enter = input.next();
        while(!enter.equalsIgnoreCase("g") && !enter.equalsIgnoreCase("q"))
        {
            System.out.println("Invalid response. Type 'q' or 'g': ");
            enter = input.next();
        }
        if (enter.equals("q") || enter.equals("Q"))
        {
            System.out.println("Thank you!");
        }
        else if (enter.equalsIgnoreCase("g"))
        {
            generatename(gender);
        }

        input.close();
    }

}