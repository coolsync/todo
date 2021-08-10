void main(List<String> args) {
  // 获取迭代对象 index 为 1的值； 迭代对象与list不同， 它没有 [index] 操作符, 获取和操作
/*  
  Iterable<int> iterable = [1, 2, 3];
  // int value = iterable[1];   // Error
  int value = iterable.elementAt(1); // 索引为1的值
  print(value);
 */

  // for in 读取迭代对象元素
  const iterable = ['Salad', 'Popcorn', 'Toast'];
  for (var elem in iterable) {
    print(elem);
  }
}
