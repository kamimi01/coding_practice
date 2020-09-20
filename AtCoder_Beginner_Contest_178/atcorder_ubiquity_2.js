function Main(input) {
  const N = parseInt(input, 10);
  const mod = BigInt(Math.pow(10, 9) + 7);

  const ten = BigInt(Math.pow(10, N));
  const nine = BigInt(Math.pow(9, N));
  const eight = BigInt(Math.pow(8, N));

  const result = (ten - 2 * nine + eight) % mod;

  console.log(result);
}

Main(require("fs").readFileSync("sample.txt", "utf8"));  // テスト用
// Main(require("fs").readFileSync("/dev/stdin", "utf8"));   // 提出用