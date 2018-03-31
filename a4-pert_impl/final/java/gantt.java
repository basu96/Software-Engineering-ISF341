import java.awt.Button;
import java.awt.GridBagConstraints;
import java.awt.GridBagLayout;
import java.awt.Insets;
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTable;
import javax.swing.table.DefaultTableModel;
import javax.swing.table.TableModel;
import java.util.StringTokenizer;
import java.io.*;
import java.io.FileOutputStream;

public class gantt
{

	gantt()
	{
		prepareGUI();
	}
	private JFrame mainFrame = new JFrame("Crete Gantt Chart");

	public void prepareGUI()
	{
		mainFrame.setSize(800,750);
		mainFrame.setLayout(null);
		mainFrame.setLocation(0,0);
		JButton Create=new JButton("Create Gantt Chart");

		String[][] data={{"","","","",""}};
		String[] col={"Task Id","Task Name","Dependencies(Task Ids separated by space)","Duration","%Completed"};
    	final DefaultTableModel model = new DefaultTableModel(data, col);
    	JTable table = new JTable(model);
		JScrollPane sp=new JScrollPane(table);
		table.setAutoResizeMode(JTable.AUTO_RESIZE_OFF);
		table.getColumnModel().getColumn(0).setPreferredWidth(60);
		table.getColumnModel().getColumn(1).setPreferredWidth(80);
		table.getColumnModel().getColumn(2).setPreferredWidth(300);
		table.getColumnModel().getColumn(3).setPreferredWidth(100);
		table.getColumnModel().getColumn(4).setPreferredWidth(100);


		JPanel panel=new JPanel(new BorderLayout());
		panel.add(sp);
		panel.setBounds(80,80,640,500);
		int i=1;
		JButton addRow = new JButton("Add Empty Row");
    	addRow.addActionListener(new ActionListener()
    	{
      		public void actionPerformed(ActionEvent e)
      		{
        		model.addRow(new Object[] {});
      		}
    	});
    	panel.add(addRow, BorderLayout.SOUTH);
		mainFrame.add(panel);

		Create.setBounds(320,600,180,30);
		mainFrame.add(Create);

		Create.addActionListener(new ActionListener()
		{
			public void actionPerformed(ActionEvent e)
			{
				exportToCSV(table,"gantt_chart.csv");
				//System.out.println("1\n");
				writeToYS(table);
				//System.out.println("1\n");




				try{
            		java.lang.Runtime rt = java.lang.Runtime.getRuntime();
		          	java.lang.Process p = rt.exec("java Graph");
					System.out.println(p.getOutputStream());
			   }
		       catch(Exception e1){
		           System.out.println(e1);
		       }


				//////////////// python gantt and pert
				try{
            		java.lang.Runtime rt = java.lang.Runtime.getRuntime();
		          	java.lang.Process p = rt.exec("python3 sample-gantt.py");
		       }
		       catch(Exception e3){
		           System.out.println(e3);
		       }
			   ////////////////

				model.fireTableDataChanged();
				try
				{
					//Process p = Runtime.getRuntime().exec("javac *.java");
             Process p2 = Runtime.getRuntime().exec("java Graph");
				}
				catch(Exception e1)
				{
					System.out.println("Nahi Chalega bc");
				}
				//Graph g=new Graph("ys.txt");
				mainFrame.dispose();

			}
		});

		mainFrame.setVisible(true);
		Container c = mainFrame.getContentPane();
		c.setBackground(new Color(119,244,66));
		mainFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	}
	public static boolean exportToCSV(JTable tableToExport,String pathToExportTo)
	{

    try
    {

        TableModel model = tableToExport.getModel();
        FileWriter csv = new FileWriter(new File(pathToExportTo));

        for (int i = 0; i < model.getColumnCount(); i++) {
            csv.write(model.getColumnName(i) + ",");
        }

        csv.write("\n");

        for (int i = 0; i < model.getRowCount(); i++)
        {
            for (int j = 0; j < model.getColumnCount(); j++)
            {
            	csv.write(model.getValueAt(i, j) + ",");
            }
            csv.write("\n");
        }

        csv.close();
        return true;
    }
    catch (IOException e)
    {
        e.printStackTrace();
    }
    return false;
	}
	public void writeToYS(JTable table)
	{
		try
		{
			FileOutputStream fout=new FileOutputStream("ys.txt");
			TableModel model=table.getModel();
			String n=String.valueOf(model.getRowCount())+" ";
			byte[] b = n.getBytes();
			fout.write(b);
			int c=0;
			for(int i=0;i<model.getRowCount();i++)
			{
				String m=String.valueOf(model.getValueAt(i,2));
				int j=0;
				String x="";
				while(j<m.length())
				{
					if(m.charAt(j)!=' '||m.charAt(j)!='\n')
					{
						if(!String.valueOf(m.charAt(j)).equals(" ")&&!String.valueOf(m.charAt(j)).equals("n")&&!String.valueOf(m.charAt(j)).equals("u")&&!String.valueOf(m.charAt(j)).equals("l")&&!String.valueOf(m.charAt(j)).equals("l"))
						{
							c++;
						}
					}
					j++;
				}
			}
			String h=String.valueOf(c)+"\n";
			b=h.getBytes();
			fout.write(b);
			for(int i=0;i<model.getRowCount();i++)
			{
				String j=String.valueOf(model.getValueAt(i,3))+" ";
				b=j.getBytes();
				fout.write(b);
			}
			String t="\n";
			b=t.getBytes();
			fout.write(b);
			for(int i=0;i<model.getRowCount();i++)
			{
				String m=String.valueOf(model.getValueAt(i,2));
				int j=0;
				String x="";
				while(j<m.length())
				{
					if(m.charAt(j)!=' '||m.charAt(j)!='\n')
					{
						if(!String.valueOf(m.charAt(j)).equals(" ")&&!String.valueOf(m.charAt(j)).equals("n")&&!String.valueOf(m.charAt(j)).equals("u")&&!String.valueOf(m.charAt(j)).equals("l")&&!String.valueOf(m.charAt(j)).equals("l"))
						{
							//System.out.println(String.valueOf(m.charAt(j)));
							x=String.valueOf(m.charAt(j))+" ";
							b = x.getBytes();
							fout.write(b);
							x=String.valueOf(model.getValueAt(i,0))+"\n";
							b=x.getBytes();
							fout.write(b);

						}
					}
					j++;
					x="";
				}
				//System.out.println("3");
				//byte[] b = m.getBytes(Charset.forName("UTF-8"));
				//byte[] b = m.getBytes(StandardCharsets.UTF_8);
			}
			fout.close();
		}
		catch(Exception e)
		{
			System.out.println("Sorry file not found\n");
		}
	}
}
