package net.changethis.traffic.routing;

import java.util.ArrayList;

public class Route
{
	public long routeStart;
	public long routeEnd;
	public List<long> routeList;
	public Route(Collection<long> theRoute) //hmm, need args for this.
	{
		routeList.addAll(theRoute);
	}
}
