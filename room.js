window.onload = function () {
  var mainimg = document.querySelectorAll("#main-img");
  var smallimg = document.querySelectorAll(".small-img");

  smallimg[0].addEventListener("click", function () {
    mainimg[0].src = smallimg[0].src;
  });

  smallimg[1].addEventListener("click", function () {
    mainimg[0].src = smallimg[1].src;
  });

  smallimg[2].addEventListener("click", function () {
    mainimg[0].src = smallimg[2].src;
  });

  smallimg[3].addEventListener("click", function () {
    mainimg[0].src = smallimg[3].src;
  });

  smallimg[4].addEventListener("click", function () {
    mainimg[1].src = smallimg[4].src;
  });

  smallimg[5].addEventListener("click", function () {
    mainimg[1].src = smallimg[5].src;
  });

  smallimg[6].addEventListener("click", function () {
    mainimg[1].src = smallimg[6].src;
  });

  smallimg[7].addEventListener("click", function () {
    mainimg[1].src = smallimg[7].src;

    smallimg[8].addEventListener("click", function () {
      mainimg[1].src = smallimg[8].src;
    });
  });
};
