package net.changethis.traffic.routing;

import java.util.*;
import net.changethis.traffic.*;

public class Route
{
	public Node routeStart;
	public Node routeEnd;
	public List<Node> routeList;
	public Route(Collection<Node> theRoute) //hmm, need args for this.
	{
		routeList.addAll(theRoute);
	}
}
