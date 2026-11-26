import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;
import java.net.Inet4Address;
import java.net.InetAddress;
import java.net.NetworkInterface;
import java.net.SocketException;
//import java.nio.charset.StandardCharsets;
import java.util.Enumeration;

public class Server {
	public static void main(String[] args) {
        System.out.println("=== Server for Basic Java Networking Application ===");

		// Set up a new TCP connection listener on port 5000
        try (ServerSocket server = new ServerSocket(5000)) {
            // Ouptut successful TCP connection
            System.out.printf("\nLOG: Server listening for new TCP connection on local port '%s'.\n", server.getLocalPort());

            // Ouptut available IP addresses to connect to
            System.out.println("\nCONNECTION: Available IP addresses:");
            printLocalIPv4Addresses();

            // Wait for a new TCP Connection request
            // Program waits here until a new connection request arrives
            try (Socket client = server.accept()) {
                // Ouptut successful TCP connection
                System.out.printf("\nLOG: Client connected to local address '%s' from remote address '%s'.\n\n", 
                    client.getLocalSocketAddress(), client.getRemoteSocketAddress());

                // Initialise the output stream - send data
                ObjectOutputStream out = new ObjectOutputStream(client.getOutputStream());
                /* --- Old string based communication system ---
                PrintWriter out = new PrintWriter(
                    new OutputStreamWriter(client.getOutputStream(), StandardCharsets.UTF_8), true
                );
                */

                // Flush the output stream before initialising the input stream
                // This removes the default header ObjectOutputStream() inserts
                out.flush();
                
                // Initialise object input stream - receive data
                ObjectInputStream in = new ObjectInputStream(client.getInputStream());
                /* --- Old string based communication system ---
                BufferedReader in = new BufferedReader(
                    new InputStreamReader(client.getInputStream(), StandardCharsets.UTF_8)
                );
                */

                Message message;
                int messageID = 0;
                Message response;
                while (true) {
                    // Read the received message
                    message = (Message) in.readObject();

                    // Check if the client terminated the connection
                    if (message == null || message.getType() == MessageType.TERMINATE) {
                        break;
                    }

                    // Mark a new message
                    messageID++;
                    System.out.printf("--- Message %d ---\n", messageID);

                    // Log the received message
                    System.out.printf("Received: %s\n", message);

                    // Construct the response
                    response = new Message(message.getBody());
                    System.out.printf("Sent back: %s\n\n", response);

                    // Echo the message back to the client
                    out.writeObject(response);
                }

                // Log connection termination
                System.out.printf("\nLOG: Connection terminated with client at remote address '%s'.\n\n", client.getRemoteSocketAddress());
            } catch (IOException e) {
                System.out.println("ERROR: Couldn't create new client Socket.");
            }
        } catch (IOException e) {
            System.out.println("ERROR: Couldn't create new ServerSocket.");
        } catch (ClassNotFoundException e) {
            System.out.println("\nERROR: Message classes don't match in deserialisation process.\n");
        }
	}

    /**
     * Ouputs a list of local IPv4 addresses that clients on the same network can use to connect to the server.
     * @throws SocketException if an I/O error occurs, or if the platform does not have at least one configured network interface.
     */
    private static void printLocalIPv4Addresses() throws SocketException {
        // Retrieve all the network interfaces on this machine
        Enumeration<NetworkInterface> interfaces = NetworkInterface.getNetworkInterfaces();

        // Loop through each interface
        while (interfaces != null && interfaces.hasMoreElements()) {
            // Extract a single interface to inspect
            NetworkInterface networkInterface = interfaces.nextElement();

            // Ignore inactive and loopback interfaces
            if ((!networkInterface.isUp()) || networkInterface.isLoopback()) {
                continue;
            }

            // Retrieve the IP addresses associated with this port
            Enumeration<InetAddress> ipAddresses = networkInterface.getInetAddresses();

            // Loop through the addresses and only choose ones that can be externally connected to
            while (ipAddresses.hasMoreElements()) {
                // Only output this IP address that
                // - Are IPv4 addresses
                // - Are not loopback addresses
                // - Are not linklocal addresses
                InetAddress ipAddress = ipAddresses.nextElement();
                if (ipAddress instanceof Inet4Address &&
                    !ipAddress.isLoopbackAddress() &&
                    !ipAddress.isLinkLocalAddress())
                {
                    System.out.printf(" - %s (%s)\n", ipAddress.getHostAddress(), ipAddress.getHostName());
                }
            }
        }
    }
}
