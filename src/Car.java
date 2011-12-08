package net.changethis.traffic;

public class Car
{
	int destination;
	int last;
	Route route;
	Road currentroad;
	float renderx;
	float rendery;
	double yaw;
	
	public Car(int start,int dest)
	{
		last = start;
		destination = dest;
	}
	public int getDestination()
	{ return destination; }
	public int getCurrentNode()
	{ return last; }
	
	void overrideRoute(int next) // should ONLY call from traffic lights
	{
		route.overrideRoute(last,next,destination);
	}
}
