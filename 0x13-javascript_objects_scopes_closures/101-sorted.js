#!/usr/bin/node
const dictionary = require('./101-main').dict;
const newDict = {};
for (const [key, value] of Object.entries(dictionary)) {
  if (newDict[value] !== undefined) {
    newDict[value].push(key);
  } else {
    newDict[value] = [key];
  }
}
console.log(newDict);
