import world,cars

class CarGenNode (world.Node):
	def __init__(self,position,cartype = cars.baseCarType, delay=20):
		world.Node.__init__(self,position)
		self.delay = delay
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
			
		
	def tick(self,node,map,rand):
		self.onTick(node,map,rand)
		
	def onTick(self,node,map,rand):
		pass
	
	def laneSort(self,car,road,map):
		return NotImplemented
	
	def carArrived(self,car,road,map):
		return NotImplemented
	
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
	
	def carArrived(self,car,road,map):
		self.passCar(self.parent,car,road,map)
		
	def laneSort(self,car,road,map):
		return 0
		
