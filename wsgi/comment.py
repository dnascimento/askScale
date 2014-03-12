import hashlib

import pymongo
client = pymongo.MongoClient("localhost", 27017)
db = client.askInesc

class Comment:
	def __init__(self,text,author,answerID,comment_id = None):
		if comment_id is None:
			m = hashlib.md5()
			m.update(text+author+answerID)
			self._id = m.hexdigest()
		else:
			self._id = comment_id
		self.text = text
		self.author = author


	@classmethod
	def build(self,text,author,answerID):
		return Comment(text, author, answerID).save()

	@classmethod
	def getFromId(self,commentId):
		comment = db.comments.find_one(commentId)
		if comment is not None:
			comment = Comment.fromDictionary(comment)
		return comment

	@classmethod
	def fromDictionary(self,array):
		return Comment(array['text'], array['author'], None, array['_id'])

	######################################################################################

	def delete(self):
		#TODO
		pass

	def update(self,text):
		#TODO
		self.text = text

	def save(self):
		objectDict = self.__dict__
		db.comments.save(objectDict)		
		return self
