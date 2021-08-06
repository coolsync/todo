foo() {}

void main(List<String> args) {
  print(foo()); // null

  // 函数体只有一对花括号， func 有一个隐藏得返回值: null
}
