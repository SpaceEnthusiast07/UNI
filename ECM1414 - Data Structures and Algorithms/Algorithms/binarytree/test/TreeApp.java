import tree.*;

public class TreeApp {
    public static void main(String[] args) {
        // Check if the user has entered anything into the terminal
        if (args.length == 0) {
            System.out.println("ERROR: Please enter at least the root node for the tree.");
            System.exit(0);
        }

        // Add the root node to the tree
        Tree tree = new Tree(Integer.parseInt(args[0]));

        // If the user has entered any more nodes, add them
        if (args.length > 1) {
            for (int i = 1; i < args.length; i++) {
                tree.add(Integer.parseInt(args[i]));
            }
        }

        // Output the tree
        System.out.println(tree);
    }
}
