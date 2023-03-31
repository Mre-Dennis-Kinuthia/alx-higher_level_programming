#!/usr/bin/node
const list = require('./100-data').list;
console.log(list);
const mappedList = list.map(function (element, idx) { return element * idx; });
// const mappedList = list.map((element, idx) => element * idx);
console.log(mappedList);