class Person {
  // 父类
  String? name;
  int? age;
  void run() {
    print('Person run ...');
  }
}

class Student extends Person {  // 继承类
  @override
  void run() {
    print('Student ${name} run...');
  }

  void study() {
    print('Student ${name} study...');
  }
}

void main() {
  var s = new Student();
  s.name = 'Bob';
  s.study();
  s.run();
}
