#!/usr/bin/node
function add (a, b) {
  return a + b;
}
const argA = parseInt(process.argv[2]);
const argB = parseInt(process.argv[3]);
console.log(add(argA, argB));
