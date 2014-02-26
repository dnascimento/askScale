from comment import Comment
import askExceptions
import hashlib


class Answer:
	def __init__(self,author,text,questionTitle, question):
		m = hashlib.md5()
		m.update(text+author+questionTitle)
		self.answerID = m.hexdigest()
		self.author = author
		self.votes = 0
		self.text = text
		self.comments = []
		self.isQuestion = question

	def getComment(self,commentID):
		for comment in self.comments:
			if comment.commentID == commentID:
				return comment
		raise askExceptions.NotExist('comment',"Unknown Comment:"+str(commentID))

	def addComment(self,comment,author):
		comm = Comment(comment, author,self.answerID)
		self.comments.append(comm)

	def deleteComment(self,commentID):
		comment = self.getComment(commentID)
		self.comments.remove(comment)


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

