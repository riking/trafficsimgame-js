from __future__ import division;
import math;
import random;
import vectors;

class Map:
	def __init__(self,siz):
		self.size = siz
		self.nodelist = []
	
	def __del__(self):
		for n in self.nodelist:
			n.cleanup()
		
	
	def makeNodes(self,density,roadrange,rand):
		for i in range(int(self.size * density)):
			q=Node((rand.randint(1,self.size), rand.randint(1,self.size)))
			for n in self.nodelist:
				if n.dist(q) < roadrange *2* density:
					break
			else:
				self.nodelist.append(q)
		return self
	
	def makeRoads(self,roadsize,roadchance,passes,rand):
		for i in range(passes):
			for n in self.nodelist:
				try:
					a=[]
					for m in self.nodelist: #get each node in range
						if n.dist(m) < roadsize:
							a.append(m)
					while rand.random() < roadchance: #maybe connect to them
						m = rand.choice(a)
						a.remove(m)
						n.addConnection(m)
				except IndexError:
					# if there's no nodes within roadrange, find the nearest other node
					
					t=None
					a=self.size**2 #distance to closest node
					for m in self.nodelist:
						d = n.dist(m)
						if d < a:
							a = d
							t = m
					if t==None:
						#hmmmmmmmmm........ does this mean that there is no nodes?
						print("attempted to add roads to node %s, no node in range." % n.coordstr())
						continue
					else:
						pass #print("made long-road from %s to %s" % (n.coordstr(),t.coordstr()))
		return self
	
	def print_(self):
		output_size = 40
		output_res = self.size / output_size
		#
		FILLER = 1
		ROAD = 2
		NODE = 3
		#
		output = []
		for i in range(output_size+1):
			output.append([])
			for j in range(output_size+1):
				output[i].append(FILLER)
		
		print("drawign roads")
		for n in self.nodelist:
			for r in n.connections.values():
				m = r.getNode(n)
				diff = (n.pos - m.pos)/20
				for i in range(20):
					tem = ((n.pos - diff*i)/output_res)._intvals()
					output[tem[0]][tem[1]] = ROAD
		
		print("drawing nodes")
		for n in self.nodelist:
			p = n.pos// output_res
			output[p[0]][p[1]] = NODE
		
		for i in range(output_size):
			print(''.join([(' ' if j==FILLER else ('+' if j==ROAD else ('#' if j==NODE else ' '))) for j in output[i]]))

		
class Node:
	#self.connections = {node: road, node: road}
	def __init__(self,position):
		self.pos = vectors.Vector(position)
		self.connections = {}
	
	def __eq__(self,other):
		if isinstance(other,Node):
			return self.pos == other.pos
		return False
		
	def __hash__(self):
		return self.pos.__hash__()
		
	def getPos(self):
		return self.pos
	
	def addConnection(self,other):
		r = Road(self,other)
		if other in self.connections.keys():
			return
		self.connections[other] = r
		other.addConnectionCB(self,r)
		
	def addConnectionCB(self,other,road):
		self.connections[other] = road
		
	def getRoad(self,other):
		if other in self.connections:
			return self.connections[other]
		return None
	
	def dist(self,other):
		return math.sqrt((self.pos[0] - other.pos[0])**2 + (self.pos[1] - other.pos[1])**2)

	def coordstr(self):
		return str(self.pos)
	
	def fullDescription(self):
		cstr = ""
		for c,r in self.connections.items():
			cstr += c.coordstr()
		return "Node at %s \nConnected to: %s" % (self.pos,cstr)
		
	def cleanup(self): #on map exit. clean up circular references
		try:
			for n,r in self.connections.items():
				r.cleanup()
			del self.connections
		except NameError as exc:
			pass #...then dump it
		
		
class Road:
	def __init__(self,n1,n2):
		self.node1 = n1
		self.node2 = n2
		self.distance = math.sqrt((n1.pos[0] - n2.pos[0])**2 + (n1.pos[1] - n2.pos[1])**2)
		self.cars = [[],[]]

	def addCar(self,origin,car):
		if origin == n1:
			self.cars[0].append(car)
		else:
			self.cars[1].append(car)
	
	def getNode(self,refnode=None):
		if self.node1 == refnode:
			return self.node2
		return self.node1
		
	def cleanup(self): #on map exit. clean up circular references
		try:
			del self.cars
			del self.node1
			del self.node2
		except NameError:
			pass #dump the error; this function will be called twice
		except AttribuiteError:
			pass #same

			
def mapGen(seed=None,size=2000,density=.3,roadrange=300,roadchance=.66,roadpasses=2):
	r = random.Random(seed)
	m = Map(size).makeNodes(density,roadrange,r).makeRoads(roadrange,roadchance,roadpasses,r)
	return m


if __name__ == "__main__":
	m = mapGen().print_()
	del m
	m = mapGen().print_()
	del m