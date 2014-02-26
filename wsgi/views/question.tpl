<div class="questionWrapper" question-title="{{questionData.title}}">
	<h1>{{questionData.title}}</h1>
	<button class="questionDelete">Delete</button>
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
		<textarea name="text" cols="40" rows="5"></textarea>
		<input type="submit" value="Answer"/>
	</form>
</div>

%rebase('base',title=questionData.title)
