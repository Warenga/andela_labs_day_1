
class Car(object):

	num_of_doors = 4
	num_of_wheels = 4
	

	def __init__(self, name='General', model='GM', v_type='saloon'):
		self.name = name
		self.model = model
		self.v_type = v_type
		self.speed = 0

		if self.name == 'Porshe' or self.name == 'Koenigsegg':
			self.num_of_doors = 2

		if self.v_type == 'trailer':
			self.num_of_wheels = 8

	def is_saloon(self):
		if self.v_type == 'saloon':
			return True
		else:
			return False

	def drive(self, speed):
		if self.v_type == 'trailer':
			speed_calc = str(speed) + str(speed)
			self.speed = int(speed_calc)
		else:
			if speed == 3:
				self.speed = 1000
		return self









		



		





		