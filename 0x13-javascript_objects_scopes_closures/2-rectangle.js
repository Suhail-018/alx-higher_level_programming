#!/usr/bin/node
// 2-rectangle.js

class Rectangle {
  constructor(w, h) {
    if (w <= 0 || h <= 0 || isNaN(w) || isNaN(h)) {
      // Initialize width and height to undefined if w or h is 0 or not a positive integer
      this.width;
      this.height;
    } else {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
