$(document).ready(function(){
    $(".fa").click(function(){

		var recipeid;
		recipeid = $(this).attr("data-rating");
		$.get('/foodfeed/add_comment/', {recipe_id: recipeid}, function(data){
			//$('#comment_field').html(data);
			$('.post').hide();
		});

alert('taute')

});
});
