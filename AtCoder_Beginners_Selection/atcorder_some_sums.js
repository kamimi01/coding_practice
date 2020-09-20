function Main(input) {
  const text = input.split(" ").map(x => +x);
  const N = text[0],
        A = text[1],
        B = text[2];

  let sum = 0;
  
  for (let i = 1; i <= N; i++) {
    // console.log(i);
    const i_split = String(i).split("").map(x => +x);
    // console.log(i_split);
    let split_sum = 0;
    for (let h = 0; h < i_split.length; h++) {
      // console.log(i_split[h]);
      split_sum += i_split[h];
    };
    // console.log("各桁の合計：", split_sum);

    if (A <= split_sum && split_sum <= B) {
      // console.log("これから足すのは:", split_sum);
      sum += i;
      // console.log("合計は：", sum);
    } else {
      // console.log("足さない");
    };

    // console.log("足した結果：", sum, "\n=====");
  };

  console.log(sum);
};

Main(require("fs").readFileSync("/dev/stdin", "utf8"));
// Main(require("fs").readFileSync("sample.txt", "utf8"));