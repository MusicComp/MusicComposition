// Script for Sidebar, Tabs, Accordions, Progress bars and slideshows

// Side navigation
function w3_open() {
    var x = document.getElementById("mySidebar");
    x.style.width = "100%";
    x.style.fontSize = "36px";
    x.style.paddingTop = "10%";
    x.style.display = "block";
}

function w3_close() {
    document.getElementById("mySidebar").style.display = "none";
}