package net.changethis.traffic;

import java.util.ArrayList;

public class Node
{
	public static List<Node> nodelist;
	static
	{
		nodelist = new ArrayList<Node>();
	}
	
	public static Node getById(long id)
	{
		return nodelist[id];
	}
}
