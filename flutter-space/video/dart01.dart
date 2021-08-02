// 简写模式
// main() => print('hello');

main(List<String> args) {
  String name = 'bob';
  // name = 123;  // error

  dynamic name2 = 'bob';
  name2 = 123;

  Object abc = 'abc';
  abc = 123;

  var name3 = 'paul';
  // name3 = 456;  // error 
}
