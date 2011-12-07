package net.changethis.traffic;

import java.util.ArrayList;

public class Node
{
	private static ArrayList<Node> nodelist;
	public static int maxid=1;
	
	public int id;
	public ArrayList<Node> connections;
	
	
	public Node()
	{
		id=maxid;
		maxid++;
		nodelist.add(id,this);
		if(maxid>1000000000) throw new IndexOutOfBoundsException("Too many nodes!!! Bad map!");
	}
	
	public static Node idGet(int id)
	{
		if(id<=0) throw new NullPointerException("Attempt to get Node ID < 1");
		return nodelist.get(id);
	}
	
	public void addConnection(Node other)//for maps
	{
		this.connections.add(other);
	}
	public void addConnection(int other) { addConnection(nodelist.get(other)); }
	
	static
	{
		nodelist = new ArrayList<Node>();
		nodelist.add(0,(Node)null);
	}
}
