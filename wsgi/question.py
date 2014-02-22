from answer import Answer

class Question:
	questionCounter = 0
	def __init__(self,title,text,tags,author):
		Question.questionCounter += 1
		self.questionID = str(Question.questionCounter)
		self.title = title
		self.tags = tags
		self.answers = []
		self.question = Answer(author, text,True)

	############### Answer #####################
	def getAnswer(self,answerID):
		if str(self.question.answerID) == str(answerID):
			return self.question

		for answer in self.answers:
			if str(answer.answerID) == str(answerID):
				return answer
		return None


	def addAnswer(self,author, text):
		ans = Answer(author, text,False)
		self.answers.append(ans)


	def deleteAnswer(self,answerID):
		for answer in self.answers:
			if answer.answerID == answerID:
				self.answers.remove(answer)
				return None
		#TODO Through exception - No answer

	def updateAnswer(self,answerID,text):
		self.getAnswer(answerID).update(text)


	def voteUp(self,answerID):
		self.getAnswer(answerID).voteUp()

	def voteDown(self,answerID):
		self.getAnswer(answerID).voteDown()

	def delete(self):
		for answer in self.answers:
			answer.delete()
		answers = []



	################ Comments ################
	def addComment(self,answerID,text,author):
		self.getAnswer(answerID).addComment(text,author)


	def deleteComment(self,answerID,commentID):
		self.getAnswer(answerID).deleteComment(commentID)


	def updateComment(self, answerID,commentID,text):
		self.getAnswer(answerID).updateComment(commentID,text)