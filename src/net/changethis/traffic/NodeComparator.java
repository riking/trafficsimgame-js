package net.changethis.traffic;
import java.util.Comparator;
public class NodeComparator implements Comparator<Node>
{
	public static NodeComparator instance = new NodeComparator();
	public int compare(Node o1, Node o2)
	{
		return o2.id - o1.id;
	}
}
