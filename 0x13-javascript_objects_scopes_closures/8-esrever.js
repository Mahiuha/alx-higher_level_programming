#!/usr/bin/node
exports.esrever = function (list) {
  const revsList = [];

  for (let i = list.length - 1; i >= 0; i--) {
    revsList.push(list[i]);
  }
  return revsList;
};
