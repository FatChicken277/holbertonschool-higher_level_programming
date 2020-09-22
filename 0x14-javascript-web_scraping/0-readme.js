#!/usr/bin/node
if (process.argv.length === 3) {
  const fs = require('fs');
  try {
    console.log(fs.readFileSync(process.argv[2], 'utf-8'));
  } catch (err) {
    console.log(err);
  }
}
