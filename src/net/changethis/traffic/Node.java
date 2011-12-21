package net.changethis.traffic;

import java.util.ArrayList;
import java.util.TreeMap;
import java.io.File;

public class Node extends Renderable
{
	int id;
	ArrayList<Node> connections;
	public TreeMap<Node,Road> roadmap = new TreeMap<Node,Road>(NodeComparator.instance);
	private IJunction manager;
        boolean ready = false;
	
	private static ArrayList<Node> nodelist;
	public static int maxid=1;

	public Node(IJunction inter)
	{
                this.manager = inter; 
	}
	public Node setLocation(float x, float y, File tex, float scale)
        {
            this.posx = x;
            this.posy = y;
            this.texture = tex;
            this.texscale = scale;
            return this;
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
