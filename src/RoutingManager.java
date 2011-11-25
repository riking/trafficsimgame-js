package net.changethis.traffic;

import java.util.HashMap;
import java.util.concurrent.ConcurrentHashMap;

public class RoutingManager
{
	public static ConcurrentHashMap<BareRoute,Route> routeHashes = new ConcurrentHashMap<>();


	public static void onMapLoaded()
	{
		
		//Add all 2-step routes. Note, need to figure out collisions (ie A>BC, B>D, C>D)
		float divisions=Node.maxid/4;
		ThreadRoutingInit[] threads = new ThreadRoutingInit[4];
		threads[0]=new ThreadRoutingInit(2, 1, (int)divisions+1);
		threads[1]=new ThreadRoutingInit(2, (int)divisions-1, (int)(divisions*2)+1);
		threads[2]=new ThreadRoutingInit(2, (int)(divisions*2)-1, (int)(divisions*3)+1);
		threads[3]=new ThreadRoutingInit(2, (int)(divisions*3)-1, Node.maxid);
		threads[0].start();
		threads[1].start();
		threads[2].start();
		threads[3].start();
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
