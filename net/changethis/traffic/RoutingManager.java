package net.changethis.traffic;

import java.util.HashMap;
import net.changethis.traffic.routing.*;
import java.util.concurrent.ConcurrentHashMap;

public class RoutingManager
{
	public static ConcurrentHashMap<BareRoute,Route> routeHashes;

	public static void onMapLoaded()
	{
		//buildRoute(??name??,false);
	}
	public static Route getRoute(Car ca,long current)
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
	}
}
