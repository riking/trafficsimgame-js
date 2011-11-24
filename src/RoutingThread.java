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
		ListIterator lia=pointA.nodelist.listIterator();
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
	public void check()
	{}
}
