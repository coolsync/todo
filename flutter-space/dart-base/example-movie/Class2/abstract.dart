// 1. 通过 abstract 声明
// 2. 可以有抽象方法, 也可以没有抽象方法, 一般来说, 都有抽象方法

abstract class Phone {
  void processer(); // 处理器
  void camera(); // 摄像头
  
  void info() {
    print('我是抽象类普通方法');
  }
}

class Xiaomi extends Phone {
  @override
  void processer() {
    print('骁龙888');
  }

  @override
  void camera() {
    print('三星摄像头');
  }
}

class Oppo extends Phone {
  @override
  void processer() {
    print('三星8780');
  }
  
  @override
  void camera() {
    print('徕卡摄像头');
  }
}

void main() {
  var m = new Xiaomi();
  m.processer();
  m.camera();
  m.info();

  var o = new Oppo();
  o.processer();
  o.camera();
  o.info();
}
