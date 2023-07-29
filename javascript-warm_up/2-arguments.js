#!/usr/bin/node
console.log(process.argv);
console.log(process.argv.length);
let argMessage;
if (process.argv.length > 2) {
  argMessage = 'Argument found';
} else {
  argMessage = 'No argument';
}
console.log(argMessage);
