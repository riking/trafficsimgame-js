package net.changethis.traffic;

import java.util.*;

public class RoutingThread extends Thread
{
	Node cur, con, start, end;
	Node[] links;
	double[] distarray;
	byte[] visitstatus;
	short stopcount;
	boolean dontstop;
	ListIterator liter;
	static short extraIters = 5;
	public RoutingThread(BareRoute br)
	{
		links = new Node[Node.maxid];
		distarray = new double[Node.maxid];
		visitstatus = new byte[Node.maxid];
		start=Node.getId(br.routeStart);
		end=Node.getId(br.routeEnd);
	}
	public void run()
	{
		/** Visit Status array
		 * 0 = unknown
		 * 1 = queued
		 * 2 = finished
		 */
		stopcount = 0;
		visitstatus[start.id] = 1;
		while(stopcount < extraIters)
		{
			dontstop = false;
			for(int i = 1; i < Node.maxid; i++) // Start at 1 because node 0 is NPE (by design)
			{
				if(visitstatus[i] == 1)
				{
					cur = Node.getId(i);
					liter = cur.connections.listIterator();
					while(liter.hasNext())
					{
						con = liter.next();
						if(visitstatus[con.id] == 0)
						{
							visitstatus[con.id] = 1;
							distarray[con.id] = distarray[i] + cur.getDist(con);
							links[con.id] = cur;
						}
						else if (distarray[con.id] > distarray[i] + cur.getDist(con))
						{
							distarray[con.id] = distarray[i] + cur.getDist(con);
							links[con.id] = cur;
							if(visitstatus[con.id] == 2)
								dontstop = true;
							visitstatus[con.id] = 1;
						}
					}
					visitstatus[i] = 2;
				}
			}
			if(visitstatus[end.id] == 2 && !dontstop)
			{
				stopcount++;
			}
		}
		//build route
	}
}
