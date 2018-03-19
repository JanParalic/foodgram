window.onload = function(){
    // your code

// Get the modal
var modal = document.getElementById('addPicModal');

// Get the button that opens the modal
var btn = document.getElementById("add_pic");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close");

// When the user clicks the button, open the modal
btn.onclick = function() {
    modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
for (var i = 0; i < span.length; i++) {
    span[i].addEventListener('click', function() {
    modal.style.display = "none";

    }, false);
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}


};