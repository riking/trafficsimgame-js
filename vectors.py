
import numbers,copy,math;

class Vector:
	__doc__ = """Syntax: Vector(values)\
values is an iterable that can be cast to list\n\
The vector class is an ordered set of values.\n\

Two vectors can be added and subtracted.\n\
The distance that the vector spans is Vector.magnitude().\n\
"""
	def __init__(self,vallist):
		self.values = list(vallist)
		self.dimensions = len(vallist)


	def __add__(self,other):
		if not isinstance(other,Vector):
			if not other: #is zero
				return self
			return NotImplemented
			#raise TypeError("Can only add 2 vectors")
		if self.dimensions != other.dimensions:
			#return NotImplemented
			raise TypeError("Dimension mismatch")
		a=[]
		for i in range(self.dimensions):
			a.append(self.values[i]+other.values[i])
		return Vector(a)

		
	def __radd__(self,other):
		if not isinstance(other,Vector):
			if isinstance(other,type(None)):
				return self
			return NotImplemented
			#raise TypeError("Can only add 2 vectors")
		return NotImplemented #let the __add__ handle it
		
		
	def __sub__(self,other):
		if not isinstance(other,Vector):
			return NotImplemented
			#raise TypeError("Can only add 2 vectors")
		if self.dimensions != other.dimensions:
			#return NotImplemented
			raise TypeError("Dimension mismatch")
		a=[]
		for i in range(self.dimensions):
			a.append(self.values[i]-other.values[i])
		return Vector(a)


	def __mul__(self,other):
		if isinstance(other,Vector):
			return self.dot(other) #dot product
		else: #scalar multiplacation
			a = []
			for v in self.values:
				a.append(v * other)
			return Vector(a)


	def __rmul__(self,other):
		if isinstance(other,Vector):
			return NotImplemented #just in case..
		else: #scalar multiplacation
			a = []
			for v in self.values:
				a.append(v * other)
			return Vector(a)
			

	def __pow__(self,other):
		if isinstance(other,Vector):
			return self.cross(other) #cross product
		return NotImplemented
		

	def __div__(self,other):
		self.__truediv__(other)


	def __truediv__(self,other):
		if isinstance(other,numbers.Number):
			a=[]
			for v in self.values:
				a.append(v/other)
			return Vector(a) #ensure python 3-ability
		elif isinstance(other,Vector):
			return self.dot(other) #dot product. meh.
		else:
			return NotImplemented


	def __floordiv__(self,other):
		if isinstance(other,numbers.Number):
			a=[]
			for v in self.values:
				a.append(int(v//other))
			return Vector(a)
		elif isinstance(other,Vector):
			return NotImplemented#not sure yet
		else:
			return NotImplemented


	def __iadd__(self,other):
		if not isinstance(other,Vector):
			if isinstance(other,None):
				return self
			return NotImplemented
			#raise TypeError("Can only add 2 vectors")
		if self.dimensions != other.dimensions:
			raise TypeError("Dimension mismatch")
		for i in range(self.dimensions):
			self.values[i] += other.values[i]


	def __isub__(self,other):
		if not isinstance(other,Vector):
			raise TypeError("Can only add 2 vectors")
		if self.dimensions != other.dimensions:
			raise TypeError("Dimension mismatch")
		for i in range(self.dimensions):
			self.values[i] += other.values[i]

	
	def __imul__(self,other):
		if isinstance(other,Vector):
			return NotImplemented
		else:
			for v in self.values:
				v *= other


	def __neg__(self):
		a=[]
		for i in self.values:
			a.append(-i)
		return Vector(a)


	def __pos__(self):
		a=[]
		for i in self.values:
			a.append(+i)
		return Vector(a)


	def __abs__(self):
		return self.magnitude()

	def __int__(self):
		return int(self.magnitude())

	def _intvals(self):
		a=[]
		for v in self.values:
			a.append(int(v))
		return Vector(a)
		
	def __float__(self):
		return float(self.magnitude())
		
	def __repr__(self):
		return "Vector(%s)" % repr(tuple(self.values))
		
	def __str__(self):
		return "<%s>" % (", ".join([str(v) for v in self.values]))
		
	def __cmp__(self,other):
		return self.magnitude() - other.magnitude()
		
	def __eq__(self,other):
		return self.values == other.values
		
	def __hash__(self):
		i=1
		for v in self.values:
			i += v.__hash__()
			i ** 2
		return i
	def __nonzero__(self):
		for v in self.values:
			if v != 0:
				return True
	
	def __len__(self):
		return self.dimensions
	
	def __iter__(self):
		return self.values.__iter__
	
	def __copy__(self): #shallow copy REQUIRED
		a = Vector(self.values)
		a.values = self.values
		
	def __getitem__(self,index):
		return self.values[index]
		
	def dot(self,other):
		if not isinstance(other,Vector):
			raise TypeError("cannot dot product with a non-integer")
		if self.dimensions != other.dimensions:
			raise TypeError("dimension mismatch")
		total = 0
		for i in range(self.dimensions):
			total += self.values[i] * other.values[i]
		return total


	def cross(self,other):
		if self.dimensions != 3:
			raise TypeError("cross product is not defined for non-3D vectors. use multicross((vec2,vec3,vec4)) (note the tuple)")
		return det([unitarray(3),self.values,other.values])


	#has a __doc__
	def multicross(self,others):
		if self.dimensions != len(others)+2:
			raise TypeError("number of additional operands must equal dimensions minus 2. read Vector.multicross.__doc__")
		else:
			a=[unitarray(self.dimensions),self.values]
			for v in others: #typecheck
				if not isinstance(v,Vector):
					raise TypeError("Second argument should be tuple of vectors.")
				a.append(v.values)
			return det(a)
			

	def scalartripleproduct(self,two,thr):
		return self.dot(two*thr)
		
	def magnitude(self):
		return math.sqrt(sum([i**2 for i in self.values]))
		
	def getcos(self,other):
		return self.dot(b)/(a.magnitude()*b.magnitude())
		
	def getAngle(self,other):
		return math.acos((self*other)/(abs(a)*abs(b)))
		#                    dot            numb
		
	def isParallel(self,other):
		return (self**other) == 0
		
	def isOrthrogonal(self,other):
		return self.dot(other) == 0
	
	def isCoplanar(self,two,three):
		return self.scalartripleproduct(two,three)==0
		
	def proj(self,other): # Vector projection of b onto a
		return self*((self * other)/abs(self)**2)
		#        scalr    dot
		
	def comp(self,other): # Scalar projection of b onto a
		return (self*other)/abs(self)
		#          dot
		

	def fromPoints(points1,points2):
		if isinstance(points1,Vector) and isinstance(points2,Vector):
			return points1 - points2


#



class UnitVector (Vector):
	def __init__(self,size,axis,sign=1):
		if axis > size:
			raise TypeError("axis index cannot be greater than the vector size")
		a=[]
		for i in range(size):
			a.append(0)
		a[axis]=sign
		Vector.__init__(self,a)


def unitarray(size):
	a=[]
	for i in range(size):
		a.append(UnitVector(size,i))
	return a


class ZeroVector(Vector):
	def __init__(self,size):
		a=[]
		for i in range(size):
			a.append(0)
		Vector.__init__(self,a)


# Determinant of a matrix, compatible with vectors
def det(matrix):
	if len(matrix)==2:
		return det2(matrix)
	if len(matrix) != len(matrix[0]):
		raise TypeError("non-square matrix")
	total = 0
	negfact = 1
	for j in range(len(matrix)):
		mc = copy.deepcopy(matrix)
		for i in range(len(matrix)):
			del mc[i][j]
		del mc[0]
		total = matrix[0][j]*negfact*det(mc) + total
		negfact *= -1
	return total


def det2(mat):
	if len(mat) != 2:
		raise TypeError("det2 needs a size-2 matrix")
	if len(mat[0]) != 2 or len(mat[1]) != 2:
		raise TypeError("not a 2x2 matrix")
	return mat[0][0]*mat[1][1] - mat[0][1]*mat[1][0]
	
