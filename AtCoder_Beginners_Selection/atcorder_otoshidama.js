function Main(input) {
  const text = input.split(" ").map(x => +x);
  const billnum = text[0];
  const otoshi = text[1];

  let x = 0,
      y = 0,
      z = 0;

  let uncleRight = false;
  
  for (let i = 0; i <= billnum; i++) {
    for(let j = 0; j <= billnum; j++) {
      if (billnum < (i + j)) {
        break;
      }
      if ((10000 * i + 5000 * j + 1000 * (billnum - i - j)) == otoshi) {
        x = i,
        y = j,
        z = billnum - i - j;
        uncleRight = true;
      }
    }
  }
  
  const result = (uncleRight) ? (x + " " + y + " " + z) : ("-1 -1 -1");
  console.log(result);
}

// Main(require("fs").readFileSync("sample.txt", "utf8"));  // テスト用
Main(require("fs").readFileSync("/dev/stdin", "utf8"));   // 提出用