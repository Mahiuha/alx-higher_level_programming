#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request.get(url, function (err, url) {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ' + url.statusCode);
  }
});
