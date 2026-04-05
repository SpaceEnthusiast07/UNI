import java.util.Scanner;
import java.io.FileWriter;
import java.io.IOException;
import java.io.BufferedWriter;

public class IOApp {
    public static void main(String[] args) {
        try {
            // Instantiate a Scanner object
            Scanner keyboardInput = new Scanner(System.in);

            // Display the title of this Java app
            System.out.println("==================\n== Java IO Test ==\n==================");

            // Ask the user for thier name
            System.out.print("What is your name? ");
            String usersName = keyboardInput.nextLine();

            // Output their name
            System.out.printf("Hello %s\n", usersName);

            // Ask the user for the name of the file
            System.out.print("Give a name to the new file (no extension): ");
            String fileName = keyboardInput.nextLine();

            // Ask the user what they want to insert into the file
            System.out.print("Type something to add to the file: ");
            String userInput = keyboardInput.nextLine();

            // Instantiate a buffered writer object to append data to the file
            BufferedWriter charWriter = new BufferedWriter(new FileWriter(String.format("%s.txt", fileName), true));
            
            // Construct the contents to add
            String contentsToAdd = String.format("%s added: \"%s\"", usersName, userInput);

            // Append this data to the text file
            charWriter.write(contentsToAdd);

            // Always close the IO streams
            charWriter.close();
            keyboardInput.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}