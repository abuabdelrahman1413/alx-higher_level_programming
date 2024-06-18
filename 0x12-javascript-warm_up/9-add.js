#!/usr/bin/node
// 9-add.js
const args = process.argv.slice(2);
function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    console.log('NaN');
  } else {
    const sum = parseInt(a) + parseInt(b);
    console.log(sum);
  }
}

add(args[0], args[1]);
