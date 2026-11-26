import java.io.*;
import java.net.*;
//import java.nio.charset.StandardCharsets;
import java.util.Scanner;

public class Client {
	public static void main(String[] args) {
        System.out.print("=== Basic Java Networking Application ===\n\nLOG: Attempting connection with server...\n");

        String serverIPAddress = "localhost";
        int serverPort = 5000;
        // Check if user provided remote server IP address at application startup
        if (args.length > 1 && args[0].equals("-sip")) {
            serverIPAddress = args[1];
        }

        // Create a new TCP connection with remote socket address "localhost:5000"
		try (Socket server = new Socket(serverIPAddress, serverPort); Scanner userIn = new Scanner(System.in)) {
            // Ouptut successful TCP connection
            System.out.printf("\nLOG: Successfully connected to server with remote address '%s'.\n\n", server.getRemoteSocketAddress());

            // Initialise object output stream - send data
            ObjectOutputStream out = new ObjectOutputStream(server.getOutputStream());
            /* --- Old string based communication system ---
            PrintWriter out = new PrintWriter(
                new OutputStreamWriter(server.getOutputStream(), StandardCharsets.UTF_8), true
            );
            */

            // Flush the output stream before initialising the input stream
            // This removes the default header ObjectOutputStream() inserts
            out.flush();
            
            // Initialise object input stream - receive data
            ObjectInputStream in = new ObjectInputStream(server.getInputStream());
            /* --- Old string based communication system ---
            BufferedReader in = new BufferedReader(
                new InputStreamReader(server.getInputStream(), StandardCharsets.UTF_8)
            );
            */

            // Ask the user to input a message to send to the server
            String userInput = "default";
            int messageID = 0;
            Message userMessage;
            while (true) {
                // Mark a new message
                messageID++;
                System.out.printf("--- Message %d ---\n", messageID);

                // Input the user's message
                System.out.print("Message: ");
                userInput = userIn.nextLine();

                // Terminate connection if user wants to
                if (userInput.equals("\\q")) {
                    Message terminationMessage = new Message(MessageType.TERMINATE, null, null, null);
                    out.writeObject(terminationMessage);
                    out.flush();
                    break;
                }

                // Construct a new message
                userMessage = new Message(userInput);

                // Add the message to the buffer
                out.writeObject(userMessage);
                // Flush to send the message
                out.flush();

                // Log sent message
                //System.out.printf("LOG: Sent \"%s\" to server at address %s\n", message, server.getRemoteSocketAddress());

                // Receive the server's response
                Message serverResponse = (Message) in.readObject();
                System.out.printf("Server response: %s\n\n", serverResponse);
            }

            // Log terminated connection
            System.out.printf("\nLOG: Connection terminated with server at remote address '%s'.\n\n", server.getRemoteSocketAddress());
        } catch (IOException e) {
            System.out.printf("\nERROR: Couldn't connect to server at remote address '%s:%d'.\n\n", serverIPAddress, serverPort);
        } catch (ClassNotFoundException e) {
            System.out.println("\nERROR: Message classes don't match in deserialisation process.\n");
        }
	}
}
