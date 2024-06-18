#!/usr/bin/node
// 11-second_biggest.js
const args = process.argv.slice(2);
const arr = args.map(Number);
if (arr.length < 2) {
  console.log(0);
} else {
  arr.sort();
  console.log(arr[arr.length - 1]);
}
