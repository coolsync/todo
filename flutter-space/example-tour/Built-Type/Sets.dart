// set 是一组特定元素的无序集合

// dart 推断出 halogens 是 Set<String> 类型；
var halogens = {'fluorine', 'chlorine', 'bromine', 'iodine', 'astatine'};

// 创建一个空的Set
var names = <String>{};

// Set<String> names = {};  // 也可以;
// var names = {};   // 会创建map, 不是 set, Map<dynamic, dynamic> 对象

void main() {
  var elements = <String>{};

  // 添加元素到 elemets
  elements.add('fluorine');
  print(elements);

  // 重复的项会被忽略 'fluorine'
  elements.addAll(halogens); // 添加 另一个 set, 也可以是 list
  print(elements); // {fluorine, chlorine, bromine, iodine, astatine}

  print(elements.length);

  // 移除一个元素
  elements.remove('fluorine');
  print(elements);    // {chlorine, bromine, iodine, astatine}

  // 创建 一个编译时的 set 常量
  final constantSet = const {
    'fluorine',
    'chlorine',
    'bromine',
    'iodine',
    'astatine',
  };

  // contentSet.add('未知'); //  Error: Cannot change an unmodifiable(不可更改) set
}
