from bottle import route, run, template, get, error, request, response, redirect, static_file, default_app
#import bottle

#Parts
from storage import *
from votes import *
from user import *

db = Storage()

application = bottle.Bottle()

@application.get("/")
def index():
	request.headers.get('cookie')
	response.add_header('RID', '124')
	questionList = db.getQuestionList(20)
	return template("index.tpl",name="dario",questionList=questionList)


@application.error(404)
def error404(error):
    return 'Nothing here, sorry'


@application.route('/static/<filepath:path>')
def server_static(filepath):
	return static_file(filepath,root="./static")




################ ANSWERS ##########################

@application.post("/question/<title>/answer")
def postAnswer(title):
	author = ""
	answer = request.forms.get('answer')
	db.addAnswer(title,answer,author)
	redirect("/question/"+title) 

############ comments #########################
@application.post("/question/<title>/comment")
def postComment(title):
	author = ""
	ident = request.forms.get("ident")
	answer = request.forms.get('answer')
	comment = request.forms.get('comment')
	db.addComment(ident,title,answer,comment,author)
	redirect("/question/"+title) 


########### questions ########################
@application.get("/new-question")
def getNewQuestion():
	return  (template("newQuestion.tpl",tags=['nice','novo']))

@application.post("/new-question")
def postNewQuestion():
	title = request.forms.get('title')
	content = request.forms.get('content')
	tags = request.forms.getlist('tags')
	author = ""
	db.addNewQuestion(title,content,tags,author)
	redirect("/question/"+title)

@application.get("/question/<title>")
def getQuestion(title):
	questionData = db.getQuestion(title)
	return template('question.tpl',questionData=questionData)

################# USER ########################
@application.get("/login")
def login():
	if isLogin():
		redirect("/")
	else:
		return template('login')

@application.get("/user/<username>")
def viewUser(username):
	print "view"


################ VOTES ####################
@application.get("/question/<title>/<answer>/up")
def voteUp(title,answer):
	votes = db.voteUp(title, answer)
	redirect("/question/"+title)


@application.get("/question/<title>/<answer>/down")
def voteDown(title,answer):
	votes = db.voteDown(title, answer)
	redirect("/question/"+title)


############################################################

#LOCAL
#application.run(host='localhost',port=8888,reloader=True)

#applicationEngine
#application.run(server='gae')

#Openshift
# This must be added in order to do correct path lookups for the views
import os
from bottle import TEMPLATE_PATH
TEMPLATE_PATH.applicationend(os.path.join(os.environ['OPENSHIFT_HOMEDIR'], 
    'runtime/repo/wsgi/views/')) 

application=default_app()


