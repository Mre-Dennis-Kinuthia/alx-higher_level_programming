#!/usr/bin/node
if (process.argv.length < 4) {
  console.log(0);
} else {
  const args = process.argv
    .slice(2).sort(function (a, b) { return a - b; });
  console.log(args[args.length - 2]);
}
