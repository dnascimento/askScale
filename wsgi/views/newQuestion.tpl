<form action="/new-question" method="post">
			<label>Please enter your question</label>
			<input name="title" type="text"/>
			<br>
			<label>Add Details</label>
			<textarea name="text" cols="40" rows="10"></textarea>
			<br>
			<label>tags</label>
			<select name="tags" multiple>
				%for tag in tags:
					<option value="{{tag}}">{{tag}}</option>
				%end
			</select>
			<br>
			<input value="Submit" type="submit"/>
</form>

%rebase('base', title='New Question')
