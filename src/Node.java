package net.changethis.traffic;

import java.util.ArrayList;
import java.util.TreeMap;
import java.io.File;

public class Node implements IRenderable
{
	int id;
	ArrayList<Node> connections;
	TreeMap<Node,Road> roadmap = new TreeMap<>(NodeComparator.instance);
	IJunction manager;

	float posx;
	float posy;
	float rotyaw;
	File texture;
	float texscale;
	
	private static ArrayList<Node> nodelist;
	public static int maxid=1;

	public Node()
	{
		id=maxid;
		maxid++;
		nodelist.add(id,this);
		if(maxid>1000000000) throw new BadMapException("Too many nodes!!! Bad map!");
	}
	
	public Node(IJunction mgr)
	{
		this();
		manager = mgr;
	}
	
	public void setManager(IJunction mgr)
	{
		if(manager != null)
		{
			throw new UnsupportedOperationException("I'll get to this later");
		}
		manager = mgr;
	}
	
	public static Node idGet(int id)
	{
		if(id<=0) throw new ArrayIndexOutOfBoundsException("Attempt to get Node ID < 1");
		return nodelist.get(id);
	}
	
	public boolean equals(Node other)
	{
	
		return id == other.id;
	}

	public void addConnection(int other, double dist, double speed) { addConnection(idGet(other),dist,speed); }

	public void addConnection(Node other, double dist, double speed)
	 throws BadMapException
	{
		// If we aren't building the map right now
		if(!World.mapinit) throw new IllegalArgumentException("Connections may not be added except during map initialization");
		// If we already are connected to the other node
		if(roadmap.containsKey(other)) throw new BadMapException("Please only add a connection once.");
		
		connections.add(other);
		Road newroad = new Road(this, other, dist, speed);
		roadmap.put(other,newroad);
	}
	private void addConnection(Node n1, Road r1)
	{
		connections.add(n1);
		roadmap.put(n1,r1);
	}

	public double getDist(Node other)
	{
		Road lroad = roadmap.get(other);
		return lroad.distance;
	}

	public Road getConnectionRoad(Node other)
	{
		return roadmap.get(other);
	}

	static
	{
		nodelist = new ArrayList<Node>();
		nodelist.add(0,(Node)null);
	}
}
