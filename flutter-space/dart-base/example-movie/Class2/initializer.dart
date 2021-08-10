class Rect {
  num height, width;

  // Rect(this.height, this.width);

  // // list params
  // Rect([int height = 2, int width = 10]) {
  //   this.height = height;
  //   this.width = width;
  //   print('${this.height} --- ${this.width}');
  // }

  // Setting params
  // Rect({int height = 2, int width = 10}) {
  //   this.height = height;
  //   this.width = width;
  //   print('${this.height} --- ${this.width}');
  // }

  // 初始化列表
  Rect()
      : height = 4,
        width = 20 {
    print('${this.height} --- ${this.width}');
  }
}

class Point {
  double x, y, z;

  Point(this.x, this.y, this.z);

  // 初始化列表 (重定向构造function)
  Point.twoD(double x, double y) : this(x, y, 0);
}

void main() {
  var r = new Rect();

  var p = new Point(1, 2, 3);
  print(p.z);

  var p2 = new Point.twoD(1, 2);
  print(p2.z);
}
