#!/usr/bin/node

let i = 0;
if (process.argv[2]) {
  for (i; i < process.argv[2]; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrencest');
}
