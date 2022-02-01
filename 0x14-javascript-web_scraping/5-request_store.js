#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const process = require('process');

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(process.argv[3], body, 'utf8', function (error, data) {
      if (error) {
        console.log(error);
      }
    });
  }
});
