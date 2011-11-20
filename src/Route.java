package net.changethis.traffic;

import java.util.*;

public class Route
{
	public Node routeStart;
	public Node routeEnd;
	public List<Node> routeList;
	public Route(Collection<Node> theRoute)
	{
		routeList.addAll(theRoute);
	}
	public void overrideRoute(Collection<Node> replacement) //could be called from map. maybe.
	{
		routeList.clear();
		routeList.addAll(replacement);
	}
	public void overrideRoute(int current,int next,int destination) //called from cars
	{
		routeList.clear();
		routeList.add(Node.nodelist.get(current));
		Route r=RoutingManager.getRoute(new BareRoute(next,destination));
		routeList.addAll(r.routeList);
	}
}
