package net.changethis.traffic;

public class Road
{
	private Node nodeA;
	private Node nodeB;
	public Node getEndpoint() { return nodeA; }
	public Node getEndpoint(int id)
	{
		if(nodeA.id==id) return nodeB;
		return nodeA;
	}
	public Node getEndpoint(Node other)
	{
		if(nodeA==other) return nodeB;
		return nodeA;
	}
}
