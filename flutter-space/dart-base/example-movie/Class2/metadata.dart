class Phone {
  // 表示这是旧版本的方法, 会在将来移除
  @deprecated
  active() {
    turnOn();
  }

  turnOn() {
    print('开机');
  }
}

void main() {
  var p = new Phone();

  p.active();

  p.turnOn();
}
