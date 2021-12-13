#!/usr/bin/node

const squareSize = Number(process.argv[2]);

if (Number(process.argv[2])) {
  let i = 0;

  for (i; i < squareSize; i++) {
    console.log('X'.repeat(squareSize));
  }
} else {
  console.log('Missing size');
}
