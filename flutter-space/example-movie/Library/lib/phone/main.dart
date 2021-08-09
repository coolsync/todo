library phone;

import 'dart:math';

// 与分库建立联系
part 'Camera.dart';
part 'Processor.dart';

void main() {
  Camera c = new Camera();
  c.info();

  Processor p = new Processor();
  p.info();

  print(pi);
}


// Problems encountered (遇到的问题):
// Try including a different part, 
// or changing the name of the library in the part's part-of directive.