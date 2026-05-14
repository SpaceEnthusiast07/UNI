public class Page {
    // Attributes about a page
    private String title;
    private String content;

    // Constructors
    public Page(String title, String content) {
        this.title = title;
        this.content = content;
    }

    /**
     * Allows the client to update the page title.
     * @param newTitle
     */
    public void setTitle(String newTitle) {
        this.title = newTitle;
    }

    /**
     * Convert this page to one single string.
     */
    public String toString() {
        StringBuilder stringRep = new StringBuilder();

        // Calculate the above and below divider length
        int dividerLength = title.length() + 10;

        stringRep.append("=".repeat(dividerLength));
        stringRep.append("\n==== ")
        stringRep.append(this.title);
        stringRep.append(" ====\n")
        stringRep.append("=".repeat(dividerLength));
        stringRep.append("\n");
        stringRep.append(this.content);
    }
}