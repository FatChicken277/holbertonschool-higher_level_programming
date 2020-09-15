#!/usr/bin/node
if (!process.argv[2] || process.argv.length === 3) {
  console.log(0);
} else {
  let second = parseInt(process.argv[2]);
  let first = parseInt(process.argv[2]);
  for (let i = 2; i < process.argv.length - 1; i++) {
    if (process.argv[i] > first) {
      second = first;
      first = parseInt(process.argv[i]);
    }
  }
  console.log(second);
}
