void main(List<String> args) {
  // while 语句 用于评估条件后 执行；
  int i = 0;
  while (i <= 10) {
    print(i); // 输出 1 ~ 10
    i++;
  }

  // do while 语句 用于执行后 再评估条件
  int j = 10;
  do {
    print('do-while');
  } while (j < 2);
}
