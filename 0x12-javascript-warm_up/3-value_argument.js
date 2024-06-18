#!/usr/bin/node
// 2-arguments.js
const process = require('process');

const args = process.argv.slice(2); // Get arguments excluding script path
if (!args[0]) {
  console.log('No argument');
} else {
  console.log(args[0]);
}
