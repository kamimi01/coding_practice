function judgePrimeNumber(number) {
  let isPrimeNumber = false;
  if (number == 1) {
    return isPrimeNumber;
  }

  if (number != 2) {
    for (let i = 2; i < Math.sqrt(number) + 1; i++) {
      if (number % i == 0) {
        return isPrimeNumber;
      }
    }
  }

  isPrimeNumber = true;
  return isPrimeNumber;
}

console.log(judgePrimeNumber(6));


// judgePrimeNumber(require("fs").readFileSync("sample.txt", "utf8"));  // テスト用
// judgePrimeNumber(require("fs").readFileSync("/dev/stdin", "utf8"));   // 提出用