#!/usr/bin/node
const request = require('request');

const me = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/films/' + me;
request(url, function (error, response, body) {
  if (error) throw error;
  for (const character of JSON.parse(body).characters) {
    request(character, function (error, response, body) {
      if (error) throw error;
      console.log(JSON.parse(body).name);
    });
  }
});
