function Main(input) {
  const text_array = input.split("");
  let count1 = 0;

  for(let i = 0; i < text_array.length; i++) {
    let number = parseInt(text_array[i], 10);
    if (number == 1) {
      count1++;
    };
  };

  console.log(count1);
};

Main(require('fs').readFileSync('/dev/stdin', 'utf8'));