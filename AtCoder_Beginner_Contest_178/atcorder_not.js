function Main(input) {
  const result = (input == 0) ? 1 : 0;
  console.log(result);
}

Main(require("fs").readFileSync("sample.txt", "utf8"));  // テスト用
// Main(require("fs").readFileSync("/dev/stdin", "utf8"));   // 提出用