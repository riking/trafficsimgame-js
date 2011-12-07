package net.changethis.traffic;

import java.util.ListIterator;
import java.util.LinkedList;

public class RoutingTask implements Runnable
{
	Node cur, con, start, end;
	Route r;
	short stopcount;
	// Storage. Could be local variables, but nah.

	Node[] links;
	// Linked path to start node. Index is node ID.
	double[] distarray;
	// Distance from start to this node
	byte[] visitstatus;
	/* Values:
	 0 = 'Unknown'
	 1 = Queued
	 2 = Done
	 */
	ListIterator<Node> liter;
	BareRoute arg;

	static short extraIters = 3; // Extra steps allowed to make a better path once we find the finish.

	public RoutingTask(BareRoute br)
	{
		links = new Node[Node.maxid];
		distarray = new double[Node.maxid];
		visitstatus = new byte[Node.maxid];
		start = Node.idGet(br.routeStart);
		end = Node.idGet(br.routeEnd);
		arg = br;
	}

	public void run()
	{
		makeRoute();
		RoutingManager.taskDone(arg,r);
	}

	public Route runUrgent()
	{
		makeRoute();
		return r;
	}

	private void makeRoute() // 'Returns' through class variable r.
	{
		stopcount = 0;
		visitstatus[start.id] = 1;
		while(stopcount < extraIters)
		{
			for(int i = 1; i < Node.maxid; i++) // Start at 1 because node ID 0 is NPE (by design)
			{
				if(visitstatus[i] == 1)
				{
					cur = Node.idGet(i);
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
								stopcount = 0; // reset counter
							visitstatus[con.id] = 1;
						}
					}
					visitstatus[i] = 2;
				}
			}
			if(visitstatus[end.id] == 2) // If we've found the endpoint
			{
				stopcount++;
			}
		}
		LinkedList<Node> lee = new LinkedList<>();
		cur = end;
		for(cur = end; cur != start; lee.addFirst(cur), cur = links[cur.id])
		{} // Pray to your deity of choice that this works.
		lee.addFirst(start);
		r = new Route(lee);
	}
}
