<div class="answerArea" answer-id="{{answer._id}}">
	<div class="vote">
		<img class="up" src="/static/up.png"/>
		<p>{{answer.votes}}</p>
		<img class="down" src="/static/down.png"/>
	</div>
	<div class="answerContent">
		<div>
			<p>{{answer.text}}</p>
			%if answer.isQuestion:
				<button class="edit">Edit Question</button>
			%else:
				<button class="delete">Delete</button>
				<button class="edit">Edit</button>
			%end
			<div class="author">
				<a href="/user/{{answer.author}}"><h4>{{answer.author}}</h4></a>
			</div>
		</div>
		<div class="commentsArea">
			<h3>Comments</h3>
				%for comment in answer.comments:
					<div class="comment" comment-id="{{comment._id}}">
						<p>{{comment.text}}</p>
						<button class="delete">Delete</button>
						<button class="edit">Edit</button>
						<a href="/user/{{comment.author}}">{{comment.author}}</a>
					</div>
					<hr>
				%end
				<button class="newComment">Comment</button>
		</div>
	</div>
</div>