// bool type, 默认值为 null
bool? flage;
bool flage1 = true;

// list
var list = [1, 2, 3];

void main(List<String> args) {
  print(flage); // null
  print(list);
  print(list.length); // 获取  list 容量

  // list add 元素
  list.add(5);
  print(list);

  // define 一个不可改变的list
  var list2 = const [1, 2, 3];
  print(list2[0])
}
