#!/usr/bin/node
// 2-arguments.js
const process = require('process');

const args = process.argv.slice(2); // Get arguments excluding script path
console.log(args[0] + ' is ' + args[1]);
