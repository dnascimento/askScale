from bottle import route, run, template, get, post, error, request, response, redirect, static_file, default_app
from storage import *

import os
from bottle import TEMPLATE_PATH
TEMPLATE_PATH.append(os.path.join(os.environ['OPENSHIFT_HOMEDIR'], 
    'app-root/runtime/repo/wsgi/views/')) 

# #import bottle

# #Parts
# from votes import *
# from user import *

db = Storage()

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




################ ANSWERS ##########################

@post("/question/<title>/answer")
def postAnswer(title):
	author = ""
	answer = request.forms.get('answer')
	db.addAnswer(title,answer,author)
	redirect("/question/"+title) 

############ comments #########################
@post("/question/<title>/comment")
def postComment(title):
	author = ""
	ident = request.forms.get("ident")
	answer = request.forms.get('answer')
	comment = request.forms.get('comment')
	db.addComment(ident,title,answer,comment,author)
	redirect("/question/"+title) 


########### questions ########################
@get("/new-question")
def getNewQuestion():
	return  (template("newQuestion.tpl",tags=['nice','novo']))

@post("/new-question")
def postNewQuestion():
	title = request.forms.get('title')
	content = request.forms.get('content')
	tags = request.forms.getlist('tags')
	author = ""
	db.addNewQuestion(title,content,tags,author)
	redirect("/question/"+title)

@get("/question/<title>")
def getQuestion(title):
	questionData = db.getQuestion(title)
	return template('question.tpl',questionData=questionData)

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
@get("/question/<title>/<answer>/up")
def voteUp(title,answer):
	votes = db.voteUp(title, answer)
	redirect("/question/"+title)


@get("/question/<title>/<answer>/down")
def voteDown(title,answer):
	votes = db.voteDown(title, answer)
	redirect("/question/"+title)


# ############################################################

# #LOCAL
#run(host='localhost',port=8888,reloader=True)

# #applicationEngine
# #application.run(server='gae')



application=default_app()





