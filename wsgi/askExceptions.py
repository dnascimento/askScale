class NotExist(Exception):
	def __init__(self, element,error):
		self.element = element
		self.error = error

	def __str__(self):
		print self.error