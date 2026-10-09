public class FlagExample extends Thread {
    // 
    private volatile boolean done = false;

    public FlagExample() {
        // Empty constructor
    }

    public static void main(String[] args) {
        // Creating a new flag example thread object
        FlagExample flagExample = new FlagExample();

        // Creating a new thread in the system and calling its run() method
        flagExample.start();

        // Indicating that the thread has been started
        System.out.println("Thread started.");

        // Telling the thread to stop
        flagExample.stopThread();
    }

    public void run() {
        while(!done) {
            System.out.println(this.getName() + " : dum diddly dum ...");

            try {
                Thread.sleep(1000);
                System.out.println(this.getName() + " : Finished sleeping.");
            } catch (InterruptedException e) {
                System.out.println(this.getName() + " : I have been interrupted.");
            }
        }
    }

    public void stopThread() {
        System.out.println(this.getName() + " : Flag is being set ...");
        this.done = true;
        System.out.println(this.getName() + " : Flag is set.");
    }
}