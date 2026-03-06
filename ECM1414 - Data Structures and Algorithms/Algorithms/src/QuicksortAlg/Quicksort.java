/**
 * This class implements the quicksort algorithm.
 * The main entry point is the sort() function.
 */
public class Quicksort {
    public static int[] sort(int[] unsortedArray, int left, int right) {
        // Choose pivot element
        int pivotIndex = (left+right)/2;
        int pivot = unsortedArray[pivotIndex];

        // Temp variable used for swapping values
        int temp;

        // Loop to move elements less than the pivot, below the pivot
        // and elements that are larger than the pivot, above the pivot
        while (left < right) {
            // Shif the left pointer up until you reach an element that is larger than the pivot
            while (unsortedArray[left] < pivot) {
                left++;
            }

            // Shift the right pointer down until you encounter an element that is less than the pivot
            while (unsortedArray[right] > pivot) {
                right--;
            }

            // Swap elements at left and right, since they are in the wrong place
            temp = unsortedArray[left];
            unsortedArray[left] = unsortedArray[right];
            unsortedArray[right] = temp;
        }

        // Since right and left are now equal, new position for pivot found
        pivotIndex = left;
        
        // Now, sort the left and right halves
        sort(unsortedArray, 0, left-1);
        sort(unsortedArray, unsortedArray.length, left+1);

        // Return the sorted result
        return unsortedArray;
    }
}