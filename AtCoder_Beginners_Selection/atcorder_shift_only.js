function Main(input) {
  const text_array = input.split("\n");
  let text_array_number = text_array[1].split(" ").map(x => +x);
  // console.log(text_array_number);

  let count = 0;
  while (!text_array_number.map(x => +x).map(x => x % 2).includes(1)) {
    text_array_number = text_array_number.map(x => x / 2);
    // console.log(text_array_number);
    count++;
  };
  console.log(count);

};

Main(require('fs').readFileSync('/dev/stdin', 'utf8'));