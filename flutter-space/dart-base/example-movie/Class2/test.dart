// 1 2 3 4 5 6
// 0 1 1 2 3 5 8 13 ...

int fibonacci(n) {
  if (n == 0 || n == 1) return n;
  return fibonacci(n - 1) + fibonacci(n - 2);
}

int fibonacci2(n) {
  if (n == 0 || n == 1) return n;

  var first = 0;
  var secode = 1;

  for (var i = 0; i < n - 1; i++) {
    int sum = first + secode;
    first = secode;
    secode = sum;
  }

  return secode;
}

void main() {
  // print(fibonacci(50));
  print(fibonacci2(50));
  
}
