#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || isNaN(w) || isNaN(h)) {
      return {}; // Create an empty object
    }
    this.width = w;
    this.height = h;
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    // Exchange width and height
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    // Double width and height
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
