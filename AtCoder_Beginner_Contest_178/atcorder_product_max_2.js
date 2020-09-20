function Main(input) {
  input = input.trim().split("\n").map(function(x) { return x.split(" ")});
  let a = BigInt(input[0][0], 10);
  let b = BigInt(input[0][1], 10);
  let c = BigInt(input[0][2], 10);
  let d = BigInt(input[0][3], 10);
  let ans = a * c;
  if (ans < a * d) ans = a * d;
  if (ans < b * c) ans = b * c;
  if (ans < b * d) ans = b * d;
  console.log(ans.toString());

}

Main(require("fs").readFileSync("/dev/stdin", "utf8"));