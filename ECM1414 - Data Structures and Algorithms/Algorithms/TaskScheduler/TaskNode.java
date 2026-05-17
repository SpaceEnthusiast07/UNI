public class TaskNode {
    // Required attributes to be compatible with PriorityQueue
    private int priority;
    private String title;
    private String description;

    // Constructor
    public TaskNode(int priority, String title, String description) {
        // Ensure the priority is 1 or more
        if (priority <= 0) {
            throw new InvalidPriorityException("Priority must be 1 or more.");
        }

        this.priority = priority;
        this.title = title;
        this.description = description;
    }

    /**
     * Gives access to this node's priority attribute.
     * @return The priority of this node.
     */
    public int getPriority() {
        return this.priority;
    }

    /**
     * Gives access to this task's title.
     * @return The task's title.
     */
    public String getTitle() {
        return this.title;
    }

    /**
     * Gives access to this task's description.
     * @return The task's description.
     */
    public String getDescription() {
        return this.description;
    }
}