import tree.*;

public class TreeApp {
    public static void main(String[] args) {
        // Create a new tree
        Tree tree = new Tree(null, 3);

        // Add to more nodes
        tree.add(4);
        tree.add(1);

        // Ouput the tree
        System.out.println(tree);
    }
}
