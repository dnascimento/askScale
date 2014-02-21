
class Comment:
	def __init__(self,comment,author):
		self.comment = comment
		self.author = author

class Answer:
	answerCounter = 0
	def __init__(self,author,content):
		Answer.answerCounter += 1
		self.ident = Answer.answerCounter
		self.author = author
		self.votes = 0
		self.content = content
		self.comments = []

	def addComment(self,comment,author):
		comm = Comment(comment, author)
		self.comments.append(comm)

	def voteUp(self):
		self.votes += 1

	def voteDown(self):
		self.votes -= 1


class Question:
	def __init__(self,title,content,tags,author):
		self.title = title
		self.tags = tags
		self.answers = []
		self.question = Answer(author, content)

	def addAnswer(self,author,content):
		ans = Answer(author, content)
		self.answers.append(ans)

	def getAnswer(self,ident):
		if str(self.question.ident) == str(ident):
			return self.question

		for answer in self.answers:
			if str(answer.ident) == str(ident):
				return answer
		return None

	def voteUp(self,answerID):
		self.getAnswer(answerID).voteUp()

	def voteDown(self,answerID):
		self.getAnswer(answerID).voteDown()

#Singleton
class Storage:
	questions = []

	_instance = None
	def __new__(cls,*args,**kwargs):
		if not cls._instance:
			cls._instance = super(Singleton,cls).__new__(cls, *args, **kwargs)
		return cls._instance

	def addNewQuestion(self,title,content,tags,author):
		quest = Question(title, content, tags,author)
		Storage.questions.append(quest)
		return quest


	def getQuestion(self,title):
		for question in Storage.questions:
			if question.title == title:
				return question
		return None


	def addAnswer(self,title,answer,author):
		quest = self.getQuestion(title)
		quest.addAnswer(author, answer)



	def voteUp(self,title,answer):
		quest = self.getQuestion(title)
		quest.voteUp(answer)



	#######################################
	def voteDown(self,title,answer):
		quest = self.getQuestion(title)
		quest.voteDown(answer)

	def addComment(self,ident,title,answer,comment,author):
		quest = self.getQuestion(title)
		ans = quest.getAnswer(ident)
		ans.addComment(comment,author)


	##########################################
	def getQuestionList(self,maxQuestions):
		return Storage.questions