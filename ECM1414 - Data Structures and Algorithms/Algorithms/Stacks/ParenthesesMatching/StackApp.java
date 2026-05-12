class Stack {
    // Array to contain the actual stack data
    private int[] data;
    // Points to the top element in the stack
    private int top;

    public Stack(int size) throws Exception {
        // Ensure size is greater than 0
        if (size <= 0) {
            throw new Exception("Size of stack cannot be zero or negative!");
        }
        // Initialise the data array
        data = new int[size];
        // Initialise the top pointer
        top = -1;
    }

    /**
     * Checks if the stack is full.
     * @return True if the stack is full, otherwise false.
     */
    public boolean isFull() {
        return top + 1 == data.length;
    }

    /**
     * Checks if the stack is empty.
     * @return True if the stack is empty, otherwise false.
     */
    public boolean isEmpty() {
        return top == -1;
    }

    /**
     * Adds an item to the top of the stack.
     * @param item The data item to add to the stack.
     */
    public void enqueue(int newItem) {
        // Check if the stack is full
        if (isFull()) {
            System.out.println("Stack is full!");
            return;
        }
        // Otherwise, increment the top pointer and add the new element there
        top++;
        data[top] = newItem;
    }

    /**
     * Removes an item from the top of the stack and returns the dequeued item.
     * @return The dequeued item.
     */
    public int dequeue() {
        // Check if the stack is empty
        if (isEmpty()) {
            System.out.println("Stack is empty!");
            return 0;
        }
        // Decrement the top pointer and return the dequeued item
        top--;
        return data[top+1];
    }

    public String toString() {
        // You cannot print an empty stack
        if (isEmpty()) {
            return "Empty stack!";
        }

        // Initialise the string representation of the stack
        String stringRep = "Top | ";

        // Add the data items to the string representation
        for (int i = 0; i <= top; i++) {
            stringRep = stringRep.concat(String.format("%d | ", data[i]));
        }

        // Add the bottom indicator to the representation
        stringRep = stringRep.concat("Bottom");

        return stringRep;
    }
}

public class StackApp {
    public static void main(String[] args) throws Exception {
        // Output app title
        System.out.println("============================");
        System.out.println("=== Parentheses Matching ===");
        System.out.println("============================");
        System.out.println("Info: Checks if a sequence of parentheses is complete.\n");
        
        System.out.println("Testing stack output functionality:");
        // Create a new stack
        Stack stack = new Stack(10);

        // Add some items to the stack
        stack.enqueue(1);
        stack.enqueue(2);
        stack.enqueue(3);
        stack.enqueue(4);

        // Output the stack
        System.out.println(stack);

        System.out.println("\nTesting matching logic:");
        // Check if the sequence of parentheses are matching
        String parenSeq = "()(()()))()";
        boolean isMatchingSeq = isMatching(parenSeq);
        String verbage = (isMatchingSeq) ? "is" : "is not";

        System.out.printf("The sequence: \"%s\" %s matching.\n", parenSeq, verbage);
    }

    /**
     * Detemrines if a sequence of parentheses, which can include other characters, is complete.<br>
     * Logic:
     * <ul>
     *      <li>If the first character is a close bracket, the sequence is automatically not complete</li>
     *      <li>Otherwise, add the character, if it is an open bracket, onto the stack</li>
     *      <li>For every close bracket encountered thereafter:
     *          <ul>
     *          <li>If the stack is empty, the sequence is automatically not complete</li>
     *          <li>Else, remove an open bracket from the stack</li>
     *          </ul>
     *      </li>
     *      <li>At the end, if the stack is empty, the sequence is complete</li>
     * </ul>
     * @param string The sequence of parentheses, or simply characters, to check.
     * @return True if the sequence of parentheses is complete.
     * @throws Exception Thrown if the size of the stack, when initialising, is negative or zero.
     */
    public static boolean isMatching(String string) throws Exception {
        // If the first character is a close bracket, the sequence is automatically not matching
        if (string.charAt(0) == ')') {
            return false;
        }

        // Create a new stack to fit all the characters
        Stack stack = new Stack(string.length());

        // Iterate through the brackets, adding open brackets onto the stack
        // and removing them from the stack when a close bracket is encountered
        for (int i = 0; i < string.length(); i++) {
            if (string.charAt(i) == '(') {
                stack.enqueue(1); // Indicates an open bracket
            }
            else if (string.charAt(i) == ')') {
                if (stack.isEmpty()) {
                    return false;
                }
                else {
                    stack.dequeue();
                }
            }
        }

        // If the stack is empty, the sequence is matching, else it is not
        return stack.isEmpty();
    }
}
