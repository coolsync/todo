// 1 使用命令行 访问使用参数的 main function
// void main(List<String> args) {
//   print(args); // [1, test]

//   print(args.length);

//   print(int.parse(args[0]) == 1);

//   print(args[1] == 'test');
// }

// 2  将 function 作为参数 传递给 另一个  function
void print_element(int elem) {
  print(elem);
}

var list = [1, 2, 3];

// 3 assign a function to a variable
// 分配 一个 function 作为 一个 变量使用
var loudify = (msg) => '!!! ${msg.toUpperCase()} !!!';

void main() {
  list.forEach(print_element);
  print(loudify('hello'));
}
