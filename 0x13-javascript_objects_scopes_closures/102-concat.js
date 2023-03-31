#!/usr/bin/node
const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];
if (fileA && fileB && fileC) {
    const fs = require('fs');
    let text = '';
    text += fs.readFileSync(fileA);
    text += fs.readFileSync(fileB);
    fs.writeFileSync(fileC, text);
}