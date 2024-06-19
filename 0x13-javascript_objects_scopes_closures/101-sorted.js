#!/usr/bin/node
const dict = require('./101-data.js').dict;
let newDict = {};
for (let key in dict) {
  let value = dict[key];
  if (newDict[value] === undefined) {
     newDict[value] = [key];
  } else {
    newDict[value].push(key);
  }
}
console.log(newDict);
