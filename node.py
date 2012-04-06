import math

import vectors

import world
import cars

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
			self.imanager = ZeroWaitIntersection(self)
				
	
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
		r = world.Road(self,other)
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


class CarGenNode (Node):
	def __init__(self,position,cartype = None, delay=20):
		Node.__init__(self,position)
		self.delay = delay
		if not cartype:
			cartype = cars.baseCarType
		self.car = cartype
		self.tickcount = 1
		
	
	def onTick(self,map,rand):
		self.tickcount -= 1
		if self.tickcount <= 0:
			self.tickcount = self.delay
			dest = rand.choice(map.nodelist)
			if dest == self:
				return
			c = self.car(self,map,rand,)
			if not c.routeInit(self,map,rand):
				del c
				return
			self.carArrived(c,None,map)

#Lane Data
# dict ( Road, *1* )
# len(lanedata) = connection number
# *1* = list [*2*]
#len(*1*) = number of lanes
# *2* = binary flags
# *2* & (1>>lanedata.index(*1*))
# 
#############
#        A
#       /|\
#  --/       \---
#B ---       ---- D
#  --\       /---
#      \\|//
#       ||||
#       ||||
#       ||||
#        C
# { A : [1>>B & 1>>C & 1>>D], B:[1>>A,1>>D,1>>C], C:[1>>B,1>>B & 1>>A,1>>D,1>>D], D:[1>>C,1>>B,1>>A] }


class Intersection:
	def __init__(self,node,lanedata = None):
		self.parent = node
		if lanedata:
			pass
		
	def tick(self,node,map,rand):
		self.onTick(node,map,rand)
		
	def onTick(self,node,map,rand):
		pass
	
	def laneSort(self,car,road,map):
		raise NotImplementedError()
	
	def carArrived(self,parent,car,road,map):
		raise NotImplementedError()
	
	def passCar(self,node,car,roadfrom,map):
		nn = car.getNextNode(roadfrom,node,map)
		if nn not in node.connections.keys():
			nn = car.emergency_reroute(roadfrom,node,map)
			if nn not in node.connections.keys():
				#print("car.emergency_rereoute failed to give a valid next node, deleting car")
				car.cleanup()
				del car
				return
		node.connections[nn].addCarFrom(self,car)
		car.notifyRoadChange(node,nn,roadfrom,node.connections[nn],map)
	
	
class ZeroWaitIntersection (Intersection):
	def __init__(self,node):
		Intersection.__init__(self,node)
	
	def carArrived(self,parent,car,road,map):
		self.passCar(parent,car,road,map)
		
	def laneSort(self,car,road,map):
		return 0
		
