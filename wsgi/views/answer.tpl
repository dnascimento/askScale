<!-- 
answer = {id,content,author, votes, comments[]}
comment = {comment,author}

-->

<div class="answerArea">
	<div class="vote">
		<a href="{{title}}/{{answer.ident}}/up"><img src="/static/up.png"/></a>
		<p>{{answer.votes}}</p>
		<a href="{{title}}/{{answer.ident}}/down"><img src="/static/down.png"/></a>
	</div>
	<div class="answerContent">
		<div>
			<div>
				<p>{{answer.content}}</p>
			</div>
			<div class="author">
				<a href="/user/{{answer.author}}"><h4>{{answer.author}}</h4></a>
			</div>
		</div>
		<div class="commentsArea">
			<h3>Comments</h3>
				%for comment in answer.comments:
					<div class="comment">
						<p>{{comment.comment}}</p>
						<a href="/user/{{comment.author}}">{{comment.author}}</a>
					</div>
					<hr>
				%end
				<form action="{{title}}/comment" method="post">
					<input name="ident"type="hidden" value="{{answer.ident}}"/>
					<textarea name="comment" cols="40" rows="5"></textarea>
					<input type="submit" value="Comment"/>
				</form>
		</div>
	</div>
</div>