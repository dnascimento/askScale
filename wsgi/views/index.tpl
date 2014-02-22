%rebase('base.tpl',title='Welcome')
<a href="new-question">New Question</a>
<ul>
	%for question in questionList:
		<li class="questionSummary">
			<a href="/question/{{question.questionID}}/{{question.title}}"><h3>{{question.title}}</h3></a>
			<ul>
			%for tag in question.tags:
				<li class="tag">{{tag}}</li>
			%end
		</li>
	%end
</ul>

