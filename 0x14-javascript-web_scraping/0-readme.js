#!/usr/bin/node
const fs = require('fs');
const argms = process.argv[2];

fs.readFile(argms, 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data.toString());
  }
});
