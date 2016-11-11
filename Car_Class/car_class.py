
class Car(object):

	num_of_wheels = 4
	speed = 0

	def __init__(self, name='General', model='GM', v_type=''):
		self.name = name
		self.model = model
		self.v_type = v_type

	@property
	def num_of_doors(self):
	    if self.name == 'Porsche' or self.name == 'Koenigsegg':
			self.num_of_doors = 2
			return self.num_of_door
		else: 
			return self.num_of_doors = 4

	def is_saloon(self):
		self.v_type = 'Saloon'

	def drive(self, drive):
		if self.v_type == 'trailer':
			if drive == 7:
				self.speed = 77
		else:
			if drive == 3:
				self.speed = 1000






		



		





		