#!/usr/bin/node

const square = require('./5-square');

class Square extends square {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let i = 0;
    for (i; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}
module.exports = Square;
