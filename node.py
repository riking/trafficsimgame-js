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
