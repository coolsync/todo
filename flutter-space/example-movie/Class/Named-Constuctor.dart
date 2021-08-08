const double xOrigin = 0;
const double yOrigin = 0;

class Point {
  num x, y;

  Point(this.x, this.y); // default constructor

  // 命名构造函数 -->> 作用：提高 构造function 清晰度
  Point.origin()
      : x = xOrigin,
        y = yOrigin;

  // 命名构造函数
  Point.fromJson({x: 0, y: 0}) {
    this.x = x;
    this.y = y;
  }
}

void main() {
  // 坐标的默认位置
  Point p1 = new Point.origin();
  print(p1.x);

  // 设置坐标位置
  Point p2 = new Point.fromJson(x: 6, y: 6);  
  print(p2.x);
}
