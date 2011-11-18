package net.changethis.traffic.routing;

import net.changethis.traffic.*;

public class BareRoute
{
	public int routeStart;
	public int routeEnd;
	public BareRoute(Node start,Node end)
	{
		routeStart=start.id;
		routeEnd=end.id;
	}
	public BareRoute(int start,int end)
	{
		routeStart=start;
		routeEnd=end;
	}
}
