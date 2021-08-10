class Point {
  int? x;
  int? y;

  Point(int x, int y) {
    // constructor function
    this.x = x;
    this.y = y;
  }
}

// 使用常量构造函数, 可在编译时使用
class Point2 {
  static final Point2 origin = const Point2(0, 0);

  final num x, y;
  const Point2(this.x, this.y);
}

void main() {
  var p = new Point(3, 4);
  print(p.x);

  const p2 = Point2(2, 2);
  print(p2.x);
}
