$(document).ready(function(){
	$(".questionDelete").click(function(){		
		questionTitle = getQuestionTitle();
		$.ajax({
			//delete: /question/<questionID>/<questionTitle>
			url: questionTitle,
			type: 'DELETE',
			error: function(jqXHR, textStatus, errorThrown){
				alert(errorThrown);
			},
			success: function(data, textStatus, jqXHR ){
				window.location.href = "/";
			}
		});
	});


	$(".delete").click(function(){
		answerID = getAnswerID(this);
		comm = $(this).parents(".comment")
		if(comm.length){
			commentID = $(comm).attr("comment-id");
			url = "/comment"
			data = {"answerID":answerID,commentID:commentID};
		}else{
			url = "/answer";
			data = {"answerID":answerID};
		}
		send(url,data,'DELETE');
	});

	$(".up").click(function(){
		answerID = getAnswerID(this);
		send("/up",{"answerID":answerID},"post");
	});

	$(".down").click(function(){
		answerID = getAnswerID(this);
		send("/down",{"answerID":answerID},"post");
	});

	$(".edit").click(function(){
		//get the text closer
		paragraph = $(this).siblings("p");
		text = paragraph.text();
		//open a textarea with that thext
		paragraph.replaceWith("<textarea>"+text+"</textarea>");
		$(this).removeClass().addClass("save");
		$(this).text("Save");
		$(".save").click(function(){updateAnswerOrComment(this)});
	});

	$(".newComment").click(function(){
		$("<textarea></textarea>").insertBefore(this);
		$(this).removeClass().addClass("saveComment");
		$(".saveComment").click(function(){saveNewComment(this)});
	});
});



function getQuestionID(){
	return $(".questionWrapper").attr("question-id");
}


function getQuestionTitle(){
	return $(".questionWrapper").attr("question-title");
}

function getAnswerID(ans){
	return $(ans).parents(".answerArea").attr("answer-id");
}



function updateAnswerOrComment(elem){
	answerID = getAnswerID(elem);
	text = $(elem).siblings("textarea").val();
	questionTitle = getQuestionTitle();

	comm = $(elem).parents(".comment")
	if(comm.length){
		//comment
		commentID = $(comm).attr("comment-id");
		//get comment ID
		url = "/comment"
		data = {"answerID":answerID,commentID:commentID, "text":text};
	}else{
		//answer
		url = "/answer";
		data = {"answerID":answerID,"text":text};
	}
	send(url,data,'PUT');
}



function saveNewComment(elem){
	answerID = getAnswerID(elem);
	text = $(elem).siblings("textarea").val();
	questionTitle = getQuestionTitle();
	// "/question/<questionID>/<questionTitle>/comment"
	send("/comment",{"answerID":answerID,"text":text},'POST');
}


function send(url,data,type){
	questionTitle = getQuestionTitle();
	$.ajax({
		url: "./"+questionTitle+url,
		data: data,
		type: type,
		error: function(jqXHR, textStatus, errorThrown){
			alert(errorThrown);
		},
		success: function(data, textStatus, jqXHR ){
			window.location.href = "./"+questionTitle;
		}
	});
}



//up and down classes

/*

				<form action="{{title}}/comment" method="post">
					<input name="answerID"type="hidden" value="{{answer.answerID}}"/>
					<textarea name="text" cols="40" rows="5"></textarea>
					<input type="submit" value="Comment"/>
				</form>

*/
