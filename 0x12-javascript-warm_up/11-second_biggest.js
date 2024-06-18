#!/usr/bin/node
// 11-second_biggest.js
const args = process.argv.slice(2);
const numbers = [];
for (let i = 0; i < args.length; i++) {
  numbers.push(args[i]);
}
if (numbers.length < 2) {
  console.log(0);
} else {
  numbers.sort();
  console.log(numbers[numbers.length - 1]);
}
