function GetRatings() {

    var health = document.getElementById("health_rating");
    var healthSpans = document.getElementById( 'health_rating' ).getElementsByTagName( 'span' );

    var style = document.getElementById("style_rating");
    var styleSpans = document.getElementById( 'style_rating' ).getElementsByTagName( 'span' );

    var cooking = document.getElementById("cooking_rating");
    var cookingSpans = document.getElementById( 'cooking_rating' ).getElementsByTagName( 'span' );

    var empty_star = "fa fa-star";
    var health_star_full = "fa fa-star checked_purple";
    var style_star_full = "fa fa-star checked_red";
    var cooking_star_full = "fa fa-star checked_blue";

    SetPictureRatingsStarClass(healthSpans, health_star_full, empty_star, health);
    SetPictureRatingsStarClass(styleSpans, style_star_full, empty_star, style);
    SetPictureRatingsStarClass(cookingSpans, cooking_star_full, empty_star, cooking);

}

function SetPictureRatingsStarClass(spanList, checkedClass, uncheckedClass, rating_type) {

    for (i = 0; i < rating_type.dataset.rating; i++) {
        spanList[i].className = checkedClass;
    }

    for (i = rating_type.dataset.rating; i < 5; i++) {
        spanList[i].className = uncheckedClass;
    }
}
