function Main(input) {
  const text = input.split("\n").map(x => +x);
  const num = text[0];

  const tmpmochiarray = text.slice(1, text.length);
  const mochiarray = Array.from(new Set(tmpmochiarray));

  const result = mochiarray.length;
  console.log(result); 
}

Main(require("fs").readFileSync("sample.txt", "utf8"));  // テスト用
// Main(require("fs").readFileSync("/dev/stdin", "utf8"));   // 提出用


// 以下の重複削除実装は、計算量が多いため、setを使うべし!(ただし、今のatcorderのnode.jsバージョンだとsetは使えない)
// function main(input) {
//   const args = input.split('\n');
//   const N = args[0],
//         nums = args.slice(1, args.length - 1);

//   console.log(nums.filter((n, i) => nums.indexOf(n) === i).length);
// }
// // main(require('fs').readFileSync('/dev/stdin', 'utf8'));
// main(require("fs").readFileSync("sample.txt", "utf8"));  // テスト用