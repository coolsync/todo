// int getData(int value) {
//   return value;
// }

// String getData(String value) {
//   return value;
// }

// T getData<T>(T value) {
//   return value;
// }

// 不约定 return value 类型
getData<T>(T value) {
  return value;
}

void main() {
  // print(getData(10));
  // print(getData('hello'));

  // Call generic
  print(getData(10));

  print(getData<int>(10));
  print(getData<String>('hello'));
}
