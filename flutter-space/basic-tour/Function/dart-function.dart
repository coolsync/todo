var nobleGases = {
  2: 'helium',
  10: 'neon',
  18: 'argon',
};

// bool isNoble(int atomicNumber) {
//   return nobleGases[atomicNumber] != null;
// }

// 简写
bool isNoble(int atomicNumber) => nobleGases[atomicNumber] != null;

// 命名参数
void enableFlags({bool? bold, bool? hidden}) {}

// 使用 required 标识 一个参数 为 必须参数
// const Scrollbar({Key? key, required Widget child}) {}

// 可选的位置参数
String say(String from, String msg, [String? device]) {
  var result = '$from say $msg';
  if (device != null) {
    result = '$result with a $device';
  }
  return result;
}

// 默认参数设定
///  Sets the [bold] and [hidden] flags ...
void enableFlags2({bool bold = false, bool hidden = false}) {}

// bold == true; hidden == false.
// enableFlags(bold: true); // 建议使用 = 来指定默认值

String say2(String from, String msg, [String device = 'carry hot']) {
  var result = '$from say $msg with a $device';
  return result;
}

// List 或 Map 同样也可以作为默认值
void doStuff(
    {List<int> list = const [1, 2, 3],
    Map<String, String> address = const {
      'Bob': 'esten',
      'Paul': 'north',
      'Sam': 'middle',
    }}) {
  print('list: ${list}');
  print('address: ${address}');
}

main(List<String> args) {
  var result = isNoble(2);
  print(result);

  enableFlags(bold: true, hidden: false);

  print(say('Bob', 'Howdy') == 'Bob say Howdy');

  print(say('Bob', 'Howdy', 'smoke signal') ==
      'Bob say Howdy with a smoke signal');

  doStuff()
  ;
}
