from bottle import route, run, template, get, post, error, request, put, response, delete, redirect, static_file, default_app
from storage import *
import askExceptions


#OPENSHIFT
# import os
# from bottle import TEMPLATE_PATH
# TEMPLATE_PATH.append(os.path.join(os.environ['OPENSHIFT_HOMEDIR'], 
#     'app-root/runtime/repo/wsgi/views/')) 



db = Storage()
#GAE - Force bootle
#import bottle
# application = bottle.Bottle()

@get("/")
def index():
	request.headers.get('cookie')
	response.add_header('RID', '124')
	questionList = db.getQuestionList(20)
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
	author = ""
	questionTitle = request.forms.get('title')
	text = request.forms.get('text')
	tags = request.forms.getlist('tags')
	question = db.addNewQuestion(questionTitle,text,tags,author)
	print question.title
	redirect("/question/"+question.questionID+"/"+question.title)


@delete("/question/<questionID>/<questionTitle>")
def deleteQuestion(questionTitle,questionID):
	try:
		db.deleteQuestion(questionID)
	except askExceptions.NotExist as e:
		return error(e)
	redirect("/")

@get("/question/<questionID>/<questionTitle>")
def getQuestion(questionTitle,questionID):
	try:
		questionData = db.getQuestion(questionID)
	except askExceptions.NotExist as e:
		return error(e)

	return template('question.tpl',questionData=questionData)




################ ANSWERS ##########################

@post("/question/<questionID>/<questionTitle>/answer")
def postAnswer(questionTitle,questionID):
	author = ""
	text = request.forms.get('text')
	try:
		db.addAnswer(questionID,text,author)
	except askExceptions.NotExist as e:
		return error(e)
	redirect("/question/"+questionID+"/"+questionTitle) 


@put("/question/<questionID>/<questionTitle>/answer")
def updateAnswer(questionTitle,questionID):
	answerId = request.forms.get('answerID')
	text = request.forms.get('text')
	print "update"+str(text)
	try:
		db.updateAnswer(questionID,answerId,text)
	except askExceptions.NotExist as e:
		return error(e)
	redirect("/question/"+questionID+"/"+questionTitle) 


@delete("/question/<questionID>/<questionTitle>/answer")
def deleteAnswer(questionTitle,questionID):
	answerID = request.forms.get('answerID')
	try:
		db.delAnswer(questionID,answerID)
	except askExceptions.NotExist as e:
		return error(e)
	redirect("/question/"+questionID+"/"+questionTitle) 


############ comments #########################
@post("/question/<questionID>/<questionTitle>/comment")
def postComment(questionTitle,questionID):
	author = ""
	answerID = request.forms.get('answerID')
	text = request.forms.get('text')
	try:
		db.addComment(questionID,answerID,text,author)
	except askExceptions.NotExist as e:
		return error(e)
	redirect("/question/"+questionID+"/"+questionTitle) 

@put("/question/<questionID>/<questionTitle>/comment")
def updateComment(questionTitle,questionID):
	answerID = request.forms.get('answerID')
	commentID = request.forms.get("commentID")
	text = request.forms.get('text')
	try:
		db.updateComment(questionID,answerID,commentID,text)
	except askExceptions.NotExist as e:
		return error(e)
	redirect("/question/"+questionID+"/"+questionTitle) 

@delete("/question/<questionID>/<questionTitle>/comment")
def deleteComment(questionTitle,questionID):
	commentID = request.forms.get("commentID")
	answerID = request.forms.get('answerID')
	try:
		db.deleteComment(questionID,answerID,commentID)
	except askExceptions.NotExist as e:
		return error(e)
	redirect("/question/"+questionID+"/"+questionTitle) 




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
@post("/question/<questionID>/<questionTitle>/up")
def voteUp(questionTitle,questionID):
	answerID = request.forms.get("answerID")
	try:
		votes = db.voteUp(questionID, answerID)
	except askExceptions.NotExist as e:
		return error(e)
	redirect("/question/"+questionID+"/"+questionTitle) 


@post("/question/<questionID>/<questionTitle>/down")
def voteDown(questionTitle,questionID):
	answerID = request.forms.get("answerID")
	try:
		votes = db.voteDown(questionID, answerID)
	except askExceptions.NotExist as e:
		return error(e)
	redirect("/question/"+questionID+"/"+questionTitle) 


# ############################################################

# #LOCAL
run(host='localhost',port=8888,reloader=True)

# #applicationEngine
# #application.run(server='gae')


#openshift
application=default_app()





