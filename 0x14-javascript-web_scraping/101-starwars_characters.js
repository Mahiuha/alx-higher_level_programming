#!/usr/bin/node
// Prints all characters of a Star Wars movie
const request = require('request');
request(`https://swapi-api.hbtn.io/api/films/${process.argv[2]}`, (error, response, body) => {
  if (error) throw error;
  else {
    send(JSON.parse(body).characters, 0);
  }
});

function send (person, idx) {
  if (idx >= person.length) {
    return;
  }
  request(person[idx], (error, response, body) => {
    if (error) throw error;
    else {
      console.log(JSON.parse(body).name);
      return send(person, ++idx);
    }
  });
}
