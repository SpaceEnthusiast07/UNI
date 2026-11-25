import java.io.*;
import java.net.*;
import java.nio.charset.StandardCharsets;
import java.util.Scanner;

public class Client {
	public static void main(String[] args) {
        System.out.println("=== Basic Java Networking Application ===");

        // Create a new TCP connection with remote socket address "localhost:5000"
		try (Socket server = new Socket("localhost", 5000)) {
                // Ouptut successful TCP connection
                System.out.printf("\nLOG: Successfully connected to server with socket address %s\n\n", server.getRemoteSocketAddress());
                
                // Initialise the input stream - receive data
                BufferedReader in = new BufferedReader(
                    new InputStreamReader(server.getInputStream(), StandardCharsets.UTF_8)
                );

                // Initialise the output stream - send data
                PrintWriter out = new PrintWriter(
                    new OutputStreamWriter(server.getOutputStream(), StandardCharsets.UTF_8), true
                );

                // Initialise a new user input stream
                Scanner userIn = new Scanner(System.in);

                // Ask the user to input a message to send to the server
                String userInput = "default";
                int messageID = 0;
                while (userInput != "\\q") {
                    // Mark a new message
                    messageID++;
                    System.out.printf("--- Message %d ---\n", messageID);

                    // Input the user's message
                    System.out.print("Message: ");
                    userInput = userIn.nextLine();

                    // Add the message to the buffer, which is automatically flushed (sent)
                    out.println(userInput);

                    // Log sent message
                    //System.out.printf("LOG: Sent \"%s\" to server at address %s\n", message, server.getRemoteSocketAddress());

                    // Receive the server's response
                    String serverResponse = in.readLine();

                    // Output the received message
                    System.out.printf("Server response: %s\n\n", serverResponse);
                }
            } catch (IOException e) {
                System.out.println("ERROR: Couldn't connect to server.");
            }
	}
}
