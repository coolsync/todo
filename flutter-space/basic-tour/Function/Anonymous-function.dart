/* 
([[类型] 参数[, …]]) {
  函数体;
};
*/

void main(List<String> args) {
  const list = ['apples', 'bananas', 'oranges'];

  list.forEach((item) {
    print('${list.indexOf(item)}: ${item}');
  });

  // 简写： 只有一行时， 可以使用 箭头
  list.forEach((item) => print('${list.indexOf(item)}: ${item}'));
}


