enum Color { red, green, blue }

void main() {
  List<Color> colors = Color.values;

  print(colors);

  var aColor = Color.blue;

  switch (aColor) {
    case Color.red:
      print('Red as Rose!');
      break;
    case Color.green:
      print('Green as grass');
      break;
    default:
      print(aColor);
  }
}
