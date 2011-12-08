package net.changethis.traffic;

public class Road
{
	private Node nodeA;
	private Node nodeB;
	double distance;
	double speed;
	
	public Road(Node n1, Node n2)
	{
		nodeA = n1;
		nodeB = n2;
		distance = World.defaultdist;
		speed = World.defaultspeed;
	}
	public Road(Node n1, Node n2, double dist, double spd)
	{
		nodeA = n1;
		nodeB = n2;
		distance = dist;
		speed = spd;
	}
	public Node getEndpoint() { return nodeA; }
	public Node getEndpoint(int id)
	{
		if(nodeA.id==id) return nodeB;
		return nodeA;
	}
	public Node getEndpoint(Node other)
	{
		if(nodeA.equals(other)) return nodeB;
		return nodeA;
	}
	public boolean equals(Road r)
	{
		if (r.getEndpoint(nodeA) == nodeB)
			if (r.getEndpoint(nodeB) == nodeA)
				return true;
		return false;
	}
}
