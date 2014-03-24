from bottle import route, run, template, get, post, error, request, put, response, delete, redirect, static_file, default_app
from askService import *
from models import askExceptions
import hashlib
import pprint

#OPENSHIFT
# import os
# from bottle import TEMPLATE_PATH
# TEMPLATE_PATH.append(os.path.join(os.environ['OPENSHIFT_HOMEDIR'], 
#     'app-root/runtime/repo/wsgi/views/')) 


pp = pprint.PrettyPrinter(indent=4)

service = AskService()
#GAE - Force bootle
#import bottle
# application = bottle.Bottle()

@get("/test")
def test():
	return "dario"

@get("/")
def index():
	reqID = request.headers.get('Id')
	print "req: "+str(reqID)
	response.add_header('RID', reqID)
	questionList = service.getQuestionList(20)
	print questionList
	return template("index.tpl",name="dario",questionList=questionList)


@error(404)
def error404(error):
    return 'Nothing here, sorry'

def error(e):
	return template("error.tpl",error=e.error)


@route('/static/<filepath:path>')
def server_static(filepath):
	return static_file(filepath,root="./static")

########### questions ########################
@get("/new-question")
def getNewQuestion():
	return  (template("newQuestion.tpl",tags=['nice','novo']))

@post("/new-question")
def postNewQuestion():
	print "body"+str(request.body)
	print "length:"+str(request.content_length)


	author = ""
	questionTitle = request.forms.get('title')
	text = request.forms.get('text')
	tags = request.forms.getlist('tags')
	print "questionTitle"+str(questionTitle)
	try:
		question = service.addNewQuestion(questionTitle,text,tags,author)
		redirect("/question/"+question.title)
	except askExceptions.NotExist as e:
		return error(e)

@delete("/question/<questionTitle>")
def deleteQuestion(questionTitle):
	try:
		service.deleteQuestion(questionTitle)
	except askExceptions.NotExist as e:
		return error(e)
	redirect("/")

@get("/question/<questionTitle>")
def getQuestion(questionTitle):
	try:
		questionData = service.getQuestion(questionTitle)
	except askExceptions.NotExist as e:
		return error(e)

	return template('question.tpl',questionData=questionData)




################ ANSWERS ##########################

@post("/question/<questionTitle>/answer")
def postAnswer(questionTitle):
	author = ""
	text = request.forms.get('text')
	try:
		service.addAnswer(questionTitle,text,author)
	except askExceptions.NotExist as e:
		return error(e)
	redirect("/question/"+questionTitle) 


@put("/question/<questionTitle>/answer")
def updateAnswer(questionTitle):
	answerId = request.forms.get('answerID')
	text = request.forms.get('text')
	print "update"+str(text)
	try:
		service.updateAnswer(questionTitle,answerId,text)
	except askExceptions.NotExist as e:
		return error(e)
	redirect("/question/"+questionTitle) 


@delete("/question/<questionTitle>/answer")
def deleteAnswer(questionTitle):
	answerID = request.forms.get('answerID')
	try:
		service.delAnswer(questionTitle,answerID)
	except askExceptions.NotExist as e:
		return error(e)
	redirect("/question/"+questionTitle) 


############ comments #########################
@post("/question/<questionTitle>/comment")
def postComment(questionTitle):
	author = ""
	answerID = request.forms.get('answerID')
	text = request.forms.get('text')
	try:
		service.addComment(questionTitle,answerID,text,author)
	except askExceptions.NotExist as e:
		return error(e)
	redirect("/question/"+questionTitle) 

@put("/question/<questionTitle>/comment")
def updateComment(questionTitle):
	answerID = request.forms.get('answerID')
	commentID = request.forms.get("commentID")
	text = request.forms.get('text')
	try:
		service.updateComment(questionTitle,answerID,commentID,text)
	except askExceptions.NotExist as e:
		return error(e)
	redirect("/question/"+questionTitle) 

@delete("/question/<questionTitle>/comment")
def deleteComment(questionTitle):
	commentID = request.forms.get("commentID")
	answerID = request.forms.get('answerID')
	try:
		service.deleteComment(questionTitle,answerID,commentID)
	except askExceptions.NotExist as e:
		return error(e)
	redirect("/question/"+questionTitle) 




################# USER ########################
@get("/login")
def login():
	if isLogin():
		redirect("/")
	else:
		return template('login')

@get("/user/<username>")
def viewUser(username):
	print "view"


################ VOTES ####################
@post("/question/<questionTitle>/up")
def voteUp(questionTitle):
	answerID = request.forms.get("answerID")
	try:
		votes = service.voteUp(questionTitle, answerID)
	except askExceptions.NotExist as e:
		return error(e)
	redirect("/question/"+questionTitle) 


@post("/question/<questionTitle>/down")
def voteDown(questionTitle):
	answerID = request.forms.get("answerID")
	try:
		votes = service.voteDown(questionTitle, answerID)
	except askExceptions.NotExist as e:
		return error(e)
	redirect("/question/"+questionTitle) 


# ############################################################

# #LOCAL
run(host='localhost',port=8080,reloader=True)

# #applicationEngine
# #application.run(server='gae')


#openshift
application=default_app()





