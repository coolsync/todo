class BaseClass {}

class Foo<T extends BaseClass> {
  // Implementation goes here...
  String toString() => "Instance of 'Foo<$T>'";
}

class SubClass extends BaseClass {}

void main() {
  var base = Foo<BaseClass>();
  var sub = Foo<SubClass>();
  
  print(base);
  print(sub);
  
  var foo = Foo();
  print(foo); // Instance of 'Foo<SomeBaseClass>' List<String>
  
  // var foo2 = Foo<Object>();
}
