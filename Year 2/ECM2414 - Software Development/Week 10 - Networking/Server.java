import java.io.*;
import java.net.*;
import java.nio.charset.StandardCharsets;

public class Server {
	public static void main(String[] args) {
        System.out.println("=== Server for Basic Java Networking Application ===");

		// Set up a new TCP connection listener on port 5000
        try (ServerSocket server = new ServerSocket(5000)) {
            // Ouptut successful TCP connection
            System.out.printf("\nLOG: Server listening for new TCP connection on local port '%s'.\n", server.getLocalPort());

            // Wait for a new TCP Connection request
            // Program waits here until a new connection request arrives
            try (Socket client = server.accept()) {
                // Ouptut successful TCP connection
                System.out.printf("\nLOG: Client connected to local address '%s' from remote address '%s'.\n\n", 
                    client.getLocalSocketAddress(), client.getRemoteSocketAddress());
                
                // Initialise the input stream - receive data
                BufferedReader in = new BufferedReader(
                    new InputStreamReader(client.getInputStream(), StandardCharsets.UTF_8)
                );

                // Initialise the output stream - send data
                PrintWriter out = new PrintWriter(
                    new OutputStreamWriter(client.getOutputStream(), StandardCharsets.UTF_8), true
                );

                String message = "default";
                int messageID = 0;
                String response;
                while (true) {
                    // Read the received message
                    message = in.readLine();

                    // Check if the client terminated the connection
                    if (message == null) {
                        break;
                    }

                    // Mark a new message
                    messageID++;
                    System.out.printf("--- Message %d ---\n", messageID);

                    // Log the received message
                    System.out.printf("Received: %s\n", message);

                    // Construct the response
                    response = String.format("Echo: %s\n", message);
                    System.out.printf("Sent back: %s\n", response);

                    // Echo the message back to the client
                    out.printf(response);
                }

                // Log connection termination
                System.out.printf("\nLOG: Connection terminated with client at remote address '%s'.\n\n", client.getRemoteSocketAddress());
            } catch (IOException e) {
                System.out.println("ERROR: Couldn't create new client Socket.");
            }
        } catch (IOException e) {
            System.out.println("ERROR: Couldn't create new ServerSocket.");
        }
	}
}
