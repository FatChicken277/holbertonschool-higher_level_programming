#!/usr/bin/node
const dictionary = require('./101-main').dict;
const newDict = {};
for (const key in dictionary) {
  if (newDict[dictionary[key]] === undefined) {
    newDict[dictionary[key]] = [];
  }
  newDict[dictionary[key]].push(key);
}
console.log(newDict);