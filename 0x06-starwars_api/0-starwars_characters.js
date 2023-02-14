#!/usr/bin/node

const request = require('request');

request('https://swapi-api.alx-tools.com/films/'+ process.argv[2], function (error, response, body) {
  if (error) throw error;
  for (const character of JSON.parse(body).characters) {
    request(character, function (error, response, body) {
      if (error) throw error;
      console.log(JSON.parse(body).name);
    });
  }
});
