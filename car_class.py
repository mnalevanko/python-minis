class Car():
	'''Testujem fungovanie tried.'''

	def __init__(self, name):
		self.name = name

	def brand(self):
		print('Toto auto ma znacku', self.name + ".")

silvia = Car('Suzuki')
michal = Car('Škoda Felicia')
michal.brand()