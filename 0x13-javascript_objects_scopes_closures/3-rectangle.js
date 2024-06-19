#!/usr/bin/node
// 3-rectangle.js
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let counter = 0; counter < this.height; counter++) {
      let row = '';
      for (let index = 0; index < this.width; index++) {
        row += 'X';
      }
      console.log(row);
    }
  }
}

module.exports = Rectangle;
