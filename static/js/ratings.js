function GetRatings() {

    var health = document.getElementById("health_rating");
    var healthSpans = document.getElementById( 'health_rating' ).getElementsByTagName( 'span' );

    var style = document.getElementById("style_rating");
    var styleSpans = document.getElementById( 'style_rating' ).getElementsByTagName( 'span' );

    var cooking = document.getElementById("cooking_rating");
    var cookingSpans = document.getElementById( 'cooking_rating' ).getElementsByTagName( 'span' );


    var health_star_full = "checked_purple";
    var style_star_full = "checked_red";
    var cooking_star_full = "checked_blue";

    SetPictureRatingsStarClass(healthSpans, health_star_full, health);
    SetPictureRatingsStarClass(styleSpans, style_star_full, style);
    SetPictureRatingsStarClass(cookingSpans, cooking_star_full,cooking);

}

function SetPictureRatingsStarClass(spanList,checkedClass, rating_type) {
    for(i=0; i<5; i++){
        if(spanList[i].classList.contains(checkedClass)){
            spanList[i].classList.remove(checkedClass);

        }
    }

    for (i = 0; i < rating_type.dataset.rating; i++) {
        spanList[i].classList.add(checkedClass);
    }

//    for (i = rating_type.dataset.rating; i < 5; i++) {
//
//    }
}

function GetElementInsideContainer(div, i) {
    return document.getElementById(div).children[i];
}


