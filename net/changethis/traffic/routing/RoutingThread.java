package net.changethis.traffic.routing;

import net.changethis.traffic.Node;
import net.changethis.traffic.World;
import java.util.LinkedList;

public class RoutingThread extends Thread
{
	Node pointA;
	Node pointB;
	LinkedList<Node> fromStart;
	LinkedList<Node> fromEnd;
	public RoutingThread(BareRoute br)
	{
		pointB=Node.nodelist.get(br.routeStart);
		pointA=Node.nodelist.get(br.routeEnd);
		fromStart=new LinkedList<Node>();
		fromEnd=new LinkedList<Node>();
		fromStart.offerFirst(pointA);
		fromEnd.offerLast(pointB);
	}
	public void run()
	{
		int i=5+6;//filler code
	}
}
