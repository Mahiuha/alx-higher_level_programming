#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let numberOcurr = 0;
  let i = 0;

  for (i; i < list.length; i++) {
    if (list[i] === searchElement) {
      numberOcurr++;
    }
  }
  return numberOcurr;
};
