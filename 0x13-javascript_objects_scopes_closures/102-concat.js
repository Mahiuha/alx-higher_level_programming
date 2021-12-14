#!/usr/bin/node
const file1 = process.argv[2];
const file2 = process.argv[3];
const newfile = process.argv[4];
const fs = require('fs');
const data1 = fs.readFileSync(file1, (err, data) => {
  if (err) throw err;
  return (data);
});
const data2 = fs.readFileSync(file2, (err, data) => {
  if (err) throw err;
  return (data);
});
fs.appendFile(newfile, data1, function (err) {
  if (err) throw err;
});
fs.appendFile(newfile, data2, function (err) {
  if (err) throw err;
});
