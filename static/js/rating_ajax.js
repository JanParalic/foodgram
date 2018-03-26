$(document).ready(function(){
     $(".fa").click(function(){
         var picSlug = $(this).dataset.picture;
         var type = $(this).dataset.type;
         var value = $(this).dataset.value;
         $.get('/foodfeed/make_rating/', {picture_slug: picSlug, type: type, value: value}, function(data){
 			$('.post').hide();
         });
     alert('taute');
     });
});