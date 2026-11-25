import java.io.*;
import java.net.*;
import java.nio.charset.StandardCharsets;

public class Server {
	public static void main(String[] args) {
        System.out.println("=== Server for Basic Java Networking Application ===");

		// Set up a new TCP connection listener on port 5000
        try (ServerSocket server = new ServerSocket(5000)) {
            // Ouptut successful TCP connection
            System.out.printf("\nLOG: Server listening on port %d\n\n", server.getLocalPort());

            // Wait for a new TCP Connection request
            // Program waits here until a new connection request arrives
            try (Socket client = server.accept()) {
                // Ouptut successful TCP connection
                System.out.printf("\nLOG: Client connected on port %d from remote address %s\n\n", 
                    client.getLocalPort(), client.getRemoteSocketAddress());
                
                // Initialise the input stream - receive data
                BufferedReader in = new BufferedReader(
                    new InputStreamReader(client.getInputStream(), StandardCharsets.UTF_8)
                );

                // Initialise the output stream - send data
                PrintWriter out = new PrintWriter(
                    new OutputStreamWriter(client.getOutputStream(), StandardCharsets.UTF_8), true
                );

                String message = "default";
                while (message != "\\q") {
                    // Read the received message
                    message = in.readLine();

                    System.out.println("--- New Message ---");

                    // Log the received message
                    System.out.printf("Received \"%s\"\n\n", message);

                    // Echo the message back to the client
                    out.printf("Echo: %s\n", message);

                    in.readLine();
                }
            } catch (IOException e) {
                System.out.println("ERROR: Couldn't create new client Socket.");
            }
        } catch (IOException e) {
            System.out.println("ERROR: Couldn't create new ServerSocket.");
        }
	}
}
