window.onload=function(){
var mainimg=document.querySelectorAll("#main-img");
var smallimg=document.querySelectorAll(".small-img");

smallimg[0].addEventListener("click",function() {
    mainimg[0].src=smallimg[0].src;
} );

smallimg[1].addEventListener("click",function() {
    mainimg[0].src=smallimg[1].src;
} );

smallimg[2].addEventListener("click",function() {
    mainimg[0].src=smallimg[2].src;
} );

smallimg[3].addEventListener("click",function() {
    mainimg[0].src=smallimg[3].src;
} );
}
