#!/usr/bin/node
const fs = require('fs');

// Get the file paths from command line arguments
const fileA = process.argv[2];
const fileB = process.argv[3];
const destFile = process.argv[4];

// Read the content of the source files
const contentA = fs.readFileSync(fileA);
const contentB = fs.readFileSync(fileB);

// Concatenate the content of the files
const contentC = Buffer.concat([contentA, contentB]);

// Write the concatenated content to the destination file
fs.writeFileSync(destFile, contentC);