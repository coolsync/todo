abstract class ObjectCache {
  Object getByKey(String key);
  void setByKey(String key, Object value);
}

abstract class StringCache {
  String getByKey(String key);
  void setByKey(String key, String value);
}

// Generic Interfaces
abstract class Cache<T> {
  T getByKey(String key);
  void setByKey(String key, T value);
}

// implements interface
// 文件缓存
class FileCache<T> implements Cache<T> {
  @override
  T getByKey(String key) {
    return null;
  }

  @override
  void setByKey(String key, T value) {
    print('文件缓冲: key=${key} value=${value}');
  }
}

// Memory 缓存
class MemoryCache<T> implements Cache<T> {
  @override
  T getByKey(String key) {
    return null;
  }

  @override
  void setByKey(String key, T value) {
    print('Memory 缓冲: key=${key} value=${value}');
  }
}

void main() {
  // 文件缓存 - 缓冲字符串
  // var fc = new FileCache<String>();
  // fc.setByKey('foo', 'bar');
  // fc.setByKey('f', 2);    // err

  // 文件缓存 - 缓冲 map
  var fc = new FileCache<Map>();
  // fc.setByKey('foo', 'bar');  // err
  fc.setByKey('index', {'name': 'Bob', 'age': '218'});

  // 内存缓存 - 缓冲字符串
  var mc = new MemoryCache<String>();
  // mc.setByKey('foo', 'bar');

  // 内存缓存 - 缓冲集合
  var mc2 = new MemoryCache<Set>();
  mc2.setByKey('home', {1, 2, 3});
}
