class Person {
  String name;

  // `_` -> 私有属性
  num _money = 100;

  num getMoney() {
    return this._money;
  }

  void _wife() {
    print('我的 wife $name');
  }

  Person(this.name);
}
