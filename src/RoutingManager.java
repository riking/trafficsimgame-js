package net.changethis.traffic;

import java.util.HashMap;
import java.util.concurrent.ConcurrentHashMap;

public class RoutingManager
{
	public static ConcurrentHashMap<BareRoute,Route> routeHashes = new ConcurrentHashMap<>();


	public static void onMapLoaded()
	{
		//ThreadRoutingInit
	}
	public static Route getRoute(Car ca)
	{
		return getRoute(new BareRoute(ca.current,ca.destination));
	}
	public static Route getRoute(int current, int dest)
	{
		return getRoute(new BareRoute(current,dest));
	}
	public static Route getRoute(BareRoute k)
	{
		if(routeHashes.containsKey(k))
		{
			return routeHashes.get(k);
		}
		else
		{
			return buildRouteRealtime(new BareRoute(k));//cloned for "escape analysis", read http://docs.oracle.com/javase/7/docs/technotes/guides/vm/performance-enhancements-7.html 
		}
	}
	public static void buildRoute(BareRoute bare)
	{
		RoutingThread rt=new RoutingThread(bare);
		rt.start();
	}
	public static Route buildRouteRealtime(BareRoute bare)
	{
		RoutingThread rt=new RoutingThread(bare);
		rt.run();
		return routeHashes.get(bare);
	}
	public static void taskDone(BareRoute b, Route r)
	{
		routeHashes.put(b,r);
	}
}
