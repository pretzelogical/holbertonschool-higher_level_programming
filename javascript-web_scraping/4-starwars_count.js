#!/usr/bin/node
const request = require('request');

let wedgeAntilles = 0;
request(process.argv[2], (error, response, body) => {
  if (error) {
    console.error(error);
  }
  JSON.parse(body).results.forEach((movie) => {
    if (movie.characters.includes('https://swapi-api.hbtn.io/api/people/18/')) {
      wedgeAntilles++;
    }
  });
  console.log(wedgeAntilles);
});
