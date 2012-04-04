from __future__ import division;
import math,random;
import vectors,cars,node;

class Map:
	def __init__(self,siz):
		self.size = siz
		self.nodelist = []
	
	def __del__(self):
		for n in self.nodelist:
			n.cleanup()
		
	def makeNodes(self,density,roadrange,rand):
		import node;
		for i in range(int(self.size * density)):
			q=None
			#should replace with a customizable weights function
			if rand.random() < 0.1:
				q=node.CarGenNode(((rand.randint(1,self.size), rand.randint(1,self.size))))
			else:
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
					m = rand.choice(a)
					a.remove(m)
					n.addConnection(m)
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
		FILLER = ' '
		ROAD = '+'
		NODE = '#'
		CAR = '>'
		#
		import array;
		output = []
		for i in range(output_size+1):
			output.append(array.array('u',[FILLER for j in range(output_size+1)]))
		
		print("drawing roads")
		for n in self.nodelist:
			for r in n.connections.values():
				m = r.getNode(n)
				diff = (n.pos - m.pos)/20
				for i in range(20):
					tem = (n.pos - diff*i)//output_res
					output[tem[0]][tem[1]] = ROAD
		
		print("drawing cars")
		for n in self.nodelist:
			for r in n.connections.values():
				for c in r.carList(n):
					p=c.getPosition()//output_res
					output[p[0]][p[1]] = CAR
		
		print("drawing nodes")
		for n in self.nodelist:
			p = n.pos// output_res
			output[p[0]][p[1]] = NODE
		
		
		# print output[]
		for i in range(output_size):
			print(''.join([j for j in output[i]]))
			

	def tick(self,rand):
		for n in self.nodelist:
			n.tick(self,rand)
	
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################

class Road:
	def __init__(self,n1,n2):
		self.node1 = n1
		self.node2 = n2
		self.distance = math.sqrt((n1.pos[0] - n2.pos[0])**2 + (n1.pos[1] - n2.pos[1])**2)
		self.cars = {n1:[],n2:[]}

	def getNode(self,refnode=None):
		return self.node2 if refnode==self.node1 else self.node1
		
	def carList(self,refnode=None):
		if not refnode:
			return self.cars
		else:
			return self.cars[refnode]
			
	def dist(self):
		return self.distance	

	def addCarFrom(self,onode,car):
		self.cars[self.getNode(onode)].append(car)
	
	def tick(self,onode,map,rand):
		self.onTick(onode,map)
		for car in self.cars[onode]:
			if car.tick(self,onode,map,rand):
				onode.carArrived(car,self,map)
				self.cars[onode].remove(car)
		
	def onTick(self,onode,map):
		pass #reserved for subclasses
		
	def cleanup(self): #on map exit. clean up circular references
		try:
			for a in self.cars:
				for c in a:
					try:
						c.cleanup()
					except (NameError, AttribuiteError):
						pass #dump it. this is because we're cleaning up circular references
			del self.cars
		except (NameError, AttribuiteError):
			pass #whee, circular references are fun!
		try:
			del self.node1
			del self.node2
		except (NameError, AttribuiteError):
			pass

###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################

class Node:
	#self.connections = {node: road, node: road}
	def __init__(self,position,connect=None,manager=None):
		self.pos = vectors.Vector(position)
		self.connections = {}
		if connect:
			for n in connect:
				self.addConnection(n)
		if manager:
			self.imanager = manager
		else:
			self.imanager = node.ZeroWaitIntersection(self)
				
	
	def __eq__(self,other):
		if isinstance(other,Node):
			return self.pos == other.pos
		if isinstance(other,vectors.Vector):
			return self.pos == other
		return NotImplemented
		
	def __ne__(self,other):
		if isinstance(other,Node):
			return self.pos != other.pos
		if isinstance(other,vectors.Vector):
			return self.pos != other
		return NotImplemented
		
	def __hash__(self):
		return self.pos.__hash__()
		
	def __str__(self):
		return str(self.pos)
		
	def __repr__(self):
		return "Node(%s,%s)"%(str(self.pos),len(self.connections))
		
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
	
	def tick(self,map,rand):
		self.onTick(map,rand)
		for r in self.connections.values():
			r.tick(self,map,rand)
	
	def onTick(self,map,rand):
		pass #Reserved for subclasses
		
	def carArrived(self,car,road,map):
		if self == car.destination():
			print("car arrived")
			print(car)
			car.cleanup()
			del car
			return #hopefully this will kill it
		self.imanager.carArrived(self,car,road,map)
	
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


###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################

def mapGen(seed=None,size=2000,density=.3,roadrange=300,roadchance=.4,roadpasses=2):
	r = random.Random(seed)
	m = Map(size).makeNodes(density,roadrange,r).makeRoads(roadrange,roadchance,roadpasses,r)
	return m,r
	
if __name__ == "__main__":
	m,r = mapGen()
	m.print_()
	import time
	for i in range(1000):
		m.tick(r)
		m.print_()
		time.sleep(0.5)


	
