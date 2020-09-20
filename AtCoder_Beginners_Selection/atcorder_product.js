const fs = require("fs");

function Main(input) {
  const text = fs.readFileSync(input, "utf-8");
  const text_array = text.split(" ");

  const a = parseInt(text_array[0], 10);
  const b = parseInt(text_array[1], 10);

  // 計算する
  const calc_result = a * b % 2;
  const result = (calc_result == 0) ? "Even" : "Odd";

  console.log(result);
};

Main("/dev/stdin");
