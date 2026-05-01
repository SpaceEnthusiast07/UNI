class TreeNode {
	float x;
	TreeNode left;
	TreeNode right;
	TreeNode(float x) {
		this.x = x;
		this.left = null;
		this.right = null;
	}
}

public class BSTNodeCount {
	public static void main(String[] args) {
		// Create a BST
		TreeNode tree = new TreeNode(3.2f);
		TreeNode n2 = new TreeNode(1.6f);
		TreeNode n3 = new TreeNode(9.2f);
		TreeNode n4 = new TreeNode(0.3f);
		TreeNode n5 = new TreeNode(1.9f);
		TreeNode n6 = new TreeNode(6.1f);
		TreeNode n7 = new TreeNode(12.4f);
		tree.left = n2;
		tree.right = n3;
		n2.left = n4;
		n2.right = n5;
		n3.left = n6;
		n3.right = n7;

		System.out.println("======================");
		System.out.println("=== BST Node Count ===");
		System.out.println("======================");
		System.out.println("Info: Count the number of nodes in this BST that adhere to a certain condition.");
		System.out.println("Condition: The value at the node must be between 1.3 and 5.6.\n");

		System.out.printf("Brute Force Count: %d\n", count(tree, 1.3f, 5.6f));
		System.out.printf("Efficient Count:   %d\n", countEfficiently(tree, 1.3f, 5.6f));
	}

	public static int count(TreeNode T, float x0, float x1) {
		// If this node is null, there are no nodes below it
		if (T == null) {
			return 0;
		}
		// Recursively traverse down the left and right subtrees to count the nodes
		int leftCount = count(T.left, x0, x1);
		int rightCount = count(T.right, x0, x1);
		// Check if this node adheres to the condition
		if (T.x > x0 && T.x < x1) {
			return 1 + leftCount + rightCount;
		}
		return leftCount + rightCount; 
	}

	public static int countEfficiently(TreeNode T, float x0, float x1) {
		// If this node is null, there are no nodes below it
		if (T == null) {
			return 0;
		}

		// Declare the counts for the left and right subtrees
		int leftCount = 0;
		int rightCount = 0;

		// If this node's value (T.x) is below the lower bound (x0), the entire left subtree can be skipped
		// as all those values are less than this node's value
		if (T.x <= x0) {
			// Only check the right subtree
			rightCount = countEfficiently(T.right, x0, x1);
			return rightCount;
		}
		// If this node's value (T.x) is above the upper bound (x1), the entire right subtree can be skipped
		// as all those values are greater than this node's value
		else if (T.x >= x1) {
			// Only check the left subtree
			leftCount = countEfficiently(T.left, x0, x1);
			return leftCount;
		}
		// Otherwise, this node's value must be within the two bounds (x0 and x1). Therefore, we need to check both subtrees
		else {
			// Check both subtrees
			leftCount = countEfficiently(T.left, x0, x1);
			rightCount = countEfficiently(T.right, x0, x1);
			return 1 + leftCount + rightCount;
		}
	}
}
