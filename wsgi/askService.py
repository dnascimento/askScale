from models.question import Question
import models.askExceptions
import hashlib

#Singleton
class AskService:
	_instance = None
	def __new__(cls,*args,**kwargs):
		if not cls._instance:
			cls._instance = super(Singleton,cls).__new__(cls, *args, **kwargs)
		return cls._instance

	############### Question #####################
	def addNewQuestion(self,title,text,tags,author):
		return Question.build(title,text,tags,author)

	def getQuestion(self,questionId):
		return Question.getFromId(questionId)

	def deleteQuestion(self,questionTitle):
		self.getQuestion(questionTitle).delete()

	def getQuestionList(self,maxQuestions):
		return Question.getList(maxQuestions)
	
	############### Answer #####################
	def addAnswer(self,questionTitle,text,author):
		self.getQuestion(questionTitle).addAnswer(author, text)

	def updateAnswer(self,questionTitle,answerID,text):
		self.getQuestion(questionTitle).updateAnswer(answerID,text)

	def delAnswer(self,questionTitle,answerID):
		self.getQuestion(questionTitle).deleteAnswer(answerID)

	############# Comment ##################
	def addComment(self,questionTitle,answerID,text,author):
		self.getQuestion(questionTitle).addComment(answerID,text,author)

	def deleteComment(self,questionTitle,answerID,commentID):
		self.getQuestion(questionTitle).deleteComment(answerID,commentID)

	def updateComment(self,questionTitle,answerID,commentID,text):
		self.getQuestion(questionTitle).updateComment(answerID,commentID,text)

	############### Vote #####################
	def voteUp(self,questionTitle,answerID):
		self.getQuestion(questionTitle).voteUp(answerID)

	def voteDown(self,questionTitle,answerID):
		self.getQuestion(questionTitle).voteDown(answerID)



	

































