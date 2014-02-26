from question import Question
import askExceptions
import hashlib

#Singleton
class Storage:
	questions = []

	_instance = None
	def __new__(cls,*args,**kwargs):
		if not cls._instance:
			cls._instance = super(Singleton,cls).__new__(cls, *args, **kwargs)
		return cls._instance



	############### Question #####################
	def addNewQuestion(self,questionTitle,text,tags,author):
		exists = self.getQuestionNone(questionTitle)
		if exists is None:
			quest = Question(questionTitle, text, tags,author)
			Storage.questions.append(quest)
			return quest
		else:
			raise askExceptions.NotExist('question',"Already exists with same title"+str(questionTitle))

	def getQuestion(self,questionTitle):
		question = self.getQuestionNone(questionTitle)
		if question is None:
			raise askExceptions.NotExist('question',"Unknown Question:"+str(questionTitle))
		else:
			return question

	def getQuestionNone(self,questionTitle):
		for question in Storage.questions:
			if question.title == questionTitle:
				return question
		return None

	def deleteQuestion(self,questionTitle):
		quest = self.getQuestion(questionTitle)
		quest.delete()
		Storage.questions.remove(quest)

		
	############### Answer #####################
	def addAnswer(self,questionTitle,text,author):
		self.getQuestion(questionTitle).addAnswer(author, text)

	def delAnswer(self,questionTitle,answerID):
		self.getQuestion(questionTitle).deleteAnswer(answerID)

	def updateAnswer(self,questionTitle,answerID,text):
		self.getQuestion(questionTitle).updateAnswer(answerID,text)



	############### Vote #####################
	def voteUp(self,questionTitle,answerID):
		self.getQuestion(questionTitle).voteUp(answerID)

	def voteDown(self,questionTitle,answerID):
		self.getQuestion(questionTitle).voteDown(answerID)


	############### Comment #####################
	def addComment(self,questionTitle,answerID,text,author):
		self.getQuestion(questionTitle).addComment(answerID,text,author)

	def deleteComment(self,questionTitle,answerID,commentID):
		self.getQuestion(questionTitle).deleteComment(answerID,commentID)

	def updateComment(self,questionTitle,answerID,commentID,text):
		self.getQuestion(questionTitle).updateComment(answerID,commentID,text)

	############### List #####################
	def getQuestionList(self,maxQuestions):
		return Storage.questions