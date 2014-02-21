<div class="questionWrapper">
	<h1>{{questionData.title}}</h1>
	<ul>
		%for tag in questionData.tags:
			<li class="tag">{{tag}}</li>
		%end
	</ul>
	<hr>
	%include answer answer=questionData.question, title=questionData.title
	<h3>Answers</h3>
	<hr>
	%for answer in questionData.answers:
		%include answer answer=answer , title=questionData.title
	%end
	<form action="{{questionData.title}}/answer" method="post">
		<textarea name="answer" cols="40" rows="5"></textarea>
		<input type="submit" value="Answer"/>
	</form>
</div>

%rebase('base',title=questionData.title)
