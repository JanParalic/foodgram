$(document).ready(function(){
    $(".fa").click(function(){
		$.get('/foodfeed/rate/', {recipe_id: recipeid}, function(data){
            alert('taute');
		});



});
});
