package net.changethis.traffic;

import java.util.ArrayList;

public class Node
{
	public static ArrayList<Node> nodelist;
	public int id;
	public static int maxid;

	public Node()
	{
		id=maxid;
		maxid++;
		if(maxid>1000000000) throw new IndexOutOfBoundsException("Too many nodes!!! Bad map!");
	}
	public static Node getById(int id)
	{
		return nodelist.get(id);
	}
	static
	{
		nodelist = new ArrayList<Node>();
	}
}