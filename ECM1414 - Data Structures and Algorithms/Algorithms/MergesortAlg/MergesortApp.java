public class MergesortApp {
    public static void main(String[] args) {
        System.out.println("=== Mergesort App ===");
    }

    void mergesort(int[] list, int first, int last) {
        // Base case
        // If list is of size 1, return list
        if (first == last) return;

        // Recursive case
        // Calculate the middle index
        int m = (first+last)/2;

        // Call merge sort on the two halves
        mergesort(list, first, m);
        mergesort(list, m+1, last);

        // Merge these two halves
        merge(list, first, last, m);

        return;
    }

    void merge(int[] list, int first, int last, int m) {
        
    }
}
