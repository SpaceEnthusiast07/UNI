package UNI.TestCode;

public class MultipleParameters {
    public static void main (String[] args) {
        // Calling the Varargs function
        System.out.println(add());
        System.out.println(add(2, 3));

        // Calling the DATATYPE[] function
        //System.out.println(add2());    <- Compiler error
        System.out.println(add2(new int[]{1, 3}));
    }

    public static int add(int... args) {
        int result = 0;
        for (int i = 0; i < args.length; i++) {
            result += args[i];
        }
        return result;
    }


    public static int add2(int[] args) {
        int result = 0;
        for (int i = 0; i < args.length; i++) {
            result += args[i];
        }
        return result;
    }
}


