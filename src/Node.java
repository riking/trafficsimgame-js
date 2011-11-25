package net.changethis.traffic;

import java.util.ArrayList;

public class Node
{
	public static ArrayList<Node> nodelist;
	public static int maxid=1;
	
	public int id;
	public ArrayList<Node> connections;
	
	
	public Node()
	{
		id=maxid;
		maxid++;
		if(maxid>1000000000) throw new IndexOutOfBoundsException("Too many nodes!!! Bad map!");
	}
	
	public static Node idGet(int id)
	{
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
	}
}
