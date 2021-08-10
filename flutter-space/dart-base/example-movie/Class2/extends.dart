import 'lib/Father.dart';
import 'lib/Son.dart';

void main() {
  var f = new Father('治理');
  // var f = new Father.origin('卖草鞋的');
  print(f.name);
  print(f.job);

  // var s = new Son('治理');
  var s = new Son.origin('卖草鞋的');
  print(s.name);
  // print(s._money);  // 子类不能访问父类的 私有内容
  print(s.getMoney);

  s.say();
}
