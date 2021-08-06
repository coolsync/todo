// 1 created using map literals:
// var gifts = {
//   // Key:    Value
//   'first': 'partridge',
//   'second': 'turtledoves',
//   'fifth': 'golden rings'
// };

var nobleGases = {
  2: 'helium',
  10: 'neon',
  18: 'argon',
};

void main(List<String> args) {
  // 2 using a Map constructor create the same objects :
  var gifts = Map<String, String>();
  gifts['first'] = 'partridge';
  gifts['second'] = 'turtledoves';
  gifts['fifth'] = 'golden rings';
  print(gifts);

  var nobleGases = Map<int, String>();
  nobleGases[2] = 'helium';
  print(nobleGases);

  print('----------');

  gifts['fourth'] =
      'calling birds'; // Add a new key-value pair to an existing map
  print(gifts);

  // 获取一个值的操作
  print(gifts['first']);

  // 检索 一个值是否为 null
  print(gifts['sixth']);

  // 使用 .length 可以获取 Map 中键值对的数量：
  print(gifts.length);

  // 在 字面量后面 使用 const keyword 创建一个 Map 编译时常量：
  var constantMap = const {
    2: 'helium',
    10: 'neon',
    18: 'argon',
  };

  // constantMap[2] = 'HELIUM'; //  Cannot set value in unmodifiable(不可改变) Map

}
