package net.changethis.traffic;

import java.util.*;

public class Route
{
	public Node routeStart;
	public Node routeEnd;
	public LinkedList<Node> routeList = new LinkedList<Node>();
	public Route(Collection<Node> theRoute)
	{
		routeList.addAll(theRoute);
		routeStart=routeList.getFirst();
		routeEnd=routeList.getLast();
	}
	public void overrideRoute(Collection<Node> replacement) // MANUAL user adjustment
	throws IllegalArgumentException
	{
		LinkedList<Node> rep = new LinkedList<Node>(replacement);
		if((rep.getLast() != routeEnd) || (rep.getFirst != routeStart))
		{
			throw new IllegalArgumentException("Inconsistent starting and ending points");
		}
		routeList.clear();
		routeList.addAll(replacement);
		
	}
	public Node getNextNode(Node n)
	{
		return routeList.get(routeList.indexOf(n)+1);
	}
}
