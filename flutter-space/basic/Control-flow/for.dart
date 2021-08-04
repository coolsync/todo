void main(List<String> args) {
  // 标准写法
  // var message = StringBuffer('Dart is fun');

  // for (var i = 0; i < 3; i++) {
  //   message.write('!');   // 在其末尾追加
  // }

  // print(message);    // Dart is fun!!!

  // for 循环中闭包 自动捕获 for 索引值
  var callbacks = [];
  for (var i = 0; i < 2; i++) {
    callbacks.add(() => print(i));
  }
  print(callbacks); // [Closure: () => void, Closure: () => void]

  callbacks.forEach((item) => item());

  // 遍历对象是一个可迭代的对象（set and list）, 并且不需要它的索引值， 可以 for in

  // 也可以使用 forEeach; void forEach(void Function(int) f)
  var collection = [1, 2, 3];
  // collection.forEach((element) {
  //   print(element);
  // });

  collection.forEach(print);
}
