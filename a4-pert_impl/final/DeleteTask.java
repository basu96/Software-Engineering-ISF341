import java.awt.Button;
import java.awt.GridBagConstraints;
import java.awt.GridBagLayout;
import java.awt.Insets;
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class DeleteTask
{
	DeleteTask()
	{
		prepareGUI();
	}
	private JFrame mainFrame = new JFrame("Delete a Task");

	public void prepareGUI()
	{
		mainFrame.setSize(300,300);
		GridBagLayout layout = new GridBagLayout();
		mainFrame.setLayout(layout);
		JLabel TaskId=new JLabel("Task Id:");
		JTextField TaskField=new JTextField();
		//TaskField.setPreferredSize(new Dimension(400,40));
		JButton DeleteButton=new JButton("Delete");
		JButton Back=new JButton("Back");

		GridBagConstraints gbc = new GridBagConstraints();
		gbc.fill = GridBagConstraints.HORIZONTAL;
		gbc.gridx=0;
		gbc.gridy=0;
		gbc.gridwidth=2;
		gbc.insets=new Insets(4,4,4,4);
		mainFrame.add(TaskId,gbc);


		gbc.fill = GridBagConstraints.HORIZONTAL;
		gbc.gridx=2;
		gbc.gridy=0;
		gbc.gridwidth=2;
		gbc.insets=new Insets(4,4,4,4);
		mainFrame.add(TaskField,gbc);

		
		gbc.fill = GridBagConstraints.HORIZONTAL;
		gbc.gridx=1;
		gbc.gridy=2;
		gbc.gridwidth=2;
		gbc.insets=new Insets(4,4,10,10);
		mainFrame.add(Back,gbc);

		
		gbc.fill = GridBagConstraints.HORIZONTAL;
		gbc.gridx=3;
		gbc.gridy=2;
		gbc.gridwidth=2;
		gbc.insets=new Insets(4,4,10,10);
		mainFrame.add(DeleteButton,gbc);

		Back.addActionListener(new ActionListener()
		{
			public void actionPerformed(ActionEvent e)
			{
				mainFrame.setVisible(false);
				gantt g=new gantt();
			}
		});

		mainFrame.setVisible(true);
		Container c = mainFrame.getContentPane();
		c.setBackground(new Color(119,244,66));
		mainFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	}
}