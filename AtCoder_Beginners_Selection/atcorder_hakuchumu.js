function Main(input) {
  
  const suffixArray = ["dream", "dreamer", "erase", "eraser"];
  let result = "YES";

  for (const value of suffixArray) {
    if (input.indexOf(value) == -1) {
      result = "NO";
    }
  }
  
  console.log(result);
}

Main(require("fs").readFileSync("sample.txt", "utf8"));  // テスト用
// Main(require("fs").readFileSync("/dev/stdin", "utf8"));   // 提出用