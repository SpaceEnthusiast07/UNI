import java.awt.*;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JButton;
import javax.swing.JComponent;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;

public class Beeper extends JPanel implements ActionListener, KeyListener {
    JButton button;
 
    public Beeper() {
        super(new BorderLayout());
        button = new JButton("Click Me");
        button.setPreferredSize(new Dimension(200, 80));
        add(button, BorderLayout.CENTER);
        button.addActionListener(this);
    }
 
    public void actionPerformed(ActionEvent e) {
        Toolkit.getDefaultToolkit().beep();
        System.out.println("Beep!");
    }

    @Override
    public void keyPressed(KeyEvent e) {
        button.setText(String.format("Key Pressed: %c", e.getKeyChar()));
        System.out.println(String.format("Key Pressed: %c", e.getKeyChar()));
    }

    @Override
    public void keyReleased(KeyEvent e) {
        button.setText(String.format("Key Released: %c", e.getKeyChar()));
        System.out.println(String.format("Key Released: %c", e.getKeyChar()));
    }

    @Override
    public void keyTyped(KeyEvent e) {
        button.setText(String.format("Key Typed: %c", e.getKeyChar()));
        System.out.println(String.format("Key Typed: %c", e.getKeyChar()));
    }
 
    /**
     * Create the GUI and show it. For thread safety,
     * this method should be invoked from the
     * event-dispatching thread.
     */
    private static void createAndShowGUI() {
        //Create and set up the window.
        JFrame frame = new JFrame("Beeper");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setPreferredSize(new Dimension(500,500));
        
        //Create and set up the content pane.
        JComponent newContentPane = new Beeper();
        newContentPane.setOpaque(true); //content panes must be opaque
        frame.setContentPane(newContentPane);
        frame.addKeyListener(new Beeper());
        
        //Display the window.
        frame.pack();
        frame.setVisible(true);
    }
    
    public static void main(String[] args) {
        //Schedule a job for the event-dispatching thread:
        //creating and showing this application's GUI.
        javax.swing.SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                createAndShowGUI();
            }
        });
    }
}