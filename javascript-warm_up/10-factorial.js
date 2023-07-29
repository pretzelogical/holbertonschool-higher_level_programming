#!/usr/bin/node
function factorial (x) {
  if (x === 0) {
    return 1;
  }
  return x * factorial(x - 1);
}
let arg = parseInt(process.argv[2]);
if (isNaN(arg)) {
  arg = 1;
}
console.log(factorial(arg));
