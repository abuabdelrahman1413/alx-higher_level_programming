#!/usr/bin/node
// 11-second_biggest.js
const args = process.argv.slice(2);
let numbers = [];
numbers = args.map(Number);
if (numbers.length < 2) {
  console.log(0);
} else {
  numbers.sort();
  console.log(numbers[numbers.length - 2]);
}
