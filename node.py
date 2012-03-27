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
			print("making car")
			c = self.car(self,map,rand,rand.choice(map.nodelist))
			c.routeInit(self,map,rand)
			self.carArrived(c,None,map)
