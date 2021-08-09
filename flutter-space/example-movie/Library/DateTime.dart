// import 'dart:core'; // auto introduce

void main() {
  // Create Current Time
  var now = DateTime.now();
  print(now);

  // 通过普通构造函数来创建时间
  var d = DateTime(2021, 8, 9, 3, 30, 41);
  print(d);

  // Create standard time, by parse string create DateTime object
  var d1 = DateTime.parse('2021-08-09 15:04:05');
  print(d1);
  var d2 = DateTime.parse('2021-08-09 15:04:05+0800');
  print(d2);

  print('-------------');

  // 时间增量
  print(now.add(new Duration(hours: 2)));
  print(now.add(new Duration(hours: -3)));

  print('-------------');

  // 时间比较
  print(d1.isBefore(d2)); // d1 是否在 d2 之前
  print(d1.isAfter(d2)); // d1 是否在 d2 之后
  print(d1.isAtSameMomentAs(d2)); // d1 与 d2 是否一致

  // Time difference
  var d3 = new DateTime(2021, 8, 1);
  var d4 = new DateTime(2021, 8, 9);
  var difference = d3.difference(d4);
  // print(difference.inDays, difference.inHours); // [-8, -192]
  print([difference.inDays, difference.inHours]); // d3 和 d4 相差的天数和小时数

  // TimeStamp
  print(now.millisecondsSinceEpoch); // 毫秒
  print(now.microsecondsSinceEpoch); // 微秒

  // Format
  print(now.month.toString().padLeft(2, '0')); // 08

  String timeFormat =
      '${now.year.toString()}-${now.month.toString().padLeft(2, '0')}-${now.day.toString().padLeft(2, '0')} ${now.hour.toString().padLeft(2, '0')}:${now.minute.toString().padLeft(2, '0')}';

  print(timeFormat);
}
