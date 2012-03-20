

import world,cars

class CarGenNode (world.Node):
	def __init__(self,position,cartype = cars.baseCarType, delay=20):
		world.Node.__init__(self,position)
		self.delay = delay
		self.car = cartype
		self.tickcount = 0
		
	
	def onTick(self,map,rand):
		self.tickcount += 1
		if self.tickcount >= self.delay:
			c = self.car(self,map,rand.choice(map.nodelist))