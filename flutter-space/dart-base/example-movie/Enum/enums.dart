import 'dart:math';

enum Color { red, green, blue }

void main() {
  // index
  print(Color.green.index);

  // values
  print(Color.values); // [Color.red, Color.green, Color.blue]

  // list values
  List<Color> colors = Color.values;
  print(colors);

  // for enum element
  colors.forEach((element) {
    print('value: ${element}  index: ${element.index}');
  });
}
