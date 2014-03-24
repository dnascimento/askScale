from voldemort import StoreClient
import json
import askService

class Storage():	
	def __init__(self):
		self.s = StoreClient('test',[('localhost',6666)])
		
	def put(self, key, value):
		rid = askService.reqId
		value = json.dumps(value, separators=(',',':'))
		self.s.put(str(key),value,None,rid)
		 
	def get(self,key):
		rid = askService.reqId
		val = self.s.get(str(key),rid)
		if not val:
			return None
		else:
			print val[0][0]
			#open the most recent
			val = val[0][0]
			return json.loads(val)


	def delete(self, key):
		rid = askService.reqId
		self.s.delete(str(key),None,rid)

