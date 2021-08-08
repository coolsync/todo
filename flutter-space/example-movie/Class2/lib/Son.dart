import 'Father.dart';

class Son extends Father {
  String name = '刘禅';

  // 使用 super 继承 父类 普通构造函数
  // Son(String job) : super(job);

  // 继承命名构造函数
  Son.origin(String job) : super(job);

  @override
  say() {
    super.say(); // 通过super访问父类的内容
    print('我是 刘禅, 我爹是 ${super.name}, 他的工作是 ${super.job}');
  }
}
