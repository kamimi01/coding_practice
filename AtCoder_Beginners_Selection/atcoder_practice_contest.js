// ファイル読み込みのためのライブラリの読み込み
const fs = require('fs');

function Main(input) {
  // ファイルを読み込む
  let text = fs.readFileSync(input, {encoding: 'utf-8'});

  // a + b + cを定義する
  const text_array_new_line = text.split("\n");
  const tmp = text_array_new_line[1].split(" ");

  const a = parseInt(text_array_new_line[0], 10);
  const b = parseInt(tmp[0], 10);
  const c = parseInt(tmp[1], 10);
  const s = text_array_new_line[2];

  // a + b + cを計算する
  const sum = a + b + c;

  // 「a + b + c（空白)s」の形で出力する
  console.log("%d %s", sum, s);
};

Main("/dev/stdin");