$(document).ready(function () {
  $.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', function (jd) {
    jd.results.forEach(movie => {
      $('ul#list_movies').append(`<li>${movie.title}</li>`);
    });
  });
});
