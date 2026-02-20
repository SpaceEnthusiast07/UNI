public class QuicksortApp {
    public static void main(String[] args) {
        int[] myArray = {4,6,12,776,89,765,87,34,56,345,67,53,2,6,75,23,378,5,365,75431,7645,84,65,3,754,75,6,2,5,6,4,2,43,43,234,5};

        sort(myArray, 0, myArray.length-1);

        for (int number: myArray) {
            System.out.print(number + " ");
        }
        System.out.println();
    }

    public static void sort(int[] unsortedArray, int start, int end) {
        // Base Case:
        if (start >= end) {
            return;
        }

        // Recursive Case:
        // Choose pivot element
        int pivotValue = unsortedArray[start];
        int lowMark = start + 1;
        int highMark = end;
        // Temp variable used for swapping values
        int temp;
        boolean finished = false;

        // Repeat until low and high values have been swapped as needed
        while (!finished) {
            // Shift the left pointer up until you reach an element that is larger than the pivot
            while (lowMark <= highMark && unsortedArray[lowMark] <= pivotValue) {
                lowMark++;
            }

            // Shift the right pointer down until you encounter an element that is less than the pivot
            while (highMark >= lowMark && unsortedArray[highMark] >= pivotValue) {
                highMark--;
            }

            if (lowMark < highMark) {
                // Swap elements at left and right, since they are in the wrong place
                temp = unsortedArray[lowMark];
                unsortedArray[lowMark] = unsortedArray[highMark];
                unsortedArray[highMark] = temp;
            } else {
                finished = true;
            }
        }

        // Swap the pivot value and the value at the highMark
        temp = unsortedArray[start];
        unsortedArray[start] = unsortedArray[highMark];
        unsortedArray[highMark] = temp;
        
        // Now, sort the left and right halves
        sort(unsortedArray, start, highMark-1);
        sort(unsortedArray, highMark+1, end);

        // Return the sorted result
        return;
    }
}
