
class Comment:
	commentCounter = 0
	def __init__(self,text,author):
		Comment.commentCounter += 1
		self.commentID = str(Comment.commentCounter)
		self.text = text
		self.author = author
	def delete(self):
		pass

	def update(self,text):
		self.text = text
