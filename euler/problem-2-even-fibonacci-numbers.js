function fiboEvenSum(n) {
  // Fib(1) = 1 which is not a even-valed term, thus
  // we can start with 2
  let sum = 0;
  let x = 1, y = 2;
  while (y <= n) {
    if (y % 2 == 0) {
      sum += y;
    }
    let t = x + y;
    x = y;
    y = t;
  }
  return sum;
}