import hashlib

class Comment:
	def __init__(self,text,author,answerID):
		m = hashlib.md5()
		m.update(text+author+answerID)
		self.commentID = m.hexdigest()
		self.text = text
		self.author = author
	def delete(self):
		pass

	def update(self,text):
		self.text = text
