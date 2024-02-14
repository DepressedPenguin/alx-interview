#!/usr/bin/node

const request = require('request');

request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (err, res, body) {
  if (err) throw err;

  try {
    const filmData = JSON.parse(body);
    const actors = filmData.characters;

    if (!Array.isArray(actors)) {
      throw new Error('Invalid or missing "characters" field in API response.');
    }

    for (const actorURL of actors) {
      request(actorURL, function (err, res, body) {
        if (err) throw err;
        console.log(JSON.parse(body).name);
      });
    }
  } catch (error) {
    console.error('Error parsing or processing API response:', error.message);
  }
});
