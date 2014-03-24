#from mongoStore import Storage
from voldemortStore import Storage


class StorageService():	
	def __init__(self):
		self.s = Storage()

	def put(self, key, value):
		return self.s.put(key,value)

	def get(self,key):
		return self.s.get(key)

	def delete(self, key):
		return self.s.delete(key)