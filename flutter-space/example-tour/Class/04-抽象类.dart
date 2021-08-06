abstract class Animal {
  eat(); // 抽象方法
  run(); // 抽象方法
  void print_info() {
    print('这是普通方法');
  }
}

class Dog extends Animal {
  @override
  eat() {     // 抽象方法必须实现
    print('小狗在啃骨头');
  }

  @override
  run() {
    print('dog is run...');
  }
}

void main() {
  var dog = new Dog();
  dog.eat();
  dog.run();
  dog.print_info();
}
