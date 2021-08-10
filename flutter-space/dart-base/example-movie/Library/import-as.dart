import 'lib/common.dart';
import 'lib/function.dart' as func; // as prefix: Introduce conflict handling

void main() {
  f1();
  func.f1();
}


// Problems encountered (遇到的问题):
// Try using 'as prefix' for one of the import directives,
// or hiding the name from all but one of the imports.
