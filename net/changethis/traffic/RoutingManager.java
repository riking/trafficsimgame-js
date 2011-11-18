package net.changethis.traffic;

import java.util.HashMap;
import net.changethis.traffic.routing.*;
import java.util.concurrent.ConcurrentHashMap;

public class RoutingManager
{
	public static ConcurrentHashMap<BareRoute,Route> routeHashes;

	public static void onMapLoaded()
	{
		//buildRoute(baseroute,false);
	}
	public static Route getRoute(Car ca,Node current)
	{
		return getRoute(ca,current.id);
	}
	public static Route getRoute(Car ca,int current)
	{
		BareRoute k=new BareRoute(current,ca.destination);
		if(routeHashes.containsKey(k))
		{
			return routeHashes.get(k);
		}
		else
		{
			return buildRoute(k,true);
		}
	}
	public static Route buildRoute(BareRoute bare)
	{ return buildRoute(bare,true);
	}
	public static Route buildRoute(BareRoute bare,boolean priority)
	{
		return null;
	}
}
