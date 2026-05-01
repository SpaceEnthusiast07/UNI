class Node {
	int data;
	Node next;
	Node(int data) {
		this.data = data;
		this.next = null;
	}
    Node(int data, Node next) {
        this.data = data;
        this.next = next;
    }
}

public class LinkedListReversal {
    public static void main(String[] args) {
        // Create some nodes
        Node n1 = new Node(4);
        Node n2 = new Node(3, n1);
        Node n3 = new Node(2, n2);
        Node head = new Node(1, n3);

        System.out.println("=====================================");
        System.out.println("=== In Place Linked List Reversal ===");
        System.out.println("=====================================");
        System.out.println("Info:\n - Given a linked list, reverse it in-place\n - One approach is to use recursion and the other is iteration\n");

        System.out.printf("Original List:      %s\n", convertListToString(head));
        head = recursiveReversal(head);
        System.out.printf("Recursive Reversal: %s\n", convertListToString(head));
        head = iterativeReversal(head);
        head = iterativeReversal(head);
        System.out.printf("Iterative Reversal: %s\n", convertListToString(head));
    }

    public static Node iterativeReversal(Node head) {
        // Cannot reverse a list that is empty or only has one element
        if (head == null || head.next == null) {
            return head;
        }

        // Set the previous node
        Node prev = null;
        Node current = head;
        Node temp;

        while (current != null) {
            temp = current.next;
            current.next = prev;
            prev = current;
            current = temp;
        }

        return prev;
    }
    
    public static Node recursiveReversal(Node head) {
        // Linked list is already reversed if there is no more nodes
        if (head.next == null) {
            return head;
        }
        // Recursively move down through the linked list
        Node lastNode = traverseLinkedList(head.next);
        // Set the second node to point to this node
        head.next.next = head;
        // Set the pointer of the old head to null
        head.next = null;
        // Return the last node in the list as the new head
        return lastNode;
    }

    private static Node traverseLinkedList(Node node) {
        // The pointer of this node is null when it is the last node
        if (node.next == null) {
            return node;
        }
        // Since this is not the last node, traverse further down the list
        Node lastNode = traverseLinkedList (node.next);
        // Change the pointer of the next node to point to this node
        node.next.next = node;
        // Return the last node in the list
        return lastNode;
    }

    public static String convertListToString(Node head) {
        // Cannot print an empty list
        if (head == null) {
            return "Empty List";
        }

        // Insert the first node into the String
        String output = Integer.toString(head.data);

        // Iterate through the rest of the list
        Node currentNode = head.next;
        while (currentNode != null) {
            output += " -> " + Integer.toString(currentNode.data);
            currentNode = currentNode.next;
        }
        return output;
    }
}
