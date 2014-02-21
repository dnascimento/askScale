import bottle
from bottle  import route, template, get, post, request, response, redirect
from storage import Storage

db = Storage()

class User:
	lastSeen = ""
	votesUp = ""
	votesDown = ""
