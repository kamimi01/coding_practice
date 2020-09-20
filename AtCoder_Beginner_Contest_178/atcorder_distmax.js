function Main(input) {
  const text = input.split("\n");
  const N = text.slice(0, 1).map(x => +x)[0];
  const dis = text.slice(1);

  
}

Main(require("fs").readFileSync("sample.txt", "utf8"));  // テスト用
// Main(require("fs").readFileSync("/dev/stdin", "utf8"));   // 提出用