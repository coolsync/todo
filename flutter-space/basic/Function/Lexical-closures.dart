// 词法闭包

// 闭包是一个对象， function对象从闭包原始作用域外部调用， 可以访问到它词法作用域的变量

Function makeAdder(int addBy) {
  return (int i) => addBy + i;
}

void main() {
  var add2 = makeAdder(2); // 捕获 addBy 变量

  // int add2(i) {
  //   return i + 2;
  // }

  var add4 = makeAdder(4);

  print(add2(3) == 5);

  print(add4(5) == 9);
}
