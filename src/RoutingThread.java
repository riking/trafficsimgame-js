package net.changethis.traffic;

import java.util.*;

public class RoutingThread extends Thread
{
	Node pointA;
	Node pointB;
	LinkedList<Node> fromStart;
	LinkedList<Node> fromEnd;
	BareRoute arg;
	static int maxiter=30;
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
		
	}
	public void check()
	{}
}
