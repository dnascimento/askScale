from answer import Answer
import askExceptions

import pymongo
client = pymongo.MongoClient("localhost", 27017)
db = client.askInesc


class Question:
	def __init__(self,title,tags, questionAnswerId, answersIds = [], question_id = None):
		if question_id is None:
			self._id = title
		else:
			self._id = question_id
		self.title = title
		self.tags = tags
		self.questionAnswerId = questionAnswerId
		self.answersIds = answersIds


	@classmethod
	def build(self,title,text,tags,author):
		exists = db.questions.find_one(title)
		if exists is None:
			answer = Answer.build(author, text,title,True).save()
			quest = Question(title, tags, answer._id,).save()
			return quest
		else:
			raise askExceptions.NotExist('question',"Already exists with same title"+str(title))

	@classmethod
	def fromDictionary(self,array):
		return Question(array['title'], array['tags'], array['questionAnswerId'], array['answersIds'],array['_id'])


	@classmethod
	def getFromId(self,questionID):
		question = db.questions.find_one(questionID)
		if question is  None:
			raise askExceptions.NotExist('question',"Unknown Question:"+str(questionID))

		question = Question.fromDictionary(question)
		question.LoadAnswers()
		return question
		
	@classmethod
	def getList(self,maxQuestions):
		objects = []
		#TODO Limiting
		for obj in db.questions.find():
			objects.append(Question.fromDictionary(obj))
		return objects
	

	def LoadAnswers(self):
		self.question = Answer.getFromId(self.questionAnswerId)
		answers = []
		for answerId in self.answersIds:
			ans = Answer.getFromId(answerId)
			if ans is not None:
				answers.append(ans)
		self.answers = answers


	############### Answer #####################
	def addAnswer(self,author, text):
		answer = Answer.build(author,text,self.title,False)
		self.answersIds.append(answer._id)
		self.save()


	#delete the comment
	def delete(self):
		self.getAnswer(self.questionAnswerId).delete()
		print self.answersIds
		for answerID in self.answersIds:
			self.getAnswer(answerID).delete()
		db.questions.remove(self._id)

	def deleteAnswer(self,answerID):
		try:
			self.answersIds.remove(answerID)
			self.getAnswer(answerID).delete()
			self.save()
		except ValueError:	
			raise askExceptions.NotExist('answer',"Unknown Answer: "+str(answerID))

	#########################################################
	def updateAnswer(self,answerID,text):
		self.getAnswer(answerID).update(text)

	def voteUp(self,answerID):
		self.getAnswer(answerID).voteUp()

	def voteDown(self,answerID):
		self.getAnswer(answerID).voteDown()

	################ Comments ################
	def addComment(self,answerID,text,author):
		self.getAnswer(answerID).addComment(text,author)

	def deleteComment(self,answerID,commentID):
		self.getAnswer(answerID).deleteComment(commentID)

	def updateComment(self, answerID,commentID,text):
		self.getAnswer(answerID).updateComment(commentID,text)

	################ CASTS ###################
	def getAnswer(self, answerID):
		return Answer.getFromId(answerID)
		
	def save(self):
		objectDict = self.__dict__
		objectDict['answers'] = None
		objectDict['question'] = None
		db.questions.save(objectDict)
		return self
	