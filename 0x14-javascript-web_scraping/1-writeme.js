#!/usr/bin/node

const fs = require('fs');

const filePath = process.argv[2];
const stringToWrite = process.argv[3];

fs.writeFile(filePath, stringToWrite, { encoding: 'utf-8' }, function (err) {
  if (err) {
    console.log(err);
    return;
  }

  console.log(`The string "${stringToWrite}" was written to the file ${filePath}!`);
});
