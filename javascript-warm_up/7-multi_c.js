#!/usr/bin/node
const arg = parseInt(process.argv[2]);
if (isNaN(arg)) {
  console.log('Missing number of occurrences');
  process.exit();
}

for (let i = 0; arg > i; i++) {
  console.log('C is fun');
}
