$(document).ready(function () {
  let data;
  $.ajax({
    type: 'GET',
    dataType: 'jsonp',
    // mimeType: 'application/json',
    crossDomain: true,
    url: 'https://stefanbohacek.com/hellosalut/?lang=fr',
    data: data,
    success: function (data) {
      console.log(JSON.parse(data));
    }
  });
});