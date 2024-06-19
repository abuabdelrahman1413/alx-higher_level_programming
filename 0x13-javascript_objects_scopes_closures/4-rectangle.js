#!/usr/bin/node
// 4-rectangle.js
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

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }

  rotate () {
    const tmp = this.height;
    this.height = this.width;
    this.width = tmp;
  }
}

module.exports = Rectangle;
