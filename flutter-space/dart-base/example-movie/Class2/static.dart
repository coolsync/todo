class Person {
  static String name = "John";
  int age = 30;

  // static method
  static printInfo() {
    // print(this.name); // static method 不能使用 this keyword
    print(name);
    // print(age);   // static method 不能访问 非static property

    // printUserInfo();  // static method can't  no-static method
  }

  printUserInfo() {
    print(name); // 非 static method 可以访问 非static property
  }
}

void main() {
  // 静态method and 静态property 可以直接通过 类名 访问
  print(Person.name);
  print(Person.printInfo());

  var p = new Person();
  // print(p.name);   // static can't access by instance class
  // print(p.printInfo());
  print(p.age);
  print(p.printUserInfo());
}
