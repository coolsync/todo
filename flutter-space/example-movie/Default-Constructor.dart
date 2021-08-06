// class Point {
//   num? x;
//   num? y;

//   // Define default constructur (普遍构造函数)
//   Point() {
//     print('我是普通构造函数，实例化时，自动调用');
//     this.x = 0;
//     this.y = 0;
//   }
// }

class Point {
  num? x;
  num? y;

  // Define default constructur (普遍构造函数)
  Point(num x, num y) {
    this.x = x;
    this.y = y;
  }
}

void main() {
  // Point p = new Point();
  // print(p.x);

  Point p = new Point(3, 4);
  print(p.y);
}
