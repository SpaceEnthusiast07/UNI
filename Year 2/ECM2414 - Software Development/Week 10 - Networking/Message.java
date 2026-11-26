import java.io.Serializable;

public class Message implements Serializable {
    // This identifier is used to check compatibility between the incoming class
    // structure and the local structure
    private static final long serialVersionUID = 1L;

    // Message headers
    private final MessageType type;
    private final String sender;
    private final String recipient;

    // Message body
    private final String body;

    public Message(MessageType type, String sender, String recipient, String body) {
        this.type = type;
        this.sender = sender;
        this.recipient = recipient;
        this.body = body;
    }

    public Message(String body) {
        this(MessageType.CHAT, null, null, body);
    }

    public Message(String body, String sender, String recipient) {
        this(MessageType.CHAT, sender, recipient, body);
    }

    public MessageType getType() {
        return this.type;
    }

    public String getSender() {
        return this.sender;
    }

    public String getRecipient() {
        return this.recipient;
    }

    public String getBody() {
        return this.body;
    }

    @Override
    public String toString() {
        // If this message is a regular chat message, simply return the body
        if (this.type == MessageType.CHAT) {
            return this.body;
        } else {
            return String.format("This is a control message with type: %s\n", this.type);
        }
    }
}
