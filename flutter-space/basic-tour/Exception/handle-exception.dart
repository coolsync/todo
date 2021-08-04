void foo(a) {
  if (a is int) {
    throw Exception('hello');
  }
}

void main() {
  try {
    foo(1);
  } on Exception catch (e, s) {
    print("22222==$e==$s");
  } catch (e) {
    print("1111==$e");
  }
}

// 2222==Exception: hello==#0  
