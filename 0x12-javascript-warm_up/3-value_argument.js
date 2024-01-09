#!/usr/bin/node

const argvarr = process.argv;

if (argvarr[2]) {
  console.log(argvarr[2]);
} else {
  console.log('No argument');
}
