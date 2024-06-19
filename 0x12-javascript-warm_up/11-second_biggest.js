#!/usr/bin/node
// 11-second_biggest.js
const args = process.argv.slice(2);
let numbers = [];
numbers = args.map(Number);
numbers.sort((a, b) => b - a);
if (numbers.length < 3) {
  console.log(0);
} else {
  console.log((parseInt(numbers[1])));
}
