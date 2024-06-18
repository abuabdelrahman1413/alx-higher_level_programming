#!/usr/bin/node
// 2-arguments.js
const process = require('process');

const args = process.argv.slice(2); // Get arguments excluding script path

if (args.length === 0) {
  console.log('No argument');
} else if (args.length === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
