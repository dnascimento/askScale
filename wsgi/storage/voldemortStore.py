from voldemort import StoreClient
import json

class Storage():	
	def __init__(self):
		self.s = StoreClient('test',[('localhost',6666)])
		
	def put(self, key, value):
		value = json.dumps(value, separators=(',',':'))
		self.s.put(str(key),value,None,'3')
		 
	def get(self,key):
		val = self.s.get(str(key),'2')
		if not val:
			return None
		else:
			print val[0][0]
			#open the most recent
			val = val[0][0]
			return json.loads(val)


	def delete(self, key):
		self.s.delete(str(key))

