$(document).ready(function(){
     $(".fa").click(function(){
         var picSlug = $(this).attr("data-picture");
         var type = $(this).attr("data-type");
         var value = $(this).attr("data-value");
         var index = $(this).attr("data-index");
         $.get("/foodfeed/make_rating/", {picture_slug: picSlug, type: type, value: value}, function(data){
             $("#big_post" + index).hide();
         });
     });

     $("#commentForm").submit(function(event){
         event.preventDefault();
         var values = $(this).serializeArray();
         var formValuesDict = {};

         $(values).each(function(i, field){
             formValuesDict[field.name] = field.value;
         });

         var picSlug = formValuesDict["picture"];
         var comment = formValuesDict["comment"];
         $.get("/foodfeed/add_comment/", {picture_slug: picSlug, comment: comment}, function (data) {
             $("#commentForm").html(data);
         });
     });
});