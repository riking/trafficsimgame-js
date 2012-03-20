
import world

class Car:
	def __init__(self,origin,map,rand,destination=None):
		if destination==None:
			destination = rand.choice(map.nodelist)
		self.startnode = origin
		self.curnode = None # node we're traveling towards
		self.curroad = None # road we're on
		self.nextnode = None # node _after_ the curnode
		self.route = []
		self.routedirection = 1 # so route caching will work, if we want to go thru the route backwards
		self.destnode = destination
		self.timetonext = 1


	def notifyRoadChange(self,turnnode,newnode,oldroad,newroad,map):
		if newnode == self.destnode:
			newroad.deleteCar(self)
			return
		self.curnode = newnode
		self.curroad = newroad
		i = 0
		try:
			i = self.route.index(newnode)
		except ValueError:
			self.route = doRouteT(self,turnnode,newnode,self.destnode,map)
			i = self.route.index(newnode)
		if self.route[i+self.routedirection] == turnnode:
			self.routedirection *= -1
		self.nextnode = self.route[i+self.routedirection]
		#!!!! SHOULD BE CHANGED!!!
		self.timetonext = int(newroad.dist())
		
	
	def getNextNode(self,oldroad,turnnode,map):
		return self.nextnode
		
	
	def tick(self,road,node,map,rand):
		self.onTick(road,node,map,rand)
		self.timetonext -= 1
		return self.timetonext <= 0
			
	def emergency_reroute(self,road,turnnode,map):
		pass
	
	def onTick(self,road,node,map,rand):
		pass
	
	def cleanup(self):
		pass #i think that cars don't make double refs, they just need to be del'd
		#del self.route
		#del self.startnode
		#del self.destnode
	
baseCarType = Car

def doRoute(car,begin,end,map):
	pass
def doRouteT(car,node1,node2,end,map):
	a = doRoute(node1,node2,map).remove(node2)
	b = doRoute(node2,end,map)
	return a+b
	
	