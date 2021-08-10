class BaseClass {}

// class MixinA extends BaseClass {    // Mixin class only extends Object class
// class MixinA extends Object {
class MixinA {
  String name = 'MixinA';

  // MixinA(this.name);    // Mixin calss can't have constructor function

  void printA() {
    print('A');
  }

  void run() {
    print('A is running');
  }
}

mixin MixinB {
  String name = 'MixinB';

  void printB() {
    print('B');
  }

  void run() {
    print('B is running');
  }
}

// class MyClass extends MixinA with MixinB {}
class MyClass with MixinA, MixinB {}

void main() {
  var c = new MyClass();
  c.printA();
  c.printB();

  // 后引入的 Mixin 类, 会覆盖前面的 Mixin 类的内容
  //The Mixin class introduced later will cover the content of the previous Mixin class
  print(c.name);
  c.run();
}
