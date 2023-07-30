#!/usr/bin/node
if (process.argv[2] === undefined || process.argv[3] === undefined) {
  console.log('0');
  process.exit();
}
const numArray = [];
for (let i = 2; isNaN(parseInt(process.argv[i])) !== true; i++) {
  numArray.push(parseInt(process.argv[i]));
}
console.log(Math.max(...numArray.filter(num => num < Math.max(...numArray))));
