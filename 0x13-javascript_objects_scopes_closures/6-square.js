#!/usr/bin/node
// 6-square
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size); // Call parent class constructor with size for both width and height
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let counter = 0; counter < this.height; counter++) {
      let row = '';
      for (let index = 0; index < this.width; index++) {
        row += c;
      }
      console.log(row);
    }
  }
}

module.exports = Square;
