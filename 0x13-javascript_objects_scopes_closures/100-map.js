#!/usr/bin/node
// 100-map.js
const list = require('./100-data'); // Import the list array from 100-data.js

// Using map to compute a new array where each element is the original element multiplied by its index

// Print the original list
console.log(list);

// Print the new computed list
console.log(list.map((value, index) => value * index));
