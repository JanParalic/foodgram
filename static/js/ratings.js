function GetRatings() {

    var health = document.getElementsByClassName("health_rating")[0];
    var style = document.getElementsByClassName("style_rating")[0];
    var cooking = document.getElementsByClassName("cooking_rating")[0];

    var name = "span";

    var star_empty = "fa fa-star";
    var health_star_full = "fa fa-star checked_purple";
    var style_star_full = "fa fa-star checked_red";
    var cooking_star_full = "fa fa-star checked_blue";

    SetPictureRatingsStarClass(health, health_star_full, star_empty, name);
    SetPictureRatingsStarClass(style, style_star_full, star_empty, name);
    SetPictureRatingsStarClass(cooking, cooking_star_full, star_empty, name);

}

function SetPictureRatingsStarClass(rating_type, star_full, star_empty, id_name) {
    for (i = 0; i < rating_type.dataset.rating; i++) {
        //var span = GetElementInsideContainer(rating_type.id, id_name + (i + 1).toString());
        var span = GetElementInsideContainer(rating_type.id, i);
        /*var arr = span.className.split(" ");
        if (arr.indexOf(star_full) == -1) {
            span.className += " " + star_full;
        }*/
        span.className = star_full;
    }

    for (i = rating_type.dataset.rating; i < 5; i++) {
        //var span = GetElementInsideContainer(rating_type.id, id_name + (i + 1).toString());
        var span = GetElementInsideContainer(rating_type.id, i);
        /*var arr = span.className.split(" ");
        if (arr.indexOf(star_full) == -1) {
            span.className += " " + star_empty;
        }*/
        span.className = star_empty;
    }
}

function GetElementInsideContainer(div, i) {
    return document.getElementById(div).children[i];
}

/*function GetElementInsideContainer(containerID, childID) {
    var elm = document.getElementById(childID);
    var parent = elm ? elm.parentNode : {};
    return (parent.id && parent.id === containerID) ? elm : {};
}*/


