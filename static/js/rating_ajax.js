$(document).ready(function(){
     $(".fa").click(function(){
         var picSlug = $(this).attr("data-picture");
         var type = $(this).attr("data-type");
         var value = $(this).attr("data-value");
         $.get("/foodfeed/make_rating/", {picture_slug: picSlug, type: type, value: value}, function(data){
            $('.post').hide();
         });
     });
});