package net.changethis.traffic;

import java.io.File;

public class Car implements IRenderable
{
	float posx;
	float posy;
	float rotyaw;
	File texture;
	float texscale;

	
	int destination;
	int last;
	Node nextNode,lastNode,destNode;
	Route route;
	Road curRoad;

	float forwardMotion, sideMotion, yawMotion;
	float forwardPos, sidePos;
	protected final float acceleration = 0.3f;
	protected final float deceleration = 0.5f;
	MovementDescriptor motionType = MovementDescriptor.STOP;
	int desiredLane, currentLane;
	
	public Car(int start,int dest)
	{
		last = start;
		lastNode = Node.idGet(start);
		nextNode = null;
		destNode = Node.idGet(dest);
		destination = dest;
	}
	public int getDestinationId()
	{
		return destination;
	}
	public Node getLastNode()
	{
		return lastNode;
	}
	public Node getNextNode()
	{
		return nextNode;
	}
	public Node getDestNode()
	{
		return lastNode;
	}
	public void popNextNode() // called when passing to new road, from lights
	{
		lastNode = nextNode;
		nextNode = route.getNextNode(lastNode);
		curRoad = lastNode.getConnectionRoad(nextNode);
	}
	
	void overrideRoute(int next) // should ONLY call from traffic lights
	{
		route.overrideRoute(last,next,destination);
	}
}
