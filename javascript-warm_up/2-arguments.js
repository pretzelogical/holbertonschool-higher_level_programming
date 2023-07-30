#!/usr/bin/node
let argMessage;
if (process.argv.length === 3) {
  argMessage = 'Argument found';
} else if (process.argv.length > 3) {
  argMessage = 'Arguments found';
} else {
  argMessage = 'No argument';
}
console.log(argMessage);
