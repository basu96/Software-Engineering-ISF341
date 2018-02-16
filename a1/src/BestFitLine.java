import java.awt.Button;
import java.awt.GridBagConstraints;
import java.awt.GridBagLayout;
import java.awt.Insets;
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.util.*;

class BestFitLine{

    BestFitLine(){
		prepareGUI();
	}

    private int numberOfPoints = 0;
    private JTextField x1=new JTextField(10);
    private JTextField y1=new JTextField(10);
    private JTextField xField=new JTextField(20);
    private JTextField yField=new JTextField(20);
    private float slope;
    private float x_intercept;
    private float y_intercept;

    private java.util.List<Float> xCoordinates = new ArrayList<Float>();
    private java.util.List<Float> yCoordinates = new ArrayList<Float>();
    private JFrame mainFrame=new JFrame("Best Fit Line");

	public void prepareGUI(){

        mainFrame.setLocation(500,250);
		mainFrame.setLayout(new GridLayout(6,1));
        mainFrame.setResizable(false);
		JPanel header=new JPanel();
		JLabel headerLabel=new JLabel("Find the line that fits best among the given points");
		//headerLabel.setForeground(new Color(92,244,66));
		header.add(headerLabel);
		header.setBackground(new Color(209, 234, 65));
		header.setFont(new Font("Courier New", Font.BOLD, 35));

		JPanel x_coord=new JPanel();
		// JTextField x1=new JTextField(10);
		JLabel xLabel=new JLabel("x-coordinate");
		//xLabel.setForeground(new Color(92,244,66));
		x_coord.add(xLabel);
		x_coord.add(x1);
		x_coord.setBackground(new Color(209, 234, 65));
		x_coord.setFont(new Font("Courier New", Font.PLAIN, 15));

		JPanel y_coord=new JPanel();
		// JTextField y1=new JTextField(10);
		JLabel yLabel=new JLabel("y-coordinate");
		//yLabel.setForeground(new Color(92,244,66));
		y_coord.add(yLabel);
		y_coord.add(y1);
		y_coord.setBackground(new Color(209, 234, 65));
		y_coord.setFont(new Font("Courier New", Font.PLAIN, 15));

		JPanel coordinates=new JPanel();
		coordinates.setBackground(new Color(209, 234, 65));
		// JTextField xField=new JTextField(20);
		// JTextField yField=new JTextField(20);
		JLabel x=new JLabel("x-coordinates so far:");
		JLabel y=new JLabel("y-coordinates so far:");
		coordinates.add(x);
		coordinates.add(xField);
		coordinates.add(y);
		coordinates.add(yField);
		coordinates.setBackground(new Color(209, 234, 65));

        xField.setEditable(false);
        yField.setEditable(false);

		JPanel buttons=new JPanel();
		JButton submit=new JButton("Submit");
		submit.setBackground(new Color(41,41,209));
		submit.setForeground(new Color(92,244,66));
		JButton show=new JButton("Show slope and intercept");
		show.setBackground(new Color(41, 41, 209));
		show.setForeground(new Color(92,244,66));
		JButton clr=new JButton("Clear all");
		clr.setBackground(new Color(41, 41, 209));
		clr.setForeground(new Color(92,244,66));
		buttons.add(submit);
		buttons.add(show);
		buttons.add(clr);
		buttons.setBackground(new Color(209, 234, 65));
		buttons.setFont(new Font("Courier New", Font.PLAIN, 10));

		JPanel back=new JPanel();
		JButton backButton=new JButton("Back");
		back.add(backButton);
		backButton.setBackground(new Color(186,35,27));
		back.setBackground(new Color(209, 234, 65));
		backButton.setForeground(new Color(92,244,66));
		back.setFont(new Font("Courier New", Font.PLAIN, 10));

        submit.addActionListener(new ButtonClickListener());
        backButton.addActionListener(new ButtonClickListener());
        show.addActionListener(new ButtonClickListener());
        clr.addActionListener(new ButtonClickListener());

		mainFrame.add(header);
		mainFrame.add(x_coord);
		mainFrame.add(y_coord);
		mainFrame.add(coordinates);
		mainFrame.add(buttons);
		mainFrame.add(back);

		mainFrame.setSize(850,500);
		mainFrame.setVisible(true);
		//Container c = mainFrame.getContentPane();
		//mainFrame.setBackground(new Color(2,30,36));
		mainFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

		backButton.addActionListener(new ActionListener()
		{
			public void actionPerformed(ActionEvent e)
			{
				mainFrame.setVisible(false);
				Calculator calc=new Calculator();
			}
		});
	}



    private class ButtonClickListener implements ActionListener{

		private String buttonCommand;

        public void actionPerformed(ActionEvent e) {

			buttonCommand = e.getActionCommand();

			if(buttonCommand.equals("Submit")){

                try{

                    String xText = x1.getText();
                    String yText = y1.getText();

                    if(xText.isEmpty() || yText.isEmpty()){
                        JOptionPane.showMessageDialog(mainFrame, "Invalid input");
                        return;
                    }

                    float xInput = Float.parseFloat(xText);
                    float yInput = Float.parseFloat(yText);
                    System.out.println("X input = " + xInput);
                    System.out.println("X input = " + yInput);

                    xCoordinates.add(xInput);
                    yCoordinates.add(yInput);

                    int count = 0;

                    // for testing
                    while(count<xCoordinates.size()){
                        System.out.println("x = " + xCoordinates.get(count) + "\ty = " + yCoordinates.get(count));
                        count++;
                    }

                    numberOfPoints++;
                    xField.setText(xField.getText() + xCoordinates.get(numberOfPoints-1) + ", ");
                    yField.setText(yField.getText() + yCoordinates.get(numberOfPoints-1) + ", ");
                }
                catch(Exception exc){
                    System.out.println(exc);
                    JOptionPane.showMessageDialog(mainFrame, "Invalid input");
                    return;
                }

                x1.setText("");
                y1.setText("");
            }

            else if(buttonCommand.equals("Show slope and intercept")){

                if(numberOfPoints == 0) System.out.println("aa");
                calculateBestFitLine();
                String resultString = "slope = " + slope + "\ny-intercept = " + y_intercept + "\nx-intercept = " + x_intercept;

                System.out.println(resultString);
                JOptionPane.showMessageDialog(mainFrame, resultString);
            }

            else if(buttonCommand.equals("Clear all")){

                numberOfPoints = 0;
                x1.setText("");
                y1.setText("");
                xField.setText("");
                yField.setText("");
                xCoordinates = new ArrayList<Float>();
                yCoordinates = new ArrayList<Float>();
            }

       }

       private void calculateBestFitLine(){

           float xSum=0, ySum=0, xMean, yMean, numr = 0, denr = 0;
           for(int i=0;i<numberOfPoints;i++){
               xSum += xCoordinates.get(i);
               ySum += yCoordinates.get(i);
           }

           xMean = xSum/numberOfPoints;
           yMean = ySum/numberOfPoints;

           for(int i=0;i<numberOfPoints;i++){
               numr += (xCoordinates.get(i) - xMean)*yCoordinates.get(i);
               denr+=(xCoordinates.get(i)-xMean)*(xCoordinates.get(i)-xMean);
           }

           slope = numr/denr;
           y_intercept = yMean - xMean*slope;
           x_intercept = -y_intercept/slope;
       }
    }
}
