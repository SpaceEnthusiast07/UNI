/**
 * This version of the Quicksort algorithm is more efficient because it only uses one for-loop.
 * Whereas, my old version had a while-loop that had two other while-loops nested within it.
 */

public class QuickSortTest {
    public static void main(String[] args) {
        // Create an array of integers to sort
        int[] array = {4, 3, 54, 23, 8, 65, 98, 32, 1, 6, 7, 23, 0};

        System.out.println("======================");
        System.out.println("=== Quicksort Test ===");
        System.out.println("======================\n");

        System.out.printf("Original Array: %s\n", convertArrayToString(array));

        // Sort the array
        quicksort(array, 0, array.length-1);

        System.out.printf("Sorted Array: %s\n", convertArrayToString(array));
    }

    public static void quicksort(int[] array, int start, int end) {
        // If the array is only 1 element, it is already sorted
        if (start >= end) {
            return;
        }

        // Find the final index for the pivot
        int pivotFinalIndex = partition(array, start, end);

        // Sort the two partitions
        quicksort(array, start, pivotFinalIndex-1);
        quicksort(array, pivotFinalIndex+1, end);
    }

    private static int partition(int[] array, int start, int end) {
        // Set the pivot to the last element in this partition
        int pivot = array[end];

        // Everything in this partition that it left of i (including i) is less than
        // or equal to the pivot
        // I.e., i marks the boundry between values "<=" to the pivot and values ">" the pivot
        int i = start - 1;
        int temp;

        for (int j = start; j < end; j++) {
            if (array[j] <= pivot) {
                i++;
                temp = array[i];
                array[i] = array[j];
                array[j] = temp;
            }
        }

        // The final position of i+1 is the new position for the pivot
        array[end] = array[i+1];
        array[i+1] = pivot;

        return i+1;
    }

    public static String convertArrayToString(int[] array) {
        // If the array is empty, cannot print anything
        if (array.length == 0) {
            return "Empty Array";
        }

        // Insert the first element into the output
        String output = Integer.toString(array[0]);

        // Iterate through the rest of the array
        for (int i = 1; i < array.length; i++) {
            output += ", " + Integer.toString(array[i]);
        }

        // Return the result
        return output;
    }
}