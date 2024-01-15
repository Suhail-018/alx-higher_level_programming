#!/usr/bin/node
// 2-arguments.js
// 2-arguments.js

const argsCount = process.argv.length - 2;

if (argsCount === 0) {
  console.log('No argument');
} else if (argsCount === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
