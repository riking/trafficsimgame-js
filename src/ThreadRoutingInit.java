package net.changethis.traffic;

import java.util.ArrayList;
import java.util.ListIterator;

class ThreadRoutingInit extends Thread
{
	byte depth;
	int cur;
	int end;
	public ThreadRoutingInit(byte d, int nodeStart, int nodeEnd)
	{
		depth=d;
		cur=nodeStart;
		end=nodeEnd;
	}
	public void run()
	{
		if (depth != 2) throw new UnsupportedOperationException("depths more than 2 not done yet");
		ArrayList<Node> temp = new ArrayList<Node>(4);
		Node other = null;
		Node second = null;
		for (;cur < end; cur++)
		{
			Node curNode=Node.idGet(cur);
			
			ListIterator<Node> iter1 = curNode.connections.listIterator();
			while(iter1.hasNext())
			{
				other = iter1.next();
				ListIterator<Node> iter2 = other.connections.listIterator();
				while(iter2.hasNext())
				{
					second = iter2.next();
					temp.add(curNode);
					temp.add(other);
					temp.add(second);
					RoutingManager.routeHashes.put(new BareRoute(curNode,second),new Route(temp));
					temp.clear();
				}
			}
		}
	}
}
