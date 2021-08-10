import 'lib/Person.dart';

void main() {
  var p1 = Person('Seth');
  print(p1.name);

  // 访问 私有property
  // print(p1._money); // err

  // 通过方法访问 私有property
  print(p1.getMoney()); // 100

  // 访问 私有method
  // print(p1._wife());  // 无法访问
}
