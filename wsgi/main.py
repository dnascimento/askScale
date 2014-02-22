from bottle import route, run, template, get, post, error, request, put, response, delete, redirect, static_file, default_app
from storage import *


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
	db.deleteQuestion(questionID)
	redirect("/")

@get("/question/<questionID>/<questionTitle>")
def getQuestion(questionTitle,questionID):
	questionData = db.getQuestion(questionID)
	return template('question.tpl',questionData=questionData)




################ ANSWERS ##########################

@post("/question/<questionID>/<questionTitle>/answer")
def postAnswer(questionTitle,questionID):
	author = ""
	text = request.forms.get('text')
	db.addAnswer(questionID,text,author)
	redirect("/question/"+questionID+"/"+questionTitle) 


@put("/question/<questionID>/<questionTitle>/answer")
def updateAnswer(questionTitle,questionID):
	answerId = request.forms.get('answerID')
	text = request.forms.get('text')
	print "update"+str(text)
	db.updateAnswer(questionID,answerId,text)
	redirect("/question/"+questionID+"/"+questionTitle) 


@delete("/question/<questionID>/<questionTitle>/answer")
def deleteAnswer(questionTitle,questionID):
	answerID = request.forms.get('answerID')
	db.delAnswer(questionID,answerID)
	redirect("/question/"+questionID+"/"+questionTitle) 


############ comments #########################
@post("/question/<questionID>/<questionTitle>/comment")
def postComment(questionTitle,questionID):
	author = ""
	answerID = request.forms.get('answerID')
	text = request.forms.get('text')
	db.addComment(questionID,answerID,text,author)
	redirect("/question/"+questionID+"/"+questionTitle) 

@put("/question/<questionID>/<questionTitle>/comment")
def updateComment(questionTitle,questionID):
	answerID = request.forms.get('answerID')
	commentID = request.forms.get("commentID")
	text = request.forms.get('text')
	db.updateComment(questionID,answerID,commentID,text)
	redirect("/question/"+questionID+"/"+questionTitle) 

@delete("/question/<questionID>/<questionTitle>/comment")
def deleteComment(questionTitle,questionID):
	commentID = request.forms.get("commentID")
	answerID = request.forms.get('answerID')
	db.deleteComment(questionID,answerID,commentID)
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
	votes = db.voteUp(questionID, answerID)
	redirect("/question/"+questionID+"/"+questionTitle) 


@post("/question/<questionID>/<questionTitle>/down")
def voteDown(questionTitle,questionID):
	answerID = request.forms.get("answerID")
	votes = db.voteDown(questionID, answerID)
	redirect("/question/"+questionID+"/"+questionTitle) 


# ############################################################

# #LOCAL
run(host='localhost',port=8888,reloader=True)

# #applicationEngine
# #application.run(server='gae')


#openshift
application=default_app()





