// 词法作用域（Lexical scope）

bool topLevel = true;

// 嵌套function中变量 指向
void main() {
  bool insideMain = true;

  void myFunction() {
    bool insideFunction = true;

    void nestedFunction() {
      bool insideNestedFunction = true;

      print(topLevel);
      print(insideMain);
      print(insideFunction);
      print(insideNestedFunction);
    }

    nestedFunction();
  }

  myFunction();
}
