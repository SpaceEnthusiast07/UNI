/**
 * This is the class that implements the Heap ADT, specifically a min-heap.
 * <ul>
 * <li>
 * Structure:
 * <ul>
 *      <li>Array indices start at 0</li>
 *      <li>For any given node i, if left child is at index 2i+1 and right child at index 2i+2</li>
 *      <li>For any given node i, its parent is at index (i-1)//2 (integer division)</li>
 * </li>
 * </ul>
 * <li>
 * Logic:
 * <ul>
 *      <li>When inserting a new node, we simply insert it at the next available index (nodeCount)</li>
 *      <li>This new node will then "swim" up the heap and settle in its correct space</li>
 *      <li>When extracting the root node, the last node will replace it</li>
 *      <li>The new root node will then "sink" down the heap and settle in its correct space</li>
 * </ul>
 * </li>
 * </ul>
 */
class Heap {
    // I am implementing the heap using an array
    private int[] data;
    // This is the current number of nodes in the heap
    private int nodeCount;
    // This is the maximum number of nodes allowed in the heap
    private int maxNodes;

    public Heap() {
        // The heap defaults to a max size of 10
        this(10);
    }

    public Heap(int maxNodes) {
        // Initialise the maximum number of nodes (size of data array)
        this.maxNodes = maxNodes;
        // Initialise the data array
        this.data = new int[this.maxNodes];
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
     * Inserts a new node into the min-heap and ensures the min-heap property remains.<br>
     * The new node is inserted in the last place in the min-heap, and then it swims up
     * through the min-heap into its correct place.
     * @param newData The new node to add to the min-heap.
     */
    public void insert(int newData) {
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

        // Iteratively swim the new node up the heap until it is in its correct space
        while (parentNodeIndex >= 0 && foundCorrectSpace == false) {
            // If the parent is larger than the new node, swap them to keep the min-heap property
            if (data[parentNodeIndex] > newData) {
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
    public int extractMin() {
        // Since this is a min-heap, the root node is the minimum element
        int min = data[0];

        // Move the last node into the position of the root
        data[0] = data[nodeCount-1];
        data[nodeCount-1] = 0;

        // Initialise variables used in the "sink" process
        boolean foundCorrectPlace = false;
        int currentNode = 0;
        int leftChild;
        int rightChild;
        int smallerChild;
        int temp;

        // Iteratively "sink" this new root node into its correct place
        while (foundCorrectPlace == false && isLeafNode(currentNode) == false) {
            // Calculate the left and right children
            leftChild = (currentNode*2) + 1;
            rightChild = (currentNode*2) + 2;

            // Determine the smaller child
            if (data[leftChild] < data[rightChild]) {
                smallerChild = leftChild;
            }
            else {
                smallerChild = rightChild;
            }

            // If the current node is larger than the smaller child,
            // swap the current node with the smaller child
            if (data[currentNode] > data[smallerChild]) {
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

        // If the left child is not zero and within the bounds, this node is not a leaf node
        if (leftChild < this.maxNodes && data[leftChild] != 0) {
            return false;
        }
        // Check the right child as well
        else if (rightChild < this.maxNodes && data[rightChild] != 0) {
            return false;
        }
        // Otherwise, this node is a leaf
        else {
            return true;
        }
    }

    /**
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
        if (leftChild < maxNodes && data[leftChild] != 0) {
            sb.append(String.format("%d-%d ", data[nodeIndex], data[leftChild]));
        }

        // If the right child exists, add that edge to the string
        if (rightChild < maxNodes && data[rightChild] != 0) {
            sb.append(String.format("%d-%d ", data[nodeIndex], data[rightChild]));
        }

        // Repeated code warning!
        // I have done this due to that output format I want!

        // Convert the left sub-tree to a string
        if (leftChild < maxNodes && data[leftChild] != 0) {
            convertHeapToString(leftChild, sb);
        }

        // Convert the right sub-tree to a string
        if (rightChild < maxNodes && data[rightChild] != 0) {
            convertHeapToString(rightChild, sb);
        }
    }
}

public class HeapApp {
    public static void main(String[] args) {
        System.out.println("===========================");
        System.out.println("=== Heap Implementation ===");
        System.out.println("===========================");
        System.out.println("Info: This program implements a min-heap with the operations: insert(x) and extractMin().\n");

        // Create a new min-heap
        Heap heap = new Heap();

        // Add 3 nodes to the heap
        heap.insert(5);
        heap.insert(3);
        heap.insert(8);
        heap.insert(10);
        heap.insert(1);
        heap.insert(16);
        heap.insert(18);
        heap.insert(21);

        // Output the edges in the heap
        System.out.println("--- Create a new heap with the following edges:");
        System.out.printf("Heap: %s\n\n", heap);

        // Extract the min node
        System.out.println("--- Extract the min element from the heap:");
        int min = heap.extractMin();

        // Output the min element and the new state of the heap
        System.out.printf("Min element: %d\n\n", min);
        System.out.printf("--- New state of the heap:\nHeap: %s\n", heap);
    }
}