

import world

class Car:
	def __init__(self,origin,map,destination=None):
		pass
	
	def notifyRoadChange(self,turnnode,newnode,oldroad,newroad,map):
		pass
	
	def getNextNode(self,oldroad,turnnode,map):
		pass
	
	def tick(self,road,node,map,rand):
		pass
	
	def onTick(self,road,node,map,rand):
		pass
	
baseCarType = Car