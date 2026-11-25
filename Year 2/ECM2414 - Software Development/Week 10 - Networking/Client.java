import java.io.*;
import java.net.*;
import java.nio.charset.StandardCharsets;

public class Client {
	public static void main(String[] args) {
        // Create a new TCP connection with remote socket address "localhost:5000"
		try (Socket server = new Socket("localhost", 5000)) {
                // Ouptut successful TCP connection
                System.out.printf("LOG: Successfully connected to server with socket address %s\n", server.getRemoteSocketAddress());
                
                // Initialise the input stream - receive data
                BufferedReader in = new BufferedReader(
                    new InputStreamReader(server.getInputStream(), StandardCharsets.UTF_8)
                );

                // Initialise the output stream - send data
                PrintWriter out = new PrintWriter(
                    new OutputStreamWriter(server.getOutputStream(), StandardCharsets.UTF_8), true
                );

                // Send a message to the server
                String message = "Hello server and world of networking!";
                out.println(message);

                // Log sent message
                System.out.printf("LOG: Sent \"%s\" to server at address %s\n", message, server.getRemoteSocketAddress());

                // Receive the server's response
                String response = in.readLine();

                // Log the received message
                System.out.printf("LOG: Server replied with \"%s\"\n", response);
            } catch (IOException e) {
                System.out.println("ERROR: Couldn't connect to server.");
            }
	}
}
