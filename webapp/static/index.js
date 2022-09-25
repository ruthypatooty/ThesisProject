function clickLicensePlate(id) {
  console.log(id)
  window.location.href = "/car/view?id=" + id;
}


function clickViolation(id) {
  console.log(id)
  window.location.href = "/violation/view?id=" + id;
}

(function ($) {

  $(".toggle-password").click(function () {

    $(this).toggleClass("zmdi-eye zmdi-eye-off");
    var input = $($(this).attr("toggle"));
    if (input.attr("type") == "password") {
      input.attr("type", "text");
    } else {
      input.attr("type", "password");
    }
  });

})(jQuery);


let currentURL = window.location.pathname;
console.log(currentURL);

if (currentURL === '/login' || currentURL.length === 1) {
  let hide = document.getElementById("logoutlink");
  hide.style.display = 'none';
} 
