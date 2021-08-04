// 测试函数是否相等

void aaa() {} // 顶级 function

class A {
  static void bbb() {} // 静态方法
  void ccc() {} // 实例方法
}

void main() {
  // 创建一个 Function 对象
  Function x;

  // 顶级 func 是否相等
  x = aaa;
  print(aaa == x);

  // Comparing 静态方法
  x = A.bbb;
  print(A.bbb == x);

  // 创建两个实例类
  var ins1 = A(); // 实例方法 1
  var ins2 = A(); // 实例方法 2

  var y = ins1.ccc;
  x = ins1.ccc;

  print(x == y); // 闭包们 引用 同一个实例方法， 所以它们是相等的

  print(ins1.ccc == ins2.ccc); // 闭包们 引用 不是同一个实例方法， 所以它们是为false
}
