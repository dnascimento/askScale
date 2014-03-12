from comment import Comment
import askExceptions
import hashlib

import pymongo
client = pymongo.MongoClient("localhost", 27017)
db = client.askInesc


class Answer:
	def __init__(self,author,text,questionTitle, isQuestion,votes = 0,commentsIds = [],answer_id = None):
		if answer_id is None:
			m = hashlib.md5()
			m.update(text+author+questionTitle)
			self._id = m.hexdigest()
		else:
			self._id = answer_id

		self.author = author
		self.text = text
		self.isQuestion = isQuestion
		self.votes = votes
		self.commentsIds = commentsIds

	@classmethod
	def build(self,author,text,title,isQuestion):
		return Answer(author, text, title, isQuestion).save()

	@classmethod
	def getFromId(self,answerId):
		answer = db.answers.find_one(answerId)
		if answer is not None:
			answer = Answer.fromDictionary(answer)
			answer.LoadComments()
		return answer

	@classmethod
	def fromDictionary(self,array):
		return Answer(array['author'], array['text'], None, array['isQuestion'],array['votes'],array['commentsIds'],array['_id'])

	def LoadComments(self):
		comments = []
		for commentID in self.commentsIds:
			comm = Comment.getFromId(commentID)
			if comm is not None:
				comments.append(comm)
		self.comments = comments
	########################################
	def addComment(self,comment,author):
		self.commentsIds.append(comment._id)
		self.save()

	def deleteComment(self,commentID):
		comment = self.getComment(commentID)
		self.comments.remove(comment)


	def updateComment(self,commentID,text):
		self.getComment(commentID).update(text)
		save()

	def update(self,text):
		self.text = text
		save()

	def voteUp(self):
		self.votes += 1
		save()

	def voteDown(self):
		self.votes -= 1
		save()

	def delete(self):
		for comment in self.comments:
			comment.delete()
		comments = []
		#TODO remove


	def getComment(self,commentID):
		for comment in self.comments:
			if comment._id == commentID:
				return comment
		raise askExceptions.NotExist('comment',"Unknown Comment:"+str(commentID))


	################ CASTS ###################
	def save(self):
		objectDict = self.__dict__
		objectDict['comments'] = None
		db.answers.save(objectDict)
		return self


