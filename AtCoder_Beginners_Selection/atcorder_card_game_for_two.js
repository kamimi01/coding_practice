const { constants } = require("buffer");

function Main(input) {
  // ファイル読み込み
  const text = input.split("\n");
  const a = parseInt(text[0], 10),
        b = text[1].split(" ").map(x => +x).slice().sort((a, b) => b - a);

  let asum = 0,
      bsum = 0;
  
  // console.log(a, b);

  // a:0,2,4
  // b:1,3,5

  for (let i = 0; i < a; i++) {
    (i % 2 == 0) ? asum += b[i] : bsum += b[i];
  }
  
  const result = (asum <= bsum) ? bsum - asum : asum - bsum;

  console.log(result);
}

Main(require("fs").readFileSync("/dev/stdin", "utf8"));
// Main(require("fs").readFileSync("sample.txt", "utf8"));

function Main(input) {
	
}

Main(require("fs").readFileSync("sample.txt", "utf8"));  // テスト用
// Main(require("fs").readFileSync("/dev/stdin", "utf8"));   // 提出用