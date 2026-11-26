import java.io.*;
import java.net.*;
import java.nio.charset.StandardCharsets;
import java.util.Scanner;

public class Client {
	public static void main(String[] args) {
        System.out.print("=== Basic Java Networking Application ===\n\nLOG: Attempting connection with server...\n");

        String serverIPAddress = "localhost";
        // Check if user provided remote server IP address at application startup
        if (args.length > 1 && args[0].equals("-sip")) {
            serverIPAddress = args[1];
        }

        // Create a new TCP connection with remote socket address "localhost:5000"
		try (Socket server = new Socket(serverIPAddress, 5000); Scanner userIn = new Scanner(System.in)) {
            // Ouptut successful TCP connection
            System.out.printf("\nLOG: Successfully connected to server with remote address '%s'.\n\n", server.getRemoteSocketAddress());
            
            // Initialise the input stream - receive data
            BufferedReader in = new BufferedReader(
                new InputStreamReader(server.getInputStream(), StandardCharsets.UTF_8)
            );

            // Initialise the output stream - send data
            PrintWriter out = new PrintWriter(
                new OutputStreamWriter(server.getOutputStream(), StandardCharsets.UTF_8), true
            );

            // Ask the user to input a message to send to the server
            String userInput = "default";
            int messageID = 0;
            while (true) {
                // Mark a new message
                messageID++;
                System.out.printf("--- Message %d ---\n", messageID);

                // Input the user's message
                System.out.print("Message: ");
                userInput = userIn.nextLine();

                // Terminate connection if user wants to
                if (userInput.equals("\\q")) {
                    break;
                }

                // Add the message to the buffer, which is automatically flushed (sent)
                out.println(userInput);

                // Log sent message
                //System.out.printf("LOG: Sent \"%s\" to server at address %s\n", message, server.getRemoteSocketAddress());

                // Receive the server's response
                String serverResponse = in.readLine();
                System.out.printf("Server response: %s\n\n", serverResponse);
            }

            // Log terminated connection
            System.out.printf("\nLOG: Connection terminated with server at remote address '%s'.\n\n", server.getRemoteSocketAddress());
        } catch (IOException e) {
            System.out.println("ERROR: Couldn't connect to server.");
        }
	}
}
