function Main(input) {
  // ファイルの読み込み
  const text = input.split("\n").map(x => +x);

  const A = text[0],
        B = text[1],
        C = text[2],
        X = text[3];

  let count = 0;

  for (var a = 0; a <= A; ++a) {
    for (var b = 0; b <= B; ++b) {
      for (var c = 0; c <= C; ++c) {
          var sum = (a * 500) + (b * 100) + (c * 50);
          if (sum === X) ++count;
      }
    }
  }
  console.log(count);
};

// Main(require("fs").readFileSync("/dev/stdin", "utf8"));
Main(require("fs").readFileSync("sample.txt", "utf8"));