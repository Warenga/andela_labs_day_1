class Vehicle(object):
	name = "General"
	model = "GM"

	def __init__(self, *args):
		pass


class Car(Vehicle):

	def __init__(self, *args):
		super(Vehicle, self).__init__(self, *args)
		self.name = args[1]
		self.model = args[2]
		self.v_type = args[3]

		



		





		