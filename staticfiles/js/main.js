$(document).ready(function () {
  var backTop = $("#back-top");

  backTop.hide();

  $(window).scroll(function () {
    var scroll = $(document).scrollTop();
    console.log(scroll);

    if (scroll > 100) {
      backTop.fadeIn();
    } else {
      backTop.fadeOut();
    }
  });
});
