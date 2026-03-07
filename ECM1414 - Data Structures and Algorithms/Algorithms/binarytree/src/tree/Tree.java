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
	
	// Constructors
    public Tree(int data) {
        this.data = data;
    }
	public Tree(Tree parent, int data) {
		// Assign the object reference for the parent to the attribute
		this.parent = parent;
		this.data = data;
	}

    // Getter for the data attribute
    public int getData() {
        return this.data;
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
        String leftChildData = "";
        String rightChildData = "";
        String leftChildString = "";
        String rightChildString = "";

        if (this.left != null) {
            leftChildData = Integer.toString(this.left.getData());
            leftChildString = this.left.toString();
        }

        if (this.right != null) {
            rightChildData = Integer.toString(this.right.getData());
            rightChildString = this.right.toString();
        }

        String outputString = String.format("TreeNode:  data=%d  left=%s  right=%s", this.data, leftChildData, rightChildData);

        outputString = String.format("%s\n%s\n%s", outputString, leftChildString, rightChildString);

        return outputString;
	}
}
