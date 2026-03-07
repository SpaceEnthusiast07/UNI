package tree;

public class Tree {
    // Object reference to the parent node
    private Tree parent;
	// Object reference for left subtree
	private Tree left;
	// Object reference for right subtree
	private Tree right;
	// Actual data in node
	private int data;
	
	// Constructor
	public Tree(Tree parent, int data) {
		// Assign the object reference for the parent to the attribute
		this.parent = parent;
		this.data = data;
	}
	
	// Method to add a node
	public void add(int newNodeData) {
		// Check if the data is greater than the data of this current node
		if (newNodeData >= this.data) {
			// Check if the right pointer of this node is null
			if (right == null) {
				// Simply add this new node as this node's right child
				this.right = new Tree(this, newNodeData);
			} else {
				// Pass this new data to the right subtree of this node
				this.right.add(newNodeData);
			}
		} else {
			// Check if the left pointer of this node is null
			if (left == null) {
				// Simply add this new node as this node's left child
				this.left = new Tree(this, newNodeData);
			} else {
				// Pass this new data to the left subtree of this node
				this.left.add(newNodeData);
			}
		}
	}

	@Override
	public String toString() {
		String parentString;
		String leftString;
		String rightString;

		if (this.parent == null) {parentString = "";}
		else {parentString = this.parent.toString();}

		if (this.left == null) {leftString = "";}
		else {leftString = this.left.toString();}

		if (this.right == null) {rightString = "";}
		else {rightString = this.right.toString();}

		return String.format("TreeNode:\n--- parent=%s\n--- left=%s\n--- right=%s\n--- data=%d", parentString, leftString, rightString, this.data);
	}
}
