#!/usr/bin/node
const request = require('request');

const completed = {};
let uid;
request('https://jsonplaceholder.typicode.com/todos/', (error, response, body) => {
  if (error) {
    console.error(error);
  }
  JSON.parse(body).forEach((task) => {
    uid = task.userId.toString();
    if (!Object.keys(completed).includes(uid)) {
      completed[uid] = 0;
    }
    if (task.completed) {
      completed[uid] += 1;
    }
  });
  console.log(completed);
});
