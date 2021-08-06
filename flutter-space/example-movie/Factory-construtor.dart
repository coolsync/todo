// class Person {
//   String name;

//   static Person instance = Person('bob');

//   // 工厂构造函数
//   factory Person([String name = '刘备']) {
//     // print(this.name);   // 不能使用 this

//     if (Person.instance == null) {
//       Person.instance = new Person.newSelf(name);
//     }
//     return Person.instance;
//   }

// // A value of type 'Person?' can't be returned from the constructor 'Person' because it has a return type of 'Person'.
//   // 命名构造函数
//   Person.newSelf(this.name);
// }

class Person {
  String name;

  static Person instance;

  // 工厂构造函数
  factory Person([String name = '刘备']) {
    // print(this.name);   // 不能使用 this

    if (Person.instance == null) {
      Person.instance = Person.newSelf(name);
    }
    return Person.instance;
  }

  // 命名构造函数
  Person.newSelf(this.name);
}

void main() {
  // 实例化操作
  var p1 = new Person('关羽');
  print(p1.name);
}
