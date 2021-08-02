// 1 字面量创建 string
// ''  ||  ""

// 2 多行 string
var multiLine1 = """多行
string
  写法
""";

var multiLine2 = '''多行
string
  写法
''';

// 3 使用 r 创建原始字符串
var path = r'D:\workspace\code';

// 4. 拼接 string
var plusString = 'hello' + 'something';

// 5. 插值表达式
var name = 'bob';
var str = 'hello, ${name}';
var str2 = 'hello, $name'; // 去掉花括号

// 插值是一个表达式时, 花括号不能省略
var str3 = 'link';
var str4 = 'click ${str3.toUpperCase()}'; // click LINK

main(List<String> args) {
  print(multiLine1);
  print(path);

  // == 操作
  print('good' == 'sam'); // false
}
