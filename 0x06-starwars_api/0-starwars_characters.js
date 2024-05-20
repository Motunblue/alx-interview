#!/usr/bin/node

const request = require('request');

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request(url, (err, res, body) => {
  if (err) {
    console.error(err);
  } else {
    const characters = JSON.parse(body).characters;
    getCharacters(characters);
  }
});

async function getCharacters (characters) {
  let char;
  for (char of characters) {
    const character = await fetchCharacter(char);
    console.log(character.name);
  }
}

function fetchCharacter (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, res, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
}
