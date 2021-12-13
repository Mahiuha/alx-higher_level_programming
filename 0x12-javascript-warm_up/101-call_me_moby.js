#!/usr/bin/node

exports.callMeMoby = function (xNum, theFunction) {
  let i = 0;
  for (i; i < xNum; i++) {
    theFunction();
  }
};
