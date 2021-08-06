class Circle {
  final double PI = 3.1415;
  num r;

  // num area() {
  //   return this.PI * this.r * this.r;
  // }

  // 使用 get, area后不能有()
  num get area {
    return this.PI * this.r * this.r;
  }

  // setter
  set setR(value) {
    this.r = value;
  }

  Circle(this.r);
}

void main() {
  var c = new Circle(10);
  // print(c.area());

  print(c.area); // 可以像属性一样访问方法

  c.setR = 20;

  print(c.area);
}
