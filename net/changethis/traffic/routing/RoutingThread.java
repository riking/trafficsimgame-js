package net.changethis.traffic.routing;

import java.util.Array

public class RoutingThread extends Thread
{
	long start;
	long end;
	LinkedList<long> fromStart;
	LinkedList<long> fromEnd;
	public RoutingThread(long begin,long en)
	{
		start=begin;
		end=en;
		fromStart=new LinkedList<long>();
		fromEnd=new LinkedList<long>();
		fromStart.offerFirst(begin);
		fromEnd.offerLast(end);
	}
}
