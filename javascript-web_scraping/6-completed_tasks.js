#!/usr/bin/node
const request = require('request');


function removeNoTasks (completed) {
  const noTasks = [];
  for (const user in completed) {
    if (completed[user] === 0) {
      noTasks.push(user);
    }
  }
  noTasks.forEach((user) => {
    delete completed[user];
  });
}

request(process.argv[2], (error, response, body) => {
  if (error) {
    console.error(error);
  }

  let uid;
  const completed = {};
  const tasks = JSON.parse(body);
  tasks.forEach((task) => {
    uid = task.userId.toString();
    if (!Object.keys(completed).includes(uid)) {
      completed[uid] = 0;
    }
    if (task.completed) {
      completed[uid] += 1;
    }
  });
  removeNoTasks(completed);
  console.log(completed);
});
