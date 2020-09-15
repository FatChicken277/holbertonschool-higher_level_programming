#!/usr/bin/node
if (!process.argv[2] || process.argv.length === 3) {
  console.log(0);
} else {
  let second = parseInt(process.argv[2]);
  let first = parseInt(process.argv[2]);
  process.argv.slice(2).forEach(val => {
    if (parseInt(val) > first) {
      second = first;
      first = val;
    }
  });
  console.log(second);
}
