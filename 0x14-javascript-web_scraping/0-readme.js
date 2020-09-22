#!/usr/bin/node
if (process.argv.length === 3) {
  const fs = require('fs');
  try {
    console.log(fs.readFileSync(process.argv[2]).toString('utf8'));
  } catch (err) {
    console.log(JSON.stringify(err));
  }
}
