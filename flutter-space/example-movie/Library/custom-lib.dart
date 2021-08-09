import 'lib/MyCustom.dart';

void main() {
  var mc = new MyCustom();

  mc.info();

  // access static property
  print(MyCustom.version);
}
