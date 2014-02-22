from question import Question
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
		quest = Question(questionTitle, text, tags,author)
		Storage.questions.append(quest)
		return quest


	def getQuestion(self,questionID):
		for question in Storage.questions:
			if question.questionID == questionID:
				return question
		return None

	def deleteQuestion(self,questionID):
		quest = self.getQuestion(questionID)
		quest.delete()
		Storage.questions.remove(quest)

		
	############### Answer #####################
	def addAnswer(self,questionID,text,author):
		self.getQuestion(questionID).addAnswer(author, text)

	def delAnswer(self,questionID,answerID):
		self.getQuestion(questionID).deleteAnswer(answerID)

	def updateAnswer(self,questionID,answerID,text):
		self.getQuestion(questionID).updateAnswer(answerID,text)



	############### Vote #####################
	def voteUp(self,questionID,answerID):
		self.getQuestion(questionID).voteUp(answerID)

	def voteDown(self,questionID,answerID):
		self.getQuestion(questionID).voteDown(answerID)


	############### Comment #####################
	def addComment(self,questionID,answerID,text,author):
		self.getQuestion(questionID).addComment(answerID,text,author)

	def deleteComment(self,questionID,answerID,commentID):
		self.getQuestion(questionID).deleteComment(answerID,commentID)

	def updateComment(self,questionID,answerID,commentID,text):
		self.getQuestion(questionID).updateComment(answerID,commentID,text)

	############### List #####################
	def getQuestionList(self,maxQuestions):
		return Storage.questions