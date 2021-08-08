class CommonClass {
  Set s = new Set();

  void add(int value) {
    this.s.add(value);
  }

  void info() {
    print(this.s);
  }
}

class GenericClass<T> {
  Set s = new Set<T>();

  void add(T value) {
    this.s.add(value);
  }

  void info() {
    print(this.s);
  }
}

void main() {
  var c = new CommonClass();
  c.add(1);
  c.add(2);
  c.info();
  // c.add('hello');  err

  // Instance Generic class
  var g = new GenericClass<int>();
  g.add(1);
  g.add(2);
  // g.add('hello');
  g.info();

  var g1 = new GenericClass<String>();
  g1.add('hello');
  g1.add('world');
  g1.info();

  // Biult-in Generic
  Set s = new Set<int>();
  s.add(1);
  // s.add('hello'); // err
  s.add(3);
  print(s);

  // 字面量形式的Generic
  Set s1 = <int>{};
  s1.add(1);
  // s.add('hello'); // err
  s1.add(3);
  print(s1);
}
