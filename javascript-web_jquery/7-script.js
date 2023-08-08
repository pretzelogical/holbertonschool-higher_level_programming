$(document).ready(function () {
  $.getJSON('https://swapi-api.hbtn.io/api/people/5/?format=json', function (jd) {
    $('div#character').text(jd.name);
  });
});
