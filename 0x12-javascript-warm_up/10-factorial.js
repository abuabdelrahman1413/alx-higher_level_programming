#!/usr/bin/env node
const argv = process.argv.slice(2);
function factorial (num) {
  // Base case: Factorial of 0 is 1
  if (num === 0 || isNaN(num)) {
    return 1;
  }

  // Recursive case: Factorial of n is n * factorial(n-1)
  return num * factorial(num - 1);
}

console.log(factorial(argv[0]));
