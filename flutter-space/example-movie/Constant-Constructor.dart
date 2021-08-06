class Point {
  num x, y;

  Point(this.x, this.y);
}

class ImmutablePoint {
  // Constant Constructor 能够提高程序速度

  // Property must be by final keyword define
  final num x, y;

  // const ImmutablePoint(this.x, this.y){} // can't have a body
  const ImmutablePoint(this.x, this.y);
}

void main() {
  var p1 = new Point(1, 2);
  var p2 = new Point(1, 2);
  print(p1 == p2); // false

  // 实例化常量构造函数的类

  // 使用 new 时， 常量构造函数被当做普通构造使用
  var p3 = new ImmutablePoint(1, 2);
  var p4 = new ImmutablePoint(1, 2);
  print(p3 == p4); // false

  // constant construct function, use const
  var p5 = const ImmutablePoint(1, 2);
  var p6 = const ImmutablePoint(1, 2);
  print(p5 == p6); // true
}
