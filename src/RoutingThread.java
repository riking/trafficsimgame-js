package net.changethis.traffic;

import net.changethis.traffic.Node;
import net.changethis.traffic.World;
import java.util.LinkedList;

public class RoutingThread extends Thread
{
	Node pointA;
	Node pointB;
	LinkedList<Node> fromStart;
	LinkedList<Node> fromEnd;
	BareRoute arg;
	public RoutingThread(BareRoute br)
	{
		arg=br;
		pointB=Node.nodelist.get(br.routeStart);
		pointA=Node.nodelist.get(br.routeEnd);
		fromStart=new LinkedList<Node>();
		fromEnd=new LinkedList<Node>();
		fromStart.add(pointA);
		fromEnd.add(pointB);
	}
	public void run()
	{
		
		int i=5+6;//filler code
		/*}
		fromEnd.removeFirst();
		fromStart.addAll(fromEnd);
		*/
		/*
		Route ret = new Route(fromStart);
		RoutingManager.taskDone(br,ret);
		*/
	}
}
