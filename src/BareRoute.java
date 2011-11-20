package net.changethis.traffic;

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
	public BareRoute(BareRoute o)
	{
		routeStart=o.routeStart;
		routeEnd=o.routeEnd;
	}
}
