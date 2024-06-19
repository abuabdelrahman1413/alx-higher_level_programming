#!/usr/bin/node
// 5-square.js
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size); // Call parent class constructor with size for both width and height
  }
}

module.exports = Square;
