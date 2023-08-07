$(document).ready(function () {
  $('div#toggle_header').click(function () {
    if ($('header').hasClass('green')) {
      $('header').removeClass('green');
      $('header').addClass('red');
    } else {
      $('header').addClass('green');
      $('header').removeClass('red');
    }
  });
});
