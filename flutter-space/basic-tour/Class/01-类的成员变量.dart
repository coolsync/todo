class Point {
  // late int x;
  // late int y;
  int? x;
  int? y;
}

void main() {
  Point p = new Point();

  p.x = 2;
  p.y = 2;

  print(p.x);
}
