// 声明类
class Person {
  String? name; // 属性

  // 方法
  void printInfo() {
    print('我是 $name');
  }
}

void main() {
  // Instance class
  Person p = new Person();
  p.name = 'Bob'; // assign value to property of object

  // access property
  print(p.name);

  // access method
  p.printInfo();

  // 在Dart中 所有内容都是对象
  Map m = new Map();
  print(m.length);
  m.addAll({'name': 'Paul', 'age': 20});
  print(m.length);
}
