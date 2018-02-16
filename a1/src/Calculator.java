import java.awt.Button;
import java.awt.GridBagConstraints;
import java.awt.GridBagLayout;
import java.awt.Insets;
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import javax.script.ScriptException;


public class Calculator{

	Calculator(){
		prepareGUI();
	}

	private JFrame mainFrame = new JFrame("Calculator");
	private JTextField input=new JTextField();
	private JTextField output=new JTextField();

	public void prepareGUI(){


		mainFrame.setSize(400,400);
		mainFrame.setResizable(false);
		mainFrame.setLocation(500,250);
		GridBagLayout layout = new GridBagLayout();

		mainFrame.setLayout(layout);
		JButton one=new JButton("1");
		JButton two=new JButton("2");
		JButton three=new JButton("3");
		JButton four=new JButton("4");
		JButton five=new JButton("5");
		JButton six=new JButton("6");
		JButton seven=new JButton("7");
		JButton eight=new JButton("8");
		JButton nine=new JButton("9");
		JButton zero=new JButton("0");
		JButton equalButton=new JButton("=");
		JButton multiply=new JButton("*");
		JButton divide=new JButton("/");
		JButton addition=new JButton("+");
		JButton minus=new JButton("-");
		JButton modulo=new JButton("%");
		JButton special=new JButton("Best Fit Line");
		JButton backspace=new JButton("Backspace");
		JButton clr=new JButton("CLR");
		JButton decimal=new JButton(".");
		JButton openBracket=new JButton("(");
		JButton closedBracket=new JButton(")");

		one.addActionListener(new ButtonClickListener());
		two.addActionListener(new ButtonClickListener());
		three.addActionListener(new ButtonClickListener());
		four.addActionListener(new ButtonClickListener());
		five.addActionListener(new ButtonClickListener());
		six.addActionListener(new ButtonClickListener());
		seven.addActionListener(new ButtonClickListener());
		eight.addActionListener(new ButtonClickListener());
		nine.addActionListener(new ButtonClickListener());
		zero.addActionListener(new ButtonClickListener());
		equalButton.addActionListener(new ButtonClickListener());
		multiply.addActionListener(new ButtonClickListener());
		divide.addActionListener(new ButtonClickListener());
		addition.addActionListener(new ButtonClickListener());
		minus.addActionListener(new ButtonClickListener());
		modulo.addActionListener(new ButtonClickListener());
		special.addActionListener(new ButtonClickListener());
		backspace.addActionListener(new ButtonClickListener());
		clr.addActionListener(new ButtonClickListener());
		decimal.addActionListener(new ButtonClickListener());
		openBracket.addActionListener(new ButtonClickListener());
		closedBracket.addActionListener(new ButtonClickListener());

		// JTextArea input=new JTextArea();
		// JTextArea output=new JTextArea();

		GridBagConstraints gbc = new GridBagConstraints();
		gbc.fill = GridBagConstraints.HORIZONTAL;
		gbc.gridx = 0;
		gbc.gridy = 0;
		gbc.gridwidth=7;
		gbc.ipady=20;
		gbc.insets=new Insets(0,0,5,0);
		input.setEditable(true);
		mainFrame.add(input,gbc);

		gbc.fill = GridBagConstraints.HORIZONTAL;
		gbc.gridx=0;
		gbc.gridy=1;
		gbc.gridwidth=7;
		gbc.ipady=15;
		gbc.insets=new Insets(0,0,5,0);
		output.setEditable(false);
		mainFrame.add(output,gbc);

		gbc.fill = GridBagConstraints.HORIZONTAL;
		gbc.gridx=0;
		gbc.gridy=2;
		gbc.gridwidth=1;
		gbc.insets=new Insets(2,2,2,2);
		mainFrame.add(seven,gbc);

		gbc.fill = GridBagConstraints.HORIZONTAL;
		gbc.gridx=1;
		gbc.gridy=2;
		gbc.gridwidth=1;
		gbc.insets=new Insets(2,2,2,2);
		mainFrame.add(eight,gbc);

		gbc.fill = GridBagConstraints.HORIZONTAL;
		gbc.gridx=2;
		gbc.gridy=2;
		gbc.gridwidth=1;
		gbc.insets=new Insets(2,2,2,2);
		mainFrame.add(nine,gbc);

		gbc.fill = GridBagConstraints.HORIZONTAL;
		gbc.gridx=0;
		gbc.gridy=3;
		gbc.gridwidth=1;
		gbc.insets=new Insets(2,2,2,2);
		mainFrame.add(four,gbc);

		gbc.fill = GridBagConstraints.HORIZONTAL;
		gbc.gridx=1;
		gbc.gridy=3;
		gbc.gridwidth=1;
		gbc.insets=new Insets(2,2,2,2);
		mainFrame.add(five,gbc);

		gbc.fill = GridBagConstraints.HORIZONTAL;
		gbc.gridx=2;
		gbc.gridy=3;
		gbc.gridwidth=1;
		gbc.insets=new Insets(2,2,2,2);
		mainFrame.add(six,gbc);

		gbc.fill = GridBagConstraints.HORIZONTAL;
		gbc.gridx=0;
		gbc.gridy=4;
		gbc.gridwidth=1;
		gbc.insets=new Insets(2,2,2,2);
		mainFrame.add(one,gbc);

		gbc.fill = GridBagConstraints.HORIZONTAL;
		gbc.gridx=1;
		gbc.gridy=4;
		gbc.gridwidth=1;
		gbc.insets=new Insets(2,2,2,2);
		mainFrame.add(two,gbc);

		gbc.fill = GridBagConstraints.HORIZONTAL;
		gbc.gridx=2;
		gbc.gridy=4;
		gbc.gridwidth=1;
		gbc.insets=new Insets(2,2,2,2);
		mainFrame.add(three,gbc);

		gbc.fill = GridBagConstraints.HORIZONTAL;
		gbc.gridx=0;
		gbc.gridy=5;
		gbc.gridwidth=1;
		gbc.insets=new Insets(2,2,2,2);
		mainFrame.add(decimal,gbc);

		gbc.fill = GridBagConstraints.HORIZONTAL;
		gbc.gridx=1;
		gbc.gridy=5;
		gbc.gridwidth=1;
		gbc.insets=new Insets(2,2,2,2);
		mainFrame.add(zero,gbc);

		gbc.fill = GridBagConstraints.HORIZONTAL;
		gbc.gridx=2;
		gbc.gridy=5;
		gbc.gridwidth=1;
		gbc.insets=new Insets(2,2,2,2);
		equalButton.setBackground(new Color(239,116,50));
		mainFrame.add(equalButton,gbc);

		gbc.fill = GridBagConstraints.HORIZONTAL;
		gbc.gridx=3;
		gbc.gridy=2;
		gbc.gridwidth=4;
		gbc.insets=new Insets(2,2,2,2);
		clr.setBackground(new Color(66,155,244));
		mainFrame.add(clr,gbc);

		gbc.fill = GridBagConstraints.HORIZONTAL;
		gbc.gridx=3;
		gbc.gridy=3;
		gbc.gridwidth=2;
		gbc.insets=new Insets(2,2,2,2);
		multiply.setBackground(new Color(208,239,50));
		mainFrame.add(multiply,gbc);

		gbc.fill = GridBagConstraints.HORIZONTAL;
		gbc.gridx=5;
		gbc.gridy=3;
		gbc.gridwidth=1;
		gbc.insets=new Insets(2,2,2,2);
		gbc.ipadx=3;
		divide.setBackground(new Color(208,239,50));
		mainFrame.add(divide,gbc);

		gbc.fill = GridBagConstraints.HORIZONTAL;
		gbc.gridx=6;
		gbc.gridy=3;
		gbc.gridwidth=1;
		gbc.insets=new Insets(2,2,2,2);
		mainFrame.add(openBracket,gbc);

		gbc.fill = GridBagConstraints.HORIZONTAL;
		gbc.gridx=3;
		gbc.gridy=4;
		gbc.gridwidth=2;
		gbc.insets=new Insets(2,2,2,2);
		addition.setBackground(new Color(208,239,50));
		mainFrame.add(addition,gbc);

		gbc.fill = GridBagConstraints.HORIZONTAL;
		gbc.gridx=5;
		gbc.gridy=4;
		gbc.gridwidth=1;
		gbc.insets=new Insets(2,2,2,2);
		gbc.ipadx=3;
		minus.setBackground(new Color(208,239,50));
		mainFrame.add(minus,gbc);

		gbc.fill = GridBagConstraints.HORIZONTAL;
		gbc.gridx=6;
		gbc.gridy=4;
		gbc.gridwidth=1;
		gbc.insets=new Insets(2,2,2,2);
		mainFrame.add(closedBracket,gbc);

		gbc.fill = GridBagConstraints.HORIZONTAL;
		gbc.gridx=3;
		gbc.gridy=5;
		gbc.gridwidth=2;
		gbc.insets=new Insets(2,2,2,2);
		modulo.setBackground(new Color(208,239,50));
		mainFrame.add(modulo,gbc);

		gbc.fill = GridBagConstraints.HORIZONTAL;
		gbc.gridx=5;
		gbc.gridy=5;
		gbc.gridwidth=2;
		gbc.insets=new Insets(2,2,2,2);
		backspace.setBackground(new Color(66,155,244));
		mainFrame.add(backspace,gbc);

		gbc.fill = GridBagConstraints.HORIZONTAL;
		gbc.gridx=0;
		gbc.gridy=6;
		gbc.gridwidth=7;
		gbc.insets=new Insets(2,2,2,2);
		special.setBackground(Color.GREEN);
		mainFrame.add(special,gbc);

		mainFrame.setVisible(true);
		Container c = mainFrame.getContentPane();
		c.setBackground(new Color(2,30,36));
		mainFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

		// special.addActionListener(new ActionListener()
		// {
		// 	public void actionPerformed(ActionEvent e)
		// 	{
		// 		mainFrame.setVisible(false);
		// 		specialFunction s=new specialFunction();
		// 		s.prepareGUI();
		// 	}
		// });
	}

	private class ButtonClickListener implements ActionListener{

		private String buttonCommand;

        public void actionPerformed(ActionEvent e) {

			buttonCommand = e.getActionCommand();

			if(buttonCommand.equals("Backspace")){
				try{input.getDocument().remove(input.getDocument().getLength() - 1,1);}
				catch(Exception ef){}
			}

			else if(buttonCommand.equals("CLR")){
				input.setText("");
				output.setText("");
			}

			else if(buttonCommand.equals("Best Fit Line")){
				mainFrame.setVisible(false);
				BestFitLine newFrame = new BestFitLine();
			}
			else if(!buttonCommand.equals("="))
				input.setText( input.getText() + buttonCommand);

			try{
				Evaluator eval = new Evaluator();
				String res = eval.evaluate(input.getText());
				output.setText("");
				if(!res.equals("null"))
					output.setText(res);
			}
			catch(ScriptException se){
				output.setText("Invalid input");
			}
			catch(Exception otherException){
				System.out.println(otherException);
			}
       }
	}

	// class NoTouchOutput extends Thread {
	//
	// 	public void run(){
	// 		while(true){
	//
	// 			try{
	//
	// 				Evaluator eval = new Evaluator();
	// 				try{
	// 					String res = eval.evaluate(input.getText());
	// 					output.setText("");
	// 					if(!res.equals("null"))
	// 						output.setText(res);
	// 				}
	// 				catch(Exception ex){
	// 					output.setText("Invalid input");
	// 				}
	// 				Thread.sleep(200);
	// 				notifyAll();
	// 			}
	// 			catch(Exception ej){System.out.println("a");}
	// 		}
	// 	}
	// }

}
