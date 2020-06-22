$(document).ready(function(){
    
    // Document download
    $(document).on('click','.download-file', function(e){
      // download-file
        var name = $(this).attr('data-name');
        var type = $(this).attr('data-type');
        console.log(name);
        console.log(type);
        $.get('/download-encrypted-file/', {
            'name': name,
            'type' : type
        }, function(data) {
        	e.preventDefault(); 
		      window.location.href = data['url'];
		    
		    setTimeout(function(){
		    	 console.log("TO File to delete"); 
		 	  }, 1000);

        });
    });


  //   $(".ques-delete").click(function(event){
  //    var curr_obj = $(this);
  //    var quesId = $(this).data("qid");
  //    var con = confirm("Are you sure you want to delete this?");
  //    if(false == con){
  //      return false;
  //    }
  //    $.ajax({
  //       type:"POST",
  //       url:"/questions/deleteQuestion/",
  //       dataType: "json",
  //       data: {'question_id':quesId},
  //       success: function(question){
  //         $('#question-count').html(question.questioncount);
  //         location.reload();
  //       }
  //     });
  //   return false;
  // });

})

