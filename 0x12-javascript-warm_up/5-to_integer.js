#!/usr/bin/node
// 5-to_integer.js
const process = require('process');

const args = process.argv.slice(2); // Get arguments excluding script path

if (isNaN(args[0])) {
  console.log('Not a number');
} else {
  console.log('My number: ' + args[0]);
}
