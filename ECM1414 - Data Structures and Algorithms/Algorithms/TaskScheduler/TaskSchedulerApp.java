import java.util.Scanner;

public class TaskSchedulerApp {
    public static void main(String[] args) {
        // Tracks if the user wants to exit the application
        boolean exitApp = false;

        // Create a new priority queue
        PriorityQueue queue = new PriorityQueue(10);

        // Create the console input object
        Scanner in = new Scanner(System.in);

        // Create the home page
        Page homePage = new Page("Task Scheduler", "A - Add Task | E - Extract Next Task | H - Help | Q - Quit");

        // Declare the variables used in the app's main loop
        String userInput;

        // Allows the app to run continuously
        while (exitApp == false) {
            System.out.println(homePage);

            
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
        // Split the string at each space
        String[] segmentedInput = userInput.split(" ");

        // Convert the first character to lowercase
        segmentedInput[0] = segmentedInput[0].toLowerCase();

        // Match the first character to a key operation character
        switch (segmentedInput[0]) {
            case "a": addTask(segmentedInput); break;
            case "e": break;
            case "h": break;
            case "q": break;
            default: throw new InvalidOperationInput("Enter \'H\' for input help.");
        }
    }

    /**
     * Parses the user's input and adds the requested task to the priority queue.
     * @param queue The priority queue that the new task is going to be added to.
     * @param segmentedInput The segmented user input containing the data about the new task to add.
     */
    public static void addTask(PriorityQueue queue, String[] segmentedInput) {
        //
    }
    
    /**
     * Extracts the next task to perform.
     * @param queue The priority queue containing the various tasks.
     */
    public static void extractNextTask(PriorityQueue queue) {
        //
    }

    public static void displayHelpPage() {
        //
    }
}