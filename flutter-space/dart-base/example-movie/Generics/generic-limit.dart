class someBaseClass {
  // ...
}

class Foo<T extends someBaseClass> {
  String toString() => 'Instance of "$T"';
}

// 子类
class Extender extends someBaseClass {
  // ...
}

class Another {
  // ...
}

void main() {
  var f = Foo<someBaseClass>();
  print(f);

  var extender = Foo<Extender>();
  print(extender);
  
  // var f2 = Foo<Another>();  // This is the type variable whose bound isn't conformed to.
  // print(f2);
}
