$(document).ready(function () {
  var backTop = $("#back-top");

  backTop.hide();

  $(window).scroll(function () {
    var scroll = $(document).scrollTop();

    if (scroll > 100) {
      backTop.fadeIn();
    } else {
      backTop.fadeOut();
    }
  });

  var dashHome = $("#dash-home");
  var dashProfile = $("#dash-profile");
  var dashProducts = $("#dash-products");
  var dashOrders = $("#dash-orders");

  var linkHome = $("#link-home");
  var linkProfile = $("#link-profile");
  var linkProducts = $("#link-products");
  var linkOrders = $("#link-orders");

  var divHome = $("#div-home");
  var divProfile = $("#div-profile");
  var divProducts = $("#div-products");
  var divOrders = $("#div-orders");

  divProfile.hide();
  divProducts.hide();
  divOrders.hide();

  dashHome.click(function () {
    linkHome.addClass("active");
    linkProfile.removeClass("active");
    linkProducts.removeClass("active");
    linkOrders.removeClass("active");

    divProfile.hide();
    divProducts.hide();
    divOrders.hide();
    divHome.fadeIn();
  });

  dashProfile.click(function () {
    linkHome.removeClass("active");
    linkProfile.addClass("active");
    linkProducts.removeClass("active");
    linkOrders.removeClass("active");

    divProducts.hide();
    divOrders.hide();
    divHome.hide();
    divProfile.fadeIn();
  });

  dashProducts.click(function () {
    linkHome.removeClass("active");
    linkProfile.removeClass("active");
    linkProducts.addClass("active");
    linkOrders.removeClass("active");

    divOrders.hide();
    divHome.hide();
    divProfile.hide();
    divProducts.fadeIn();
  });

  dashOrders.click(function () {
    linkHome.removeClass("active");
    linkProfile.removeClass("active");
    linkProducts.removeClass("active");
    linkOrders.addClass("active");

    divHome.hide();
    divProfile.hide();
    divProducts.hide();
    divOrders.fadeIn();
  });

  var prodDescription = $("#prod-description");
  var toggleDescription = $(".toggle-description");

  prodDescription.hide();

  toggleDescription.click(function () {
    prodDescription.slideToggle();
  });

  var beginCheckout = $(".to-checkout");
  var checkoutContainer = $(".checkout-container");

  checkoutContainer.hide();

  beginCheckout.click(function () {
    checkoutContainer.slideToggle();
  });
});
