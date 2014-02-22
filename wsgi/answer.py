from comment import Comment

class Answer:
	answerCounter = 0
	def __init__(self,author,text,question):
		Answer.answerCounter += 1
		self.answerID = str(Answer.answerCounter)
		self.author = author
		self.votes = 0
		self.text = text
		self.comments = []
		self.isQuestion = question

	def getComment(self,commentID):
		for comment in self.comments:
			if comment.commentID == commentID:
				return comment
		return None

	def addComment(self,comment,author):
		comm = Comment(comment, author)
		self.comments.append(comm)

	def deleteComment(self,commentID):
		comment = self.getComment(commentID)
		if comment is not None:
			self.comments.remove(comment)
		else:
			pass
			#TODO: Throw exception

	def updateComment(self,commentID,text):
		self.getComment(commentID).update(text)


	def update(self,text):
		self.text = text

	def voteUp(self):
		self.votes += 1

	def voteDown(self):
		self.votes -= 1

	def delete(self):
		for comment in self.comments:
			comment.delete()
		comments = []

