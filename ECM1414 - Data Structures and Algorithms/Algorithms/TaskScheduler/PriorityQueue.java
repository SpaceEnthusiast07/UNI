/**
 * This priority queue is implemented using a min-heap.<br>
 * The data item stored at each node must contain the fields "priority"
 * and "value" to be compatible with this implementation.<br>
 * A more important task has a priority closer to 1.<br>
 */
class PriorityQueue {
    // I am implementing the min-heap using an array
    private TaskNode[] data;
    // This is the current number of nodes in the heap
    private int nodeCount;
    // This is the maximum number of nodes allowed in the heap
    private int maxNodes;

    public PriorityQueue() {
        // The heap defaults to a max size of 100
        this(100);
    }

    public PriorityQueue(int maxNodes) {
        // Initialise the maximum number of nodes (size of data array)
        this.maxNodes = maxNodes;
        // Initialise the data array
        this.data = new TaskNode[this.maxNodes];
        // Initialise the node count
        this.nodeCount = 0;
    }

    /**
     * Determines if the heap is full.
     * @return True if the heap is full, otherwise false.
     */
    public boolean isFull() {
        return nodeCount == maxNodes;
    }

    /**
     * Determines if the heap is empty.
     * @return True if the heap is empty, otherwise false.
     */
    public boolean isEmpty() {
        return nodeCount == 0;
    }

    /**
     * Inserts a new node into the min-heap and ensures the min-heap property remains.<br>
     * The new node is inserted in the last place in the min-heap, and then it swims up
     * through the min-heap into its correct place.
     * @param newData The new node to add to the min-heap.
     */
    public void insert(TaskNode newData) {
        // Check if the heap is full
        if (isFull()) {
            System.out.println("Heap is full!");
        }

        // Simply insert the new node in the last available index
        int newNodeIndex = nodeCount;
        data[newNodeIndex] = newData;
        // Increment the node counter to account for the addition of the new node
        nodeCount++;

        // Calculate the index of the parent node
        int parentNodeIndex = (newNodeIndex-1) / 2;
        // Initialise a tracker for if the new node has found its correct space
        boolean foundCorrectSpace = false;

        // Iteratively swim the new node up the heap until it is in its correct place
        while (parentNodeIndex >= 0 && foundCorrectSpace == false) {
            // If the parent's priority is larger than the new node's priority, swap them to keep the min-heap property
            if (data[parentNodeIndex].getPriority() > newData.getPriority()) {
                data[newNodeIndex] = data[parentNodeIndex];
                data[parentNodeIndex] = newData;
                // Now, the index of the new node is the parent index
                newNodeIndex = parentNodeIndex;
                // Re-calculate the parent index
                parentNodeIndex = (newNodeIndex-1) / 2;
            }
            // Else, the new node has found its correct space
            else {
                foundCorrectSpace = true;
            }
        }
    }

    /**
     * Extracts the min element from the min-heap, which is the root node.<br>
     * It then moves the last node to the position of the root node, and sinks this
     * new root node in to its correct place.
     * @return The min element extracted from the min-heap.
     */
    public TaskNode extractMin() {
        // Check if the heap is empty
        if (isEmpty()) {
            System.out.println("Queue is empty.");
            return null;
        }

        // Since this is a min-heap, the root node is the minimum element
        TaskNode min = data[0];

        // Move the last node into the position of the root
        data[0] = data[nodeCount-1];
        data[nodeCount-1] = null;

        // Initialise variables used in the "sink" process
        boolean foundCorrectPlace = false;
        int currentNode = 0;
        int leftChild;
        int rightChild;
        int smallerChild;
        TaskNode temp;

        // Iteratively "sink" this new root node into its correct place
        while (foundCorrectPlace == false && isLeafNode(currentNode) == false) {
            // Calculate the left and right children
            leftChild = (currentNode*2) + 1;
            rightChild = (currentNode*2) + 2;

            // Determine the smaller child
            if (data[leftChild].getPriority() < data[rightChild].getPriority()) {
                smallerChild = leftChild;
            }
            else {
                smallerChild = rightChild;
            }

            // If the current node is larger than the smaller child,
            // swap the current node with the smaller child
            if (data[currentNode].getPriority() > data[smallerChild].getPriority()) {
                temp = data[currentNode];
                data[currentNode] = data[smallerChild];
                data[smallerChild] = temp;

                // Update the current node index to the smaller child index
                currentNode = smallerChild;
            }
            // Else, the current node is in its correct place
            else {
                foundCorrectPlace = true;
            }
        }

        // Decrement the node count to reflect the removed node
        nodeCount--;

        // Return the min element
        return min;
    }

    /**
     * Determines if the provided node is a leaf node.
     * @param nodeIndex The index of the node in the array to analyse.
     */
    private boolean isLeafNode(int nodeIndex) {
        // Calculate the indices for the left and right children nodes
        int leftChild = (nodeIndex*2) + 1;
        int rightChild = (nodeIndex*2) + 2;

        // If the left child is not null and within the bounds, this node is not a leaf node
        if (leftChild < this.maxNodes && data[leftChild] != null) {
            return false;
        }
        // Check the right child as well
        else if (rightChild < this.maxNodes && data[rightChild] != null) {
            return false;
        }
        // Otherwise, this node is a leaf
        else {
            return true;
        }
    }

    /**
     * Needs Correction!<br>
     * Converts the array representation of the min-heap to a string representation for the user to view.<br>
     * Currently, the best way I can output a tree structure is to output the corresponding edges between nodes.
     * @return A string representing the min-heap.
     */
    @Override
    public String toString() {
        // Create a new string builder object to build the output of the heap
        StringBuilder sb = new StringBuilder("");

        // Convert the heap to a string
        convertHeapToString(0, sb);

        // Return the string representation of the heap
        return sb.toString();
    }

    /**
     * The recursive function that converts the min-heap to a string.
     * @param nodeIndex The index of the node to start at.
     * @param sb The string builder object used to create the string representation.
     */
    private void convertHeapToString(int nodeIndex, StringBuilder sb) {
        // If the current node is a leaf node, there is nothing to output
        if (isLeafNode(nodeIndex)) {
            return;
        }

        // Else, calculate the indices of the left and right children nodes
        int leftChild = (nodeIndex*2) + 1;
        int rightChild = (nodeIndex*2) + 2;

        // If the left child exists, add that edge to the string
        if (leftChild < maxNodes && data[leftChild] != null) {
            sb.append(String.format("%d-%d ", data[nodeIndex].getTitle(), data[leftChild].getTitle()));
        }

        // If the right child exists, add that edge to the string
        if (rightChild < maxNodes && data[rightChild] != null) {
            sb.append(String.format("%d-%d ", data[nodeIndex].getTitle(), data[rightChild].getTitle()));
        }

        // Repeated code warning!
        // I have done this due to that output format I want!

        // Convert the left sub-tree to a string
        if (leftChild < maxNodes && data[leftChild] != null) {
            convertHeapToString(leftChild, sb);
        }

        // Convert the right sub-tree to a string
        if (rightChild < maxNodes && data[rightChild] != null) {
            convertHeapToString(rightChild, sb);
        }
    }
}