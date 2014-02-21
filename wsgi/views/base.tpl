<!DOCTYPE HTML>
<html>
<head>
	<link rel="stylesheet" type="text/css" href="/static/ask.css"/>
	<script src="/static/ask.js"></script>
	<title>{{"AskINESC"+title or 'No title'}}</title>
</head>
<body>
	<div class="header">
		<a href="/">
			<img src="/static/logo.png"/>
			<h1>Ask</h1>
		</a>
		<div class="user">
			%if defined('name'):
				<h2>Welcome: {{name}}</h2>
			%else:
				<a href="/login"><h2>Login</h2></a>
			%end
		</div>
	</div>
	<div id="content">
		%include
	</div>
</body>
</html>

