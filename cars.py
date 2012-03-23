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

	def __str__(self):
		print("car at %s with %d ticks to %s" % (self.curroad.getNode(self.curnode),self.timetonext,self.curnode))

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
		print("car tick")
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

routecache = {}

def clearroutecache():
	routecache = {}


# Better routing algo (using dist):
# .py import operator;sorted({"three":3, "five":5, "four":4, "one":1}.values())
def doRoute(car,begin,end,map):
	if (begin, end) in routecache:
		return routecache[(begin,end)]
	#key = node, val = nodefrom
	bestroute = {begin:begin}
	queue=[begin]
	
	while end not in bestroute:
		nod = queue.pop()
		for n in nod.connections.keys():
			if n not in bestroute:
				bestroute[n]=nod
				queue.append(n)
			if n == end:
				break
	del queue
	#start building route
	n = end
	a=[]
	while n != begin:
		a.append(bestroute[n])
		n=bestroute[n]
	return a[::-1]
			
	
def doRouteT(car,node1,node2,end,map):
	a = doRoute(node1,node2,map).remove(node2)
	b = doRoute(node2,end,map)
	return a+b
	
	