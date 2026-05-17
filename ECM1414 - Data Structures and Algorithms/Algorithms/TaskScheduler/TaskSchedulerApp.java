import java.util.InputMismatchException;
import java.util.Scanner;

public class TaskSchedulerApp {
    public static void main(String[] args) throws InterruptedException {
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
            System.out.print("\033[H\033[2J");
            System.out.flush();
            outputAppTitle();

            // Ask for the users input
            userInput = in.nextLine();

            // Analayse this input to perform the requested task
            analyseUserInput(userInput, queue);

            
            //exitApp = true;
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
    public static void analyseUserInput(String userInput, PriorityQueue queue) throws InterruptedException {
        // Split the string at each space
        String[] segmentedInput = userInput.split(" ");

        // Convert the first character to lowercase
        segmentedInput[0] = segmentedInput[0].toLowerCase();

        // Match the first character to a key operation character
        switch (segmentedInput[0]) {
            case "a": addTask(queue, segmentedInput); break;
            case "e": extractNextTask(queue); break;
            case "h": displayHelpPage(); break;
            case "q": System.exit(0); break;
            default: System.out.println("Enter \'H\' for input help."); Thread.sleep(1500);
        }
    }

    /**
     * Parses the user's input and adds the requested task to the priority queue.
     * @param queue The priority queue that the new task is going to be added to.
     * @param segmentedInput The segmented user input containing the data about the new task to add.
     */
    public static void addTask(PriorityQueue queue, String[] segmentedInput) throws InterruptedException {
        Scanner in = new Scanner(System.in);

        try {
            // Ask the user for the task details
            System.out.print("Priority: ");
            int priority = in.nextInt();
            in.nextLine();
            System.out.print("Task Title: ");
            String title = in.nextLine();
            System.out.print("Task Description: ");
            String description = in.nextLine();

            // Add this new node to the queue
            queue.insert(new TaskNode(priority, title, description));
            // Output success message
            System.out.println("New task added.");
            // Give the user time to read the message
            Thread.sleep(1500);
        }
        catch (NumberFormatException e) {
            System.out.println("Invalid priority or value entered.");
        }
        catch (InvalidPriorityException e) {
            System.out.println("Invalid priority.");
        }
        catch (InputMismatchException e) {
            System.out.println("Please enter an integer for the priority.");
        }
    }
    
    /**
     * Extracts the next task to perform.
     * @param queue The priority queue containing the various tasks.
     */
    public static void extractNextTask(PriorityQueue queue) throws InterruptedException {
        TaskNode extractedNode = queue.extractMin();

        if (extractedNode == null) {
            Thread.sleep(1500);
        }
        else {
            // Output this task
            System.out.printf("Extracted Task:\n - Priority = %d\n - Title = %s\n - Description = %s\n", extractedNode.getPriority(), extractedNode.getTitle(), extractedNode.getDescription());

            System.out.println("\nPress enter to continue...");
            Scanner inTemp = new Scanner(System.in);
            inTemp.nextLine();
        }
    }

    public static void displayHelpPage() {
        System.out.print("\033[H\033[2J");
        System.out.flush();
        outputAppTitle();

        System.out.println("\nAdd Task Format: A\n - priority = the priority for the new task\n - title = the title of the task\n - description = the description for the task\n");
        System.out.println("\nExtract Next Task: E\n - removes and displays the next task to complete from the queue\n");
        System.out.println("\nExtract Next Task: Q\n - quits the application\n");

        System.out.println("\nPress enter to continue...");
        Scanner inTemp = new Scanner(System.in);
        inTemp.nextLine();
    }
}