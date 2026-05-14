import java.util.Scanner;

public class TaskSchedulerApp {
    public static void main(String[] args) {
        // Tracks if the user wants to exit the application
        boolean exitApp = false;

        // Create a new priority queue
        PriorityQueue queue = new PriorityQueue(10);

        // Create the console input object
        Scanner in = new Scanner(System.in);

        // Declare the variables used in the app's main loop
        String userInput;

        // Allows the app to run continuously
        while (exitApp == false) {
            outputAppTitle();

            // Get the user's input
            System.out.print("> ");
            userInput = in.nextLine();

            // Analyse the user's input
            analyseUserInput(userInput);



            // Close the input stream
            in.close();
            exitApp = true;
        }
    }

    public static void outputAppTitle() {
        System.out.printf("%s\n====%sTask Scheduler%s====\n%s\n", ("=".repeat(58)), (" ".repeat(18)), (" ".repeat(18)), ("=".repeat(58)));
        System.out.println("A - Add Task | E - Extract Next Task | H - Help | Q - Quit\n");
    }

    /**
     * Analyses the user's input, then performs the requested operation, or outputs an error message.
     * @param userInput The user's input.
     */
    public static void analyseUserInput(String userInput) {
        //
    }
}