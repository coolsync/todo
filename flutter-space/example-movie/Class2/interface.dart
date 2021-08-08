abstract class Processer {
  String cores;
  arch(String name);
}

abstract class Camera {
  String resolution;
  brand(String name);
}

// implements interface
class Phone implements Processer, Camera {
  @override
  String cores;

  @override
  String resolution;

  Phone(this.cores, this.resolution);

  @override
  arch(String name) {
    print('芯片制程: ' + name);
  }

  @override
  brand(String name) {
    print('品牌: ' + name);
  }
}

void main() {
  var p = new Phone('4 cores', '3000w');
  p.arch('7nm');
  p.brand('徕卡');
}
