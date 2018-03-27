// Script for Sidebar, Tabs, Accordions, Progress bars and slideshows

// Side navigation
//function w3_open() {
//    var x = document.getElementById("mySidebar");
//    x.style.width = "100%";
//    x.style.fontSize = "36px";
//    x.style.paddingTop = "10%";
//    x.style.display = "block";
//}
//
//function w3_close() {
//    document.getElementById("mySidebar").style.display = "none";
//}
//
//var columnList = document.getElementsByClassName("column");
//var input = 3;
//for (var i = 0; i < columnList.length; i++) {
//    columnList[i].addEventListener("mouseenter", mouseEnter);
//    columnList[i].addEventListener("mouseleave", mouseLeave);
//}
//
//function mouseEnter() {
//    MIDIjs.stop();
//    MIDIjs.play('{{ url_for('static', filename='midi/createdMidi2.mid') }}');
//}
//
//function mouseLeave() {
//    MIDIjs.stop();
//    MIDIjs.play('{{ url_for('static', filename='midi/createdMidi3.mid') }}');
//}
//
//document.addEventListener('keydown', function(event) {
//    if (event.keyCode == 37) {
//        mouseEnter();
//        input = 0;
//    } else if (event.keyCode == 38) {
//        playMIDI();
//    } else if (event.keyCode == 39) {
//        mouseEnter();
//        input = 1;
//    } else if (event.keyCode == 40) {
//        playIntro();
//    } else if (event.keyCode == 32) {
//        if (input == 0) {
//          window.location = "http://127.0.0.1:5000/secondQuestion";
//        } else if (input == 1) {
//          window.location = "http://127.0.0.1:5000/secondQuestion"
//        }
//    }
//});
//
//function playIntro() {
//    document.getElementById("my_audio").play();
//}
//
//function playMIDI() {
//    MIDIjs.play('{{ url_for('static', filename='midi/createdMidi.mid') }}');
//}
////window.onload = function () {
////    for (var i = 0; i < columnList.length; i++) {
////        columnList[i].onclick = function() {
////            selectAnswer(this);
////        }
////    }
////    playIntro();
////}
//
//function selectAnswer(columnClicked) {
//    if (columnClicked == columnList[0]) {
//        window.location = "http://127.0.0.1:5000/secondQuestion";
//    } else if (columnClicked == columnList[1]) {
//        window.location = "http://127.0.0.1:5000/secondQuestion";
//    }
//}