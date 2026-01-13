public class Args {
    public static void main (String[] args) {
        // Check that any args have been passed in
        if (args.length == 0) {
            System.out.println("No arguments passed in!");
        }
        else {
            // Loop through each argument passed in
            for (int i = 0; i < args.length; i++) {
                System.out.println("Arg " + (i+1) + ": " + args[i]);
            }
        }
    }
}