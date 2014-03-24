import pymongo



class MongoStorage():	
	def __init__(self):
		client = pymongo.MongoClient("localhost", 27017)
		self.db = client.askInesc

	def put(self, key, value):
		self.db.ask.save(value)
		 
	def get(self,key):
		return self.db.ask.find_one(key)

	def delete(self, key):
		self.db.ask.remove(key)