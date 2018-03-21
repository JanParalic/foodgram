window.onload = function(){
    // your code

// Get the modal
var modal = document.getElementById('big_post');

// Get the button that opens the modal
var btn = document.getElementsByClassName('post_img');

var btn2 = document.getElementsByClassName('middle');

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

var body = document.getElementsByTagName('body')[0];

// When the user clicks the button, open the modal
for (var i = 0; i < btn.length; i++) {
    btn[i].addEventListener('click', function() {
    modal.style.display = "block";

    }, false);
}
for (var i = 0; i < btn2.length; i++) {
    btn2[i].addEventListener('click', function() {
    modal.style.display = "block";

    }, false);
}



// When the user clicks on <span> (x), close the modal
span.onclick = function() {
    modal.style.display = "none";
    body.style.overflow = "visible";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
        body.style.overflow = "visible";
    }
}


};

function viewBigPost(index) {
    var modal = document.getElementById('big_post ' + index.toString());

    modal.style.display = "block";
}