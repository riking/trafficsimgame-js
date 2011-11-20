package net.changethis.traffic;

public class Car
{
	int destination;
	Route route;
	int current;

	public void overrideRoute(int next) //can ONLY call from traffic lights
	{
		route.overrideRoute(current,next,destination);
	}
}
