public class QueueNode<T> {
    // Required attributes to be compatible with PriorityQueue
    private int priority;
    private T value;

    // Constructor
    public QueueNode(int priority, T value) {
        // Ensure the priority is 1 or more
        if (priority <= 0) {
            throw new InvalidPriorityException("Priority must be 1 or more.");
        }

        this.priority = priority;
        this.value = value;
    }

    /**
     * Gives access to this node's priority attribute.
     * @return The priority of this node.
     */
    public int getPriority() {
        return this.priority;
    }

    /**
     * Gives access to this node's value attribute.
     * @return The value held in this node.
     */
    public T getValue() {
        return this.value;
    }
}