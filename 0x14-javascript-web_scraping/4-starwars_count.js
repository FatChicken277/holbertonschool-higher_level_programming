#!/usr/bin/node
if (process.argv.length === 3) {
  const request = require('request');
  request(process.argv[2], function (err, res, body) {
    if (res.statusCode === 200) {
      const films = JSON.parse(body);
      let count = 0;
      for (const film of films.results) {
        if (film.characters.includes('https://swapi-api.hbtn.io/api/people/18/')) {
          count++;
        }
      }
      console.log(count);
    } else {
      console.log(err);
    }
  });
}
