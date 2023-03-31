#!/usr/bin/node
class Square extends require('./5-square') {
  charPrint (c) {
    let printChar = c;
    if (printChar === undefined) {
      printChar = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(printChar.repeat(this.width));
    }
  }
}

module.exports = Square;
