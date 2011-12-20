package net.changethis.traffic;

public class World
{
	public static boolean mapinit = false;
	public static double defaultdist = 5;
	public static double defaultspeed = 5;
}

//goes in se[erate file; using web interface
package net.changethis.traffic;
import javax.swing.*;
public class GameMain
{
	public static World curWorld;
	private static boolean inGame;
	private static void createAndShowGUI() {
		//Create and set up the window.
		JFrame frame = new JFrame("GameMain");
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		//Add the ubiquitous "Hello World" label.
		JLabel label = new JLabel("Hello World");
		frame.getContentPane().add(label);
		
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
}