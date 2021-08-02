# A tour of the Dart language

This page shows you how to use each major Dart feature, from variables and operators to classes and libraries, with the assumption that you already know how to program in another language. For a briefer, less complete introduction to the language, see the [language samples page](https://dart.dev/samples).

To learn more about Dart’s core libraries, see the [library tour](https://dart.dev/guides/libraries/library-tour). Whenever you want more details about a language feature, consult the [Dart language specification](https://dart.dev/guides/language/spec).

 **Note:** You can play with most of Dart’s language features using DartPad ([learn more](https://dart.dev/tools/dartpad)). **[Open DartPad.](https://dartpad.dev/)**

This page uses embedded DartPads to display some of the examples. If you see empty boxes instead of DartPads, go to the [DartPad troubleshooting page](https://dart.dev/tools/dartpad/troubleshoot).

## A basic Dart program

The following code uses many of Dart’s most basic features:

```dart
// Define a function.
void printInteger(int aNumber) {
  print('The number is $aNumber.'); // Print to console.
}

// This is where the app starts executing.
void main() {
  var number = 42; // Declare and initialize a variable.
  printInteger(number); // Call a function.
}
```

Here’s what this program uses that applies to all (or almost all) Dart apps:

- `// *This is a comment.*`

  A single-line comment. Dart also supports multi-line and document comments. For details, see [Comments](https://dart.dev/guides/language/language-tour#comments).

- `void`

  A special type that indicates a value that’s never used. Functions like `printInteger()` and `main()` that don’t explicitly return a value have the `void` return type.

- `int`

  Another type, indicating an integer. Some additional [built-in types](https://dart.dev/guides/language/language-tour#built-in-types) are `String`, `List`, and `bool`.

- `42`

  A number literal. Number literals are a kind of compile-time constant.

- `print()`

  A handy way to display output.

- `'...'` (or `"..."`)

  A string literal.

- `$*variableName*` (or `${*expression*}`)

  String interpolation: including a variable or expression’s string equivalent inside of a string literal. For more information, see [Strings](https://dart.dev/guides/language/language-tour#strings).

- `main()`

  The special, *required*, top-level function where app execution starts. For more information, see [The main() function](https://dart.dev/guides/language/language-tour#the-main-function).

- `var`

  A way to declare a variable without specifying its type. The type of this variable (`int`) is determined by its initial value (`42`).

 **Note:** This site’s code follows the conventions in the [Dart style guide](https://dart.dev/guides/language/effective-dart/style).

## Important concepts

As you learn about the Dart language, keep these facts and concepts in mind:

- Everything you can place in a variable is an *object*, and every object is an instance of a *class*. Even numbers, functions, and `null` are objects. With the exception of `null` (if you enable [sound null safety](https://dart.dev/null-safety)), all objects inherit from the [`Object`](https://api.dart.dev/stable/dart-core/Object-class.html) class.

   **Version note:** [Null safety](https://dart.dev/null-safety) was introduced in Dart 2.12. Using null safety requires a [language version](https://dart.dev/guides/language/evolution#language-versioning) of at least 2.12.

- Although Dart is strongly typed, type annotations are optional because Dart can infer types. In the code above, `number` is inferred to be of type `int`.

- If you enable [null safety](https://dart.dev/null-safety), variables can’t contain `null` unless you say they can. You can make a variable nullable by putting a question mark (`?`) at the end of its type. For example, a variable of type `int?` might be an integer, or it might be `null`. If you *know* that an expression never evaluates to `null` but Dart disagrees, you can add `!` to assert that it isn’t null (and to throw an exception if it is). An example: `int x = nullableButNotNullInt!`

- When you want to explicitly say that any type is allowed, use the type `Object?` (if you’ve [enabled null safety](https://dart.dev/null-safety#enable-null-safety)), `Object`, or — if you must defer type checking until runtime — the [special type `dynamic`](https://dart.dev/guides/language/effective-dart/design#avoid-using-dynamic-unless-you-want-to-disable-static-checking).

- Dart supports generic types, like `List<int>` (a list of integers) or `List<Object>` (a list of objects of any type).

- Dart supports top-level functions (such as `main()`), as well as functions tied to a class or object (*static* and *instance methods*, respectively). You can also create functions within functions (*nested* or *local functions*).

- Similarly, Dart supports top-level *variables*, as well as variables tied to a class or object (static and instance variables). Instance variables are sometimes known as *fields* or *properties*.

- Unlike Java, Dart doesn’t have the keywords `public`, `protected`, and `private`. If an identifier starts with an underscore (`_`), it’s private to its library. For details, see [Libraries and visibility](https://dart.dev/guides/language/language-tour#libraries-and-visibility).

- *Identifiers* can start with a letter or underscore (`_`), followed by any combination of those characters plus digits.

- Dart has both *expressions* (which have runtime values) and *statements* (which don’t). For example, the [conditional expression](https://dart.dev/guides/language/language-tour#conditional-expressions) `condition ? expr1 : expr2` has a value of `expr1` or `expr2`. Compare that to an [if-else statement](https://dart.dev/guides/language/language-tour#if-and-else), which has no value. A statement often contains one or more expressions, but an expression can’t directly contain a statement.

- Dart tools can report two kinds of problems: *warnings* and *errors*. Warnings are just indications that your code might not work, but they don’t prevent your program from executing. Errors can be either compile-time or run-time. A compile-time error prevents the code from executing at all; a run-time error results in an [exception](https://dart.dev/guides/language/language-tour#exceptions) being raised while the code executes.

## Keywords

The following table lists the words that the Dart language treats specially.

| [abstract](https://dart.dev/guides/language/language-tour#abstract-classes) 2 | [else](https://dart.dev/guides/language/language-tour#if-and-else) | [import](https://dart.dev/guides/language/language-tour#using-libraries) 2 | [show](https://dart.dev/guides/language/language-tour#importing-only-part-of-a-library) 1 |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| [as](https://dart.dev/guides/language/language-tour#type-test-operators) 2 | [enum](https://dart.dev/guides/language/language-tour#enumerated-types) | [in](https://dart.dev/guides/language/language-tour#for-loops) | [static](https://dart.dev/guides/language/language-tour#class-variables-and-methods) 2 |
| [assert](https://dart.dev/guides/language/language-tour#assert) | [export](https://dart.dev/guides/libraries/create-library-packages) 2 | [interface](https://stackoverflow.com/questions/28595501/was-the-interface-keyword-removed-from-dart) 2 | [super](https://dart.dev/guides/language/language-tour#extending-a-class) |
| [async](https://dart.dev/guides/language/language-tour#asynchrony-support) 1 | [extends](https://dart.dev/guides/language/language-tour#extending-a-class) | [is](https://dart.dev/guides/language/language-tour#type-test-operators) | [switch](https://dart.dev/guides/language/language-tour#switch-and-case) |
| [await](https://dart.dev/guides/language/language-tour#asynchrony-support) 3 | [extension](https://dart.dev/guides/language/language-tour#extension-methods) 2 | [late](https://dart.dev/guides/language/language-tour#late-variables) 2 | [sync](https://dart.dev/guides/language/language-tour#generators) 1 |
| [break](https://dart.dev/guides/language/language-tour#break-and-continue) | [external](https://stackoverflow.com/questions/24929659/what-does-external-mean-in-dart) 2 | [library](https://dart.dev/guides/language/language-tour#libraries-and-visibility) 2 | [this](https://dart.dev/guides/language/language-tour#constructors) |
| [case](https://dart.dev/guides/language/language-tour#switch-and-case) | [factory](https://dart.dev/guides/language/language-tour#factory-constructors) 2 | [mixin](https://dart.dev/guides/language/language-tour#adding-features-to-a-class-mixins) 2 | [throw](https://dart.dev/guides/language/language-tour#throw) |
| [catch](https://dart.dev/guides/language/language-tour#catch) | [false](https://dart.dev/guides/language/language-tour#booleans) | [new](https://dart.dev/guides/language/language-tour#using-constructors) | [true](https://dart.dev/guides/language/language-tour#booleans) |
| [class](https://dart.dev/guides/language/language-tour#instance-variables) | [final](https://dart.dev/guides/language/language-tour#final-and-const) | [null](https://dart.dev/guides/language/language-tour#default-value) | [try](https://dart.dev/guides/language/language-tour#catch)  |
| [const](https://dart.dev/guides/language/language-tour#final-and-const) | [finally](https://dart.dev/guides/language/language-tour#finally) | [on](https://dart.dev/guides/language/language-tour#catch) 1 | [typedef](https://dart.dev/guides/language/language-tour#typedefs) 2 |
| [continue](https://dart.dev/guides/language/language-tour#break-and-continue) | [for](https://dart.dev/guides/language/language-tour#for-loops) | [operator](https://dart.dev/guides/language/language-tour#_operators) 2 | [var](https://dart.dev/guides/language/language-tour#variables) |
| [covariant](https://dart.dev/guides/language/sound-problems#the-covariant-keyword) 2 | [Function](https://dart.dev/guides/language/language-tour#functions) 2 | [part](https://dart.dev/guides/libraries/create-library-packages#organizing-a-library-package) 2 | [void](https://dart.dev/guides/language/language-tour#built-in-types) |
| [default](https://dart.dev/guides/language/language-tour#switch-and-case) | [get](https://dart.dev/guides/language/language-tour#getters-and-setters) 2 | [required](https://dart.dev/guides/language/language-tour#named-parameters) 2 | [while](https://dart.dev/guides/language/language-tour#while-and-do-while) |
| [deferred](https://dart.dev/guides/language/language-tour#lazily-loading-a-library) 2 | [hide](https://dart.dev/guides/language/language-tour#importing-only-part-of-a-library) 1 | [rethrow](https://dart.dev/guides/language/language-tour#catch) | [with](https://dart.dev/guides/language/language-tour#adding-features-to-a-class-mixins) |
| [do](https://dart.dev/guides/language/language-tour#while-and-do-while) | [if](https://dart.dev/guides/language/language-tour#if-and-else) | [return](https://dart.dev/guides/language/language-tour#functions) | [yield](https://dart.dev/guides/language/language-tour#generators) 3 |
| [dynamic](https://dart.dev/guides/language/language-tour#important-concepts) 2 | [implements](https://dart.dev/guides/language/language-tour#implicit-interfaces) 2 | [set](https://dart.dev/guides/language/language-tour#getters-and-setters) 2 |                                                              |

Avoid using these words as identifiers. However, if necessary, the keywords marked with superscripts can be identifiers:

- Words with the superscript **1** are **contextual keywords**, which have meaning only in specific places. They’re valid identifiers everywhere.
- Words with the superscript **2** are **built-in identifiers**. To simplify the task of porting JavaScript code to Dart, these keywords are valid identifiers in most places, but they can’t be used as class or type names, or as import prefixes.
- Words with the superscript **3** are limited reserved words related to [asynchrony support](https://dart.dev/guides/language/language-tour#asynchrony-support). You can’t use `await` or `yield` as an identifier in any function body marked with `async`, `async*`, or `sync*`.

All other words in the table are **reserved words**, which can’t be identifiers.

## Variables

Here’s an example of creating a variable and initializing it:

```dart
var name = 'Bob';
```

Variables store references. The variable called `name` contains a reference to a `String` object with a value of “Bob”.

The type of the `name` variable is inferred to be `String`, but you can change that type by specifying it. If an object isn’t restricted to a single type, specify the `Object` type (or `dynamic` if necessary).

```dart
Object name = 'Bob';
```

Another option is to explicitly declare the type that would be inferred:

```dart
String name = 'Bob';
```

 **Note:** This page follows the [style guide recommendation](https://dart.dev/guides/language/effective-dart/design#types) of using `var`, rather than type annotations, for local variables.

### Default value

Uninitialized variables that have a nullable type have an initial value of `null`. (If you haven’t opted into [null safety](https://dart.dev/null-safety), then every variable has a nullable type.) Even variables with numeric types are initially null, because numbers—like everything else in Dart—are objects.

```dart
int? lineCount;
assert(lineCount == null);
```

 **Note:** Production code ignores the `assert()` call. During development, on the other hand, `assert(*condition*)` throws an exception if *condition* is false. For details, see [Assert](https://dart.dev/guides/language/language-tour#assert).

If you enable null safety, then you must initialize the values of non-nullable variables before you use them:

```dart
int lineCount = 0;
```

You don’t have to initialize a local variable where it’s declared, but you do need to assign it a value before it’s used. For example, the following code is valid because Dart can detect that `lineCount` is non-null by the time it’s passed to `print()`:

```dart
int lineCount;

if (weLikeToCount) {
  lineCount = countLines();
} else {
  lineCount = 0;
}

print(lineCount);
```

### Late variables

Dart 2.12 added the `late` modifier, which has two use cases:

- Declaring a non-nullable variable that’s initialized after its declaration.
- Lazily initializing a variable.

Often Dart’s control flow analysis can detect when a non-nullable variable is set to a non-null value before it’s used, but sometimes analysis fails. Two common cases are top-level variables and instance variables: Dart often can’t determine whether they’re set, so it doesn’t try.

If you’re sure that a variable is set before it’s used, but Dart disagrees, you can fix the error by marking the variable as `late`:

```dart
late String description;

void main() {
  description = 'Feijoada!';
  print(description);
}
```

 If you fail to initialize a `late` variable, a runtime error occurs when the variable is used.

When you mark a variable as `late` but initialize it at its declaration, then the initializer runs the first time the variable is used. This lazy initialization is handy in a couple of cases:

- The variable might not be needed, and initializing it is costly.
- You’re initializing an instance variable, and its initializer needs access to `this`.

In the following example, if the `temperature` variable is never used, then the expensive `_readThermometer()` function is never called:

```dart
// This is the program's only call to _readThermometer().
late String temperature = _readThermometer(); // Lazily initialized.
```

### Final and const

If you never intend to change a variable, use `final` or `const`, either instead of `var` or in addition to a type. A final variable can be set only once; a const variable is a compile-time constant. (Const variables are implicitly final.) A final top-level or class variable is initialized the first time it’s used.

 **Note:** [Instance variables](https://dart.dev/guides/language/language-tour#instance-variables) can be `final` but not `const`.

Here’s an example of creating and setting a `final` variable:

```dart
final name = 'Bob'; // Without a type annotation
final String nickname = 'Bobby';
```

You can’t change the value of a `final` variable:

```dart
name = 'Alice'; // Error: a final variable can only be set once.
```

Use `const` for variables that you want to be **compile-time constants**. If the const variable is at the class level, mark it `static const`. Where you declare the variable, set the value to a compile-time constant such as a number or string literal, a const variable, or the result of an arithmetic operation on constant numbers:

```dart
const bar = 1000000; // Unit of pressure (dynes/cm2)
const double atm = 1.01325 * bar; // Standard atmosphere
```

The `const` keyword isn’t just for declaring constant variables. You can also use it to create constant *values*, as well as to declare constructors that *create* constant values. Any variable can have a constant value.

```dart
var foo = const [];
final bar = const [];
const baz = []; // Equivalent to `const []`
```

You can omit `const` from the initializing expression of a `const` declaration, like for `baz` above. For details, see [DON’T use const redundantly](https://dart.dev/guides/language/effective-dart/usage#dont-use-const-redundantly).

You can change the value of a non-final, non-const variable, even if it used to have a `const` value:

```dart
foo = [1, 2, 3]; // Was const []
```

You can’t change the value of a `const` variable:

```dart
baz = [42]; // Error: Constant variables can't be assigned a value.
```

You can define constants that use [type checks and casts](https://dart.dev/guides/language/language-tour#type-test-operators) (`is` and `as`), [collection `if`](https://dart.dev/guides/language/language-tour#collection-operators), and [spread operators](https://dart.dev/guides/language/language-tour#spread-operator) (`...` and `...?`):

```dart
const Object i = 3; // Where i is a const Object with an int value...
const list = [i as int]; // Use a typecast.
const map = {if (i is int) i: 'int'}; // Use is and collection if.
const set = {if (list is List<int>) ...list}; // ...and a spread.
```

 **Note:** Although a `final` object cannot be modified, its fields can be changed. In comparison, a `const` object and its fields cannot be changed: they’re *immutable*.

For more information on using `const` to create constant values, see [Lists](https://dart.dev/guides/language/language-tour#lists), [Maps](https://dart.dev/guides/language/language-tour#maps), and [Classes](https://dart.dev/guides/language/language-tour#classes).

## Built-in types

The Dart language has special support for the following:

- [Numbers](https://dart.dev/guides/language/language-tour#numbers) (`int`, `double`)
- [Strings](https://dart.dev/guides/language/language-tour#strings) (`String`)
- [Booleans](https://dart.dev/guides/language/language-tour#booleans) (`bool`)
- [Lists](https://dart.dev/guides/language/language-tour#lists) (`List`, also known as *arrays*)
- [Sets](https://dart.dev/guides/language/language-tour#sets) (`Set`)
- [Maps](https://dart.dev/guides/language/language-tour#maps) (`Map`)
- [Runes](https://dart.dev/guides/language/language-tour#characters) (`Runes`; often replaced by the `characters` API)
- [Symbols](https://dart.dev/guides/language/language-tour#symbols) (`Symbol`)
- The value `null` (`Null`)

This support includes the ability to create objects using literals. For example, `'this is a string'` is a string literal, and `true` is a boolean literal.

Because every variable in Dart refers to an object—an instance of a *class*—you can usually use *constructors* to initialize variables. Some of the built-in types have their own constructors. For example, you can use the `Map()` constructor to create a map.

Some other types also have special roles in the Dart language:

- `Object`: The superclass of all Dart classes except `Null`.
- `Future` and `Stream`: Used in [asynchrony support](https://dart.dev/guides/language/language-tour#asynchrony-support).
- `Iterable`: Used in [for-in loops](https://dart.dev/guides/libraries/library-tour#iteration) and in synchronous [generator functions](https://dart.dev/guides/language/language-tour#generator).
- `Never`: Indicates that an expression can never successfully finish evaluating. Most often used for functions that always throw an exception.
- `dynamic`: Indicates that you want to disable static checking. Usually you should use `Object` or `Object?` instead.
- `void`: Indicates that a value is never used. Often used as a return type.

The `Object`, `Object?`, `Null`, and `Never` classes have special roles in the class hierarchy, as described in the [top-and-bottom](https://dart.dev/null-safety/understanding-null-safety#top-and-bottom) section of [Understanding null safety](https://dart.dev/null-safety/understanding-null-safety).

### Numbers

Dart numbers come in two flavors:

- [`int`](https://api.dart.dev/stable/dart-core/int-class.html)

  Integer values no larger than 64 bits, [depending on the platform](https://dart.dev/guides/language/numbers). On native platforms, values can be from -263 to 263 - 1. On the web, integer values are represented as JavaScript numbers (64-bit floating-point values with no fractional part) and can be from -253 to 253 - 1.

- [`double`](https://api.dart.dev/stable/dart-core/double-class.html)

  64-bit (double-precision) floating-point numbers, as specified by the IEEE 754 standard.

Both `int` and `double` are subtypes of [`num`](https://api.dart.dev/stable/dart-core/num-class.html). The num type includes basic operators such as +, -, /, and *, and is also where you’ll find `abs()`,` ceil()`, and `floor()`, among other methods. (Bitwise operators, such as >>, are defined in the `int` class.) If num and its subtypes don’t have what you’re looking for, the [dart:math](https://api.dart.dev/stable/dart-math) library might.

Integers are numbers without a decimal point. Here are some examples of defining integer literals:

```dart
var x = 1;
var hex = 0xDEADBEEF;
var exponent = 8e5;
```

If a number includes a decimal, it is a double. Here are some examples of defining double literals:

```dart
var y = 1.1;
var exponents = 1.42e5;
```

You can also declare a variable as a num. If you do this, the variable can have both integer and double values.

```dart
num x = 1; // x can have both int and double values
x += 2.5;
```

Integer literals are automatically converted to doubles when necessary:

```dart
double z = 1; // Equivalent to double z = 1.0.
```

Here’s how you turn a string into a number, or vice versa:

```dart
// String -> int
var one = int.parse('1');
assert(one == 1);

// String -> double
var onePointOne = double.parse('1.1');
assert(onePointOne == 1.1);

// int -> String
String oneAsString = 1.toString();
assert(oneAsString == '1');

// double -> String
String piAsString = 3.14159.toStringAsFixed(2);
assert(piAsString == '3.14');
```

The int type specifies the traditional bitwise shift (<<, >>), AND (&), and OR (|) operators. For example:

```dart
assert((3 << 1) == 6); // 0011 << 1 == 0110
assert((3 >> 1) == 1); // 0011 >> 1 == 0001
assert((3 | 4) == 7); // 0011 | 0100 == 0111
```

Literal numbers are compile-time constants. Many arithmetic expressions are also compile-time constants, as long as their operands are compile-time constants that evaluate to numbers.

```dart
const msPerSecond = 1000;
const secondsUntilRetry = 5;
const msUntilRetry = secondsUntilRetry * msPerSecond;
```

For more information, see [Numbers in Dart](https://dart.dev/guides/language/numbers).

### Strings

A Dart string (`String` object) holds a sequence of UTF-16 code units. You can use either single or double quotes to create a string:

```dart
var s1 = 'Single quotes work well for string literals.';
var s2 = "Double quotes work just as well.";
var s3 = 'It\'s easy to escape the string delimiter.';
var s4 = "It's even easier to use the other delimiter.";
```

You can put the value of an expression inside a string by using `${`*`expression`*`}`. If the expression is an identifier, you can skip the {}. To get the string corresponding to an object, Dart calls the object’s `toString()` method.

```dart
var s = 'string interpolation';

assert('Dart has $s, which is very handy.' ==
    'Dart has string interpolation, '
        'which is very handy.');
assert('That deserves all caps. '
        '${s.toUpperCase()} is very handy!' ==
    'That deserves all caps. '
        'STRING INTERPOLATION is very handy!');
```

 **Note:** The `==` operator tests whether two objects are equivalent. Two strings are equivalent if they contain the same sequence of code units.

You can concatenate strings using adjacent string literals or the `+` operator:

```dart
var s1 = 'String '
    'concatenation'
    " works even over line breaks.";
assert(s1 ==
    'String concatenation works even over '
        'line breaks.');

var s2 = 'The + operator ' + 'works, as well.';
assert(s2 == 'The + operator works, as well.');
```

Another way to create a multi-line string: use a triple quote with either single or double quotation marks:

```dart
var s1 = '''
You can create
multi-line strings like this one.
''';

var s2 = """This is also a
multi-line string.""";
```

You can create a “raw” string by prefixing it with `r`:

```dart
var s = r'In a raw string, not even \n gets special treatment.';
```

See [Runes and grapheme clusters](https://dart.dev/guides/language/language-tour#characters) for details on how to express Unicode characters in a string.

Literal strings are compile-time constants, as long as any interpolated expression is a compile-time constant that evaluates to null or a numeric, string, or boolean value.

```dart
// These work in a const string.
const aConstNum = 0;
const aConstBool = true;
const aConstString = 'a constant string';

// These do NOT work in a const string.
var aNum = 0;
var aBool = true;
var aString = 'a string';
const aConstList = [1, 2, 3];

const validConstString = '$aConstNum $aConstBool $aConstString';
// const invalidConstString = '$aNum $aBool $aString $aConstList';
```

For more information on using strings, see [Strings and regular expressions](https://dart.dev/guides/libraries/library-tour#strings-and-regular-expressions).

### Booleans

To represent boolean values, Dart has a type named `bool`. Only two objects have type bool: the boolean literals `true` and `false`, which are both compile-time constants.

Dart’s type safety means that you can’t use code like `if (*nonbooleanValue*)` or `assert (*nonbooleanValue*)`. Instead, explicitly check for values, like this:

```dart
// Check for an empty string.
var fullName = '';
assert(fullName.isEmpty);

// Check for zero.
var hitPoints = 0;
assert(hitPoints <= 0);

// Check for null.
var unicorn;
assert(unicorn == null);

// Check for NaN.
var iMeantToDoThis = 0 / 0;
assert(iMeantToDoThis.isNaN);
```

### Lists

Perhaps the most common collection in nearly every programming language is the *array*, or ordered group of objects. In Dart, arrays are [`List`](https://api.dart.dev/stable/dart-core/List-class.html) objects, so most people just call them *lists*.

Dart list literals look like JavaScript array literals. Here’s a simple Dart list:

```dart
var list = [1, 2, 3];
```

 **Note:** Dart infers that `list` has type `List<int>`. If you try to add non-integer objects to this list, the analyzer or runtime raises an error. For more information, read about [type inference.](https://dart.dev/guides/language/type-system#type-inference)

You can add a comma after the last item in a Dart collection literal. This *trailing comma* doesn’t affect the collection, but it can help prevent copy-paste errors.

```dart
var list = [
  'Car',
  'Boat',
  'Plane',
];
```

Lists use zero-based indexing, where 0 is the index of the first value and `list.length - 1` is the index of the last value. You can get a list’s length and refer to list values just as you would in JavaScript:

```dart
var list = [1, 2, 3];
assert(list.length == 3);
assert(list[1] == 2);

list[1] = 1;
assert(list[1] == 1);
```

To create a list that’s a compile-time constant, add `const` before the list literal:

```dart
var constantList = const [1, 2, 3];
// constantList[1] = 1; // This line will cause an error.
```

Dart 2.3 introduced the **spread operator** (`...`) and the **null-aware spread operator** (`...?`), which provide a concise way to insert multiple values into a collection.

For example, you can use the spread operator (`...`) to insert all the values of a list into another list:

```dart
var list = [1, 2, 3];
var list2 = [0, ...list];
assert(list2.length == 4);
```

If the expression to the right of the spread operator might be null, you can avoid exceptions by using a null-aware spread operator (`...?`):

```dart
var list;
var list2 = [0, ...?list];
assert(list2.length == 1);
```

For more details and examples of using the spread operator, see the [spread operator proposal.](https://github.com/dart-lang/language/blob/master/accepted/2.3/spread-collections/feature-specification.md)

Dart also offers **collection if** and **collection for**, which you can use to build collections using conditionals (`if`) and repetition (`for`).

Here’s an example of using **collection if** to create a list with three or four items in it:

```dart
var nav = [
  'Home',
  'Furniture',
  'Plants',
  if (promoActive) 'Outlet'
];
```

Here’s an example of using **collection for** to manipulate the items of a list before adding them to another list:

```dart
var listOfInts = [1, 2, 3];
var listOfStrings = [
  '#0',
  for (var i in listOfInts) '#$i'
];
assert(listOfStrings[1] == '#1');
```

For more details and examples of using collection `if` and `for`, see the [control flow collections proposal.](https://github.com/dart-lang/language/blob/master/accepted/2.3/control-flow-collections/feature-specification.md)

The List type has many handy methods for manipulating lists. For more information about lists, see [Generics](https://dart.dev/guides/language/language-tour#generics) and [Collections](https://dart.dev/guides/libraries/library-tour#collections).

### Sets

A set in Dart is an unordered collection of unique items. Dart support for sets is provided by set literals and the [`Set`](https://api.dart.dev/stable/dart-core/Set-class.html) type.

Here is a simple Dart set, created using a set literal:

```dart
var halogens = {'fluorine', 'chlorine', 'bromine', 'iodine', 'astatine'};
```

 **Note:** Dart infers that `halogens` has the type `Set<String>`. If you try to add the wrong type of value to the set, the analyzer or runtime raises an error. For more information, read about [type inference.](https://dart.dev/guides/language/type-system#type-inference)

To create an empty set, use `{}` preceded by a type argument, or assign `{}` to a variable of type `Set`:

```dart
var names = <String>{};
// Set<String> names = {}; // This works, too.
// var names = {}; // Creates a map, not a set.
```

 **Set or map?** The syntax for map literals is similar to that for set literals. Because map literals came first, `{}` defaults to the `Map` type. If you forget the type annotation on `{}` or the variable it’s assigned to, then Dart creates an object of type `Map<dynamic, dynamic>`.

Add items to an existing set using the `add()` or `addAll()` methods:

```dart
var elements = <String>{};
elements.add('fluorine');
elements.addAll(halogens);
```

Use `.length` to get the number of items in the set:

```dart
var elements = <String>{};
elements.add('fluorine');
elements.addAll(halogens);
assert(elements.length == 5);
```

To create a set that’s a compile-time constant, add `const` before the set literal:

```dart
final constantSet = const {
  'fluorine',
  'chlorine',
  'bromine',
  'iodine',
  'astatine',
};
// constantSet.add('helium'); // This line will cause an error.
```

Sets support spread operators (`...` and `...?`) and collection `if` and `for`, just like lists do. For more information, see the [list spread operator](https://dart.dev/guides/language/language-tour#spread-operator) and [list collection operator](https://dart.dev/guides/language/language-tour#collection-operators) discussions.

For more information about sets, see [Generics](https://dart.dev/guides/language/language-tour#generics) and [Sets](https://dart.dev/guides/libraries/library-tour#sets).

### Maps

In general, a map is an object that associates keys and values. Both keys and values can be any type of object. Each *key* occurs only once, but you can use the same *value* multiple times. Dart support for maps is provided by map literals and the [`Map`](https://api.dart.dev/stable/dart-core/Map-class.html) type.

Here are a couple of simple Dart maps, created using map literals:

```dart
var gifts = {
  // Key:    Value
  'first': 'partridge',
  'second': 'turtledoves',
  'fifth': 'golden rings'
};

var nobleGases = {
  2: 'helium',
  10: 'neon',
  18: 'argon',
};
```

 **Note:** Dart infers that `gifts` has the type `Map<String, String>` and `nobleGases` has the type `Map<int, String>`. If you try to add the wrong type of value to either map, the analyzer or runtime raises an error. For more information, read about [type inference.](https://dart.dev/guides/language/type-system#type-inference)

You can create the same objects using a Map constructor:

```dart
var gifts = Map<String, String>();
gifts['first'] = 'partridge';
gifts['second'] = 'turtledoves';
gifts['fifth'] = 'golden rings';

var nobleGases = Map<int, String>();
nobleGases[2] = 'helium';
nobleGases[10] = 'neon';
nobleGases[18] = 'argon';
```

 **Note:** If you come from a language like C# or Java, you might expect to see `new Map()` instead of just `Map()`. In Dart, the `new` keyword is optional. For details, see [Using constructors](https://dart.dev/guides/language/language-tour#using-constructors).

Add a new key-value pair to an existing map just as you would in JavaScript:

```dart
var gifts = {'first': 'partridge'};
gifts['fourth'] = 'calling birds'; // Add a key-value pair
```

Retrieve a value from a map the same way you would in JavaScript:

```dart
var gifts = {'first': 'partridge'};
assert(gifts['first'] == 'partridge');
```

If you look for a key that isn’t in a map, you get a null in return:

```dart
var gifts = {'first': 'partridge'};
assert(gifts['fifth'] == null);
```

Use `.length` to get the number of key-value pairs in the map:

```dart
var gifts = {'first': 'partridge'};
gifts['fourth'] = 'calling birds';
assert(gifts.length == 2);
```

To create a map that’s a compile-time constant, add `const` before the map literal:

```dart
final constantMap = const {
  2: 'helium',
  10: 'neon',
  18: 'argon',
};

// constantMap[2] = 'Helium'; // This line will cause an error.
```

Maps support spread operators (`...` and `...?`) and collection `if` and `for`, just like lists do. For details and examples, see the [spread operator proposal](https://github.com/dart-lang/language/blob/master/accepted/2.3/spread-collections/feature-specification.md) and the [control flow collections proposal.](https://github.com/dart-lang/language/blob/master/accepted/2.3/control-flow-collections/feature-specification.md)

For more information about maps, see the [generics](https://dart.dev/guides/language/language-tour#generics) section and the library tour’s coverage of the [`Maps` API](https://dart.dev/guides/libraries/library-tour#maps).



### Runes and grapheme clusters

In Dart, [runes](https://api.dart.dev/stable/dart-core/Runes-class.html) expose the Unicode code points of a string. You can use the [characters package](https://pub.dev/packages/characters) to view or manipulate user-perceived characters, also known as [Unicode (extended) grapheme clusters.](https://unicode.org/reports/tr29/#Grapheme_Cluster_Boundaries)

Unicode defines a unique numeric value for each letter, digit, and symbol used in all of the world’s writing systems. Because a Dart string is a sequence of UTF-16 code units, expressing Unicode code points within a string requires special syntax. The usual way to express a Unicode code point is `\uXXXX`, where XXXX is a 4-digit hexadecimal value. For example, the heart character (♥) is `\u2665`. To specify more or less than 4 hex digits, place the value in curly brackets. For example, the laughing emoji (😆) is `\u{1f606}`.

If you need to read or write individual Unicode characters, use the `characters` getter defined on String by the characters package. The returned [`Characters`](https://pub.dev/documentation/characters/latest/characters/Characters-class.html) object is the string as a sequence of grapheme clusters. Here’s an example of using the characters API:

```
import 'package:characters/characters.dart';
...
var hi = 'Hi 🇩🇰';
print(hi);
print('The end of the string: ${hi.substring(hi.length - 1)}');
print('The last character: ${hi.characters.last}\n');
```

The output, depending on your environment, looks something like this:

```
$ dart bin/main.dart
Hi 🇩🇰
The end of the string: ???
The last character: 🇩🇰
```

For details on using the characters package to manipulate strings, see the [example](https://pub.dev/packages/characters/example) and [API reference](https://pub.dev/documentation/characters) for the characters package.

### Symbols

A [`Symbol`](https://api.dart.dev/stable/dart-core/Symbol-class.html) object represents an operator or identifier declared in a Dart program. You might never need to use symbols, but they’re invaluable for APIs that refer to identifiers by name, because minification changes identifier names but not identifier symbols.

To get the symbol for an identifier, use a symbol literal, which is just `#` followed by the identifier:

```nocode
#radix
#bar
```

Symbol literals are compile-time constants.

## Functions

Dart is a true object-oriented language, so even functions are objects and have a type, [Function.](https://api.dart.dev/stable/dart-core/Function-class.html) This means that functions can be assigned to variables or passed as arguments to other functions. You can also call an instance of a Dart class as if it were a function. For details, see [Callable classes](https://dart.dev/guides/language/language-tour#callable-classes).

Here’s an example of implementing a function:

```dart
bool isNoble(int atomicNumber) {
  return _nobleGases[atomicNumber] != null;
}
```

Although Effective Dart recommends [type annotations for public APIs](https://dart.dev/guides/language/effective-dart/design#do-type-annotate-fields-and-top-level-variables-if-the-type-isnt-obvious), the function still works if you omit the types:

```dart
isNoble(atomicNumber) {
  return _nobleGases[atomicNumber] != null;
}
```

For functions that contain just one expression, you can use a shorthand syntax:

```dart
bool isNoble(int atomicNumber) => _nobleGases[atomicNumber] != null;
```

The `=> *expr*` syntax is a shorthand for `{ return *expr*; }`. The `=>` notation is sometimes referred to as *arrow* syntax.

 **Note:** Only an *expression*—not a *statement*—can appear between the arrow (=>) and the semicolon (;). For example, you can’t put an [if statement](https://dart.dev/guides/language/language-tour#if-and-else) there, but you can use a [conditional expression](https://dart.dev/guides/language/language-tour#conditional-expressions).

### Parameters

A function can have any number of *required positional* parameters. These can be followed either by *named* parameters or by *optional positional* parameters (but not both).

 **Note:** Some APIs — notably [Flutter](https://flutter.dev/) widget constructors — use only named parameters, even for parameters that are mandatory. See the next section for details.

You can use [trailing commas](https://dart.dev/guides/language/language-tour#trailing-comma) when you pass arguments to a function or when you define function parameters.

#### Named parameters

Named parameters are optional unless they’re specifically marked as `required`.

When calling a function, you can specify named parameters using `*paramName*: *value*`. For example:

```dart
enableFlags(bold: true, hidden: false);
```

When defining a function, use `{*param1*, *param2*, …}` to specify named parameters:

```dart
/// Sets the [bold] and [hidden] flags ...
void enableFlags({bool? bold, bool? hidden}) {...}
```

 **Tip:** If a parameter is optional but can’t be `null`, provide a [default value](https://dart.dev/guides/language/language-tour#default-parameter-values).

Although named parameters are a kind of optional parameter, you can annotate them with `required` to indicate that the parameter is mandatory — that users must provide a value for the parameter. For example:

```dart
const Scrollbar({Key? key, required Widget child})
```

If someone tries to create a `Scrollbar` without specifying the `child` argument, then the analyzer reports an issue.

#### Optional positional parameters

Wrapping a set of function parameters in `[]` marks them as optional positional parameters:

```dart
String say(String from, String msg, [String? device]) {
  var result = '$from says $msg';
  if (device != null) {
    result = '$result with a $device';
  }
  return result;
}
```

Here’s an example of calling this function without the optional parameter:

```dart
assert(say('Bob', 'Howdy') == 'Bob says Howdy');
```

And here’s an example of calling this function with the third parameter:

```dart
assert(say('Bob', 'Howdy', 'smoke signal') ==
    'Bob says Howdy with a smoke signal');
```



#### Default parameter values

Your function can use `=` to define default values for both named and positional parameters. The default values must be compile-time constants. If no default value is provided, the default value is `null`.

Here’s an example of setting default values for named parameters:

```dart
/// Sets the [bold] and [hidden] flags ...
void enableFlags({bool bold = false, bool hidden = false}) {...}

// bold will be true; hidden will be false.
enableFlags(bold: true);
```

 **Deprecation note:** Old code might use a colon (`:`) instead of `=` to set default values of named parameters. The reason is that originally, only `:` was supported for named parameters. That support might be deprecated, so we recommend that you **[use `=` to specify default values.](https://dart.dev/guides/language/effective-dart/usage#do-use--to-separate-a-named-parameter-from-its-default-value)**

The next example shows how to set default values for positional parameters:

```dart
String say(String from, String msg,
    [String device = 'carrier pigeon']) {
  var result = '$from says $msg with a $device';
  return result;
}

assert(say('Bob', 'Howdy') ==
    'Bob says Howdy with a carrier pigeon');
```

You can also pass lists or maps as default values. The following example defines a function, `doStuff()`, that specifies a default list for the `list` parameter and a default map for the `gifts` parameter.

```dart
void doStuff(
    {List<int> list = const [1, 2, 3],
    Map<String, String> gifts = const {
      'first': 'paper',
      'second': 'cotton',
      'third': 'leather'
    }}) {
  print('list:  $list');
  print('gifts: $gifts');
}
```

### The main() function

Every app must have a top-level `main()` function, which serves as the entrypoint to the app. The `main()` function returns `void` and has an optional `List<String>` parameter for arguments.

Here’s a simple `main()` function:

```dart
void main() {
  print('Hello, World!');
}
```

Here’s an example of the `main()` function for a command-line app that takes arguments:

```dart
// Run the app like this: dart args.dart 1 test
void main(List<String> arguments) {
  print(arguments);

  assert(arguments.length == 2);
  assert(int.parse(arguments[0]) == 1);
  assert(arguments[1] == 'test');
}
```

You can use the [args library](https://pub.dev/packages/args) to define and parse command-line arguments.

### Functions as first-class objects

You can pass a function as a parameter to another function. For example:

```dart
void printElement(int element) {
  print(element);
}

var list = [1, 2, 3];

// Pass printElement as a parameter.
list.forEach(printElement);
```

You can also assign a function to a variable, such as:

```dart
var loudify = (msg) => '!!! ${msg.toUpperCase()} !!!';
assert(loudify('hello') == '!!! HELLO !!!');
```

This example uses an anonymous function. More about those in the next section.

### Anonymous functions

Most functions are named, such as `main()` or `printElement()`. You can also create a nameless function called an *anonymous function*, or sometimes a *lambda* or *closure*. You might assign an anonymous function to a variable so that, for example, you can add or remove it from a collection.

An anonymous function looks similar to a named function— zero or more parameters, separated by commas and optional type annotations, between parentheses.

The code block that follows contains the function’s body:

```
([[*Type*] *param1*[, …]]) { *codeBlock*;};
```

The following example defines an anonymous function with an untyped parameter, `item`. The function, invoked for each item in the list, prints a string that includes the value at the specified index.

```dart
const list = ['apples', 'bananas', 'oranges'];
list.forEach((item) {
  print('${list.indexOf(item)}: $item');
});
```

Click **Run** to execute the code.

<iframe src="https://dartpad.dev/embed-dart.html?theme=light&amp;run=dartpad&amp;split=false&amp;ga_id=anonymous_functions&amp;null_safety=true" style="box-sizing: border-box; border: 1px solid rgb(204, 204, 204); margin-bottom: 1rem; min-height: 400px; resize: vertical; width: 891.273px; height: 400px;"></iframe>

If the function contains only a single expression or return statement, you can shorten it using arrow notation. Paste the following line into DartPad and click **Run** to verify that it is functionally equivalent.

```dart
list.forEach(
    (item) => print('${list.indexOf(item)}: $item'));
```

### Lexical scope

Dart is a lexically scoped language, which means that the scope of variables is determined statically, simply by the layout of the code. You can “follow the curly braces outwards” to see if a variable is in scope.

Here is an example of nested functions with variables at each scope level:

```dart
bool topLevel = true;

void main() {
  var insideMain = true;

  void myFunction() {
    var insideFunction = true;

    void nestedFunction() {
      var insideNestedFunction = true;

      assert(topLevel);
      assert(insideMain);
      assert(insideFunction);
      assert(insideNestedFunction);
    }
  }
}
```

Notice how `nestedFunction()` can use variables from every level, all the way up to the top level.

### Lexical closures

A *closure* is a function object that has access to variables in its lexical scope, even when the function is used outside of its original scope.

Functions can close over variables defined in surrounding scopes. In the following example, `makeAdder()` captures the variable `addBy`. Wherever the returned function goes, it remembers `addBy`.

```dart
/// Returns a function that adds [addBy] to the
/// function's argument.
Function makeAdder(int addBy) {
  return (int i) => addBy + i;
}

void main() {
  // Create a function that adds 2.
  var add2 = makeAdder(2);

  // Create a function that adds 4.
  var add4 = makeAdder(4);

  assert(add2(3) == 5);
  assert(add4(3) == 7);
}
```

### Testing functions for equality

Here’s an example of testing top-level functions, static methods, and instance methods for equality:

```dart
void foo() {} // A top-level function

class A {
  static void bar() {} // A static method
  void baz() {} // An instance method
}

void main() {
  Function x;

  // Comparing top-level functions.
  x = foo;
  assert(foo == x);

  // Comparing static methods.
  x = A.bar;
  assert(A.bar == x);

  // Comparing instance methods.
  var v = A(); // Instance #1 of A
  var w = A(); // Instance #2 of A
  var y = w;
  x = w.baz;

  // These closures refer to the same instance (#2),
  // so they're equal.
  assert(y.baz == x);

  // These closures refer to different instances,
  // so they're unequal.
  assert(v.baz != w.baz);
}
```

### Return values

All functions return a value. If no return value is specified, the statement `return null;` is implicitly appended to the function body.

```dart
foo() {}

assert(foo() == null);
```

## Operators

Dart supports the operators shown in the following table. You can implement many of these [operators as class members](https://dart.dev/guides/language/language-tour#_operators).

| Description              | Operator                                                     |
| ------------------------ | ------------------------------------------------------------ |
| unary postfix            | `*expr*++`  `*expr*--`  `()`  `[]`  `.`  `?.`                |
| unary prefix             | `-*expr*`  `!*expr*`  `~*expr*`  `++*expr*`  `--*expr*`   `await *expr*` |
| multiplicative           | `*`  `/`  `%` `~/`                                           |
| additive                 | `+`  `-`                                                     |
| shift                    | `<<`  `>>`  `>>>`                                            |
| bitwise AND              | `&`                                                          |
| bitwise XOR              | `^`                                                          |
| bitwise OR               | `|`                                                          |
| relational and type test | `>=`  `>`  `<=`  `<`  `as`  `is`  `is!`                      |
| equality                 | `==`  `!=`                                                   |
| logical AND              | `&&`                                                         |
| logical OR               | `||`                                                         |
| if null                  | `??`                                                         |
| conditional              | `*expr1* ? *expr2* : *expr3*`                                |
| cascade                  | `..`  `?..`                                                  |
| assignment               | `=`  `*=`  `/=`  `+=`  `-=`  `&=`  `^=`  *etc.*              |

 **Warning:** Operator precedence is an approximation of the behavior of a Dart parser. For definitive answers, consult the grammar in the [Dart language specification](https://dart.dev/guides/language/spec).

When you use operators, you create expressions. Here are some examples of operator expressions:

```dart
a++
a + b
a = b
a == b
c ? a : b
a is T
```

In the [operator table](https://dart.dev/guides/language/language-tour#operators), each operator has higher precedence than the operators in the rows that follow it. For example, the multiplicative operator `%` has higher precedence than (and thus executes before) the equality operator `==`, which has higher precedence than the logical AND operator `&&`. That precedence means that the following two lines of code execute the same way:

```dart
// Parentheses improve readability.
if ((n % i == 0) && (d % i == 0)) ...

// Harder to read, but equivalent.
if (n % i == 0 && d % i == 0) ...
```

 **Warning:** For operators that take two operands, the leftmost operand determines which method is used. For example, if you have a `Vector` object and a `Point` object, then `aVector + aPoint` uses `Vector` addition (`+`).

### Arithmetic operators

Dart supports the usual arithmetic operators, as shown in the following table.

| Operator  | Meaning                                                      |
| --------- | ------------------------------------------------------------ |
| `+`       | Add                                                          |
| `–`       | Subtract                                                     |
| `-*expr*` | Unary minus, also known as negation (reverse the sign of the expression) |
| `*`       | Multiply                                                     |
| `/`       | Divide                                                       |
| `~/`      | Divide, returning an integer result                          |
| `%`       | Get the remainder of an integer division (modulo)            |

Example:

```dart
assert(2 + 3 == 5);
assert(2 - 3 == -1);
assert(2 * 3 == 6);
assert(5 / 2 == 2.5); // Result is a double
assert(5 ~/ 2 == 2); // Result is an int
assert(5 % 2 == 1); // Remainder

assert('5/2 = ${5 ~/ 2} r ${5 % 2}' == '5/2 = 2 r 1');
```

Dart also supports both prefix and postfix increment and decrement operators.

| Operator  | Meaning                                               |
| --------- | ----------------------------------------------------- |
| `++*var*` | `*var* = *var* + 1` (expression value is `*var* + 1`) |
| `*var*++` | `*var* = *var* + 1` (expression value is `*var*`)     |
| `--*var*` | `*var* = *var* – 1` (expression value is `*var* – 1`) |
| `*var*--` | `*var* = *var* – 1` (expression value is `*var*`)     |

Example:

```dart
int a;
int b;

a = 0;
b = ++a; // Increment a before b gets its value.
assert(a == b); // 1 == 1

a = 0;
b = a++; // Increment a AFTER b gets its value.
assert(a != b); // 1 != 0

a = 0;
b = --a; // Decrement a before b gets its value.
assert(a == b); // -1 == -1

a = 0;
b = a--; // Decrement a AFTER b gets its value.
assert(a != b); // -1 != 0
```

### Equality and relational operators

The following table lists the meanings of equality and relational operators.

| Operator | Meaning                     |
| -------- | --------------------------- |
| `==`     | Equal; see discussion below |
| `!=`     | Not equal                   |
| `>`      | Greater than                |
| `<`      | Less than                   |
| `>=`     | Greater than or equal to    |
| `<=`     | Less than or equal to       |

To test whether two objects x and y represent the same thing, use the `==` operator. (In the rare case where you need to know whether two objects are the exact same object, use the [identical()](https://api.dart.dev/stable/dart-core/identical.html) function instead.) Here’s how the `==` operator works:

1. If *x* or *y* is null, return true if both are null, and false if only one is null.
2. Return the result of the method invocation `*x*.==(*y*)`. (That’s right, operators such as `==` are methods that are invoked on their first operand. For details, see [Operators](https://dart.dev/guides/language/language-tour#_operators).)

Here’s an example of using each of the equality and relational operators:

```dart
assert(2 == 2);
assert(2 != 3);
assert(3 > 2);
assert(2 < 3);
assert(3 >= 3);
assert(2 <= 3);
```

### Type test operators

The `as`, `is`, and `is!` operators are handy for checking types at runtime.

| Operator | Meaning                                                      |
| -------- | ------------------------------------------------------------ |
| `as`     | Typecast (also used to specify [library prefixes](https://dart.dev/guides/language/language-tour#specifying-a-library-prefix)) |
| `is`     | True if the object has the specified type                    |
| `is!`    | True if the object doesn’t have the specified type           |

The result of `obj is T` is true if `obj` implements the interface specified by `T`. For example, `obj is Object?` is always true.

Use the `as` operator to cast an object to a particular type if and only if you are sure that the object is of that type. Example:

```dart
(employee as Person).firstName = 'Bob';
```

If you aren’t sure that the object is of type `T`, then use `is T` to check the type before using the object.

```dart
if (employee is Person) {
  // Type check
  employee.firstName = 'Bob';
}
```

 **Note:** The code isn’t equivalent. If `employee` is null or not a `Person`, the first example throws an exception; the second does nothing.

### Assignment operators

As you’ve already seen, you can assign values using the `=` operator. To assign only if the assigned-to variable is null, use the `??=` operator.

```dart
// Assign value to a
a = value;
// Assign value to b if b is null; otherwise, b stays the same
b ??= value;
```

Compound assignment operators such as `+=` combine an operation with an assignment.

| `=`  | `–=` | `/=`  | `%=`  | `>>=` | `^=` |
| ---- | ---- | ----- | ----- | ----- | ---- |
| `+=` | `*=` | `~/=` | `<<=` | `&=`  | `|=` |

Here’s how compound assignment operators work:

|                             | Compound assignment | Equivalent expression |
| --------------------------- | ------------------- | --------------------- |
| **For an operator \*op\*:** | `a *op*= b`         | `a = a *op* b`        |
| **Example:**                | `a += b`            | `a = a + b`           |

The following example uses assignment and compound assignment operators:

```dart
var a = 2; // Assign using =
a *= 3; // Assign and multiply: a = a * 3
assert(a == 6);
```

### Logical operators

You can invert or combine boolean expressions using the logical operators.

| Operator  | Meaning                                                      |
| --------- | ------------------------------------------------------------ |
| `!*expr*` | inverts the following expression (changes false to true, and vice versa) |
| `||`      | logical OR                                                   |
| `&&`      | logical AND                                                  |

Here’s an example of using the logical operators:

```dart
if (!done && (col == 0 || col == 3)) {
  // ...Do something...
}
```

### Bitwise and shift operators

You can manipulate the individual bits of numbers in Dart. Usually, you’d use these bitwise and shift operators with integers.

| Operator  | Meaning                                               |
| --------- | ----------------------------------------------------- |
| `&`       | AND                                                   |
| `|`       | OR                                                    |
| `^`       | XOR                                                   |
| `~*expr*` | Unary bitwise complement (0s become 1s; 1s become 0s) |
| `<<`      | Shift left                                            |
| `>>`      | Shift right                                           |

Here’s an example of using bitwise and shift operators:

```dart
final value = 0x22;
final bitmask = 0x0f;

assert((value & bitmask) == 0x02); // AND
assert((value & ~bitmask) == 0x20); // AND NOT
assert((value | bitmask) == 0x2f); // OR
assert((value ^ bitmask) == 0x2d); // XOR
assert((value << 4) == 0x220); // Shift left
assert((value >> 4) == 0x02); // Shift right
```

### Conditional expressions

Dart has two operators that let you concisely evaluate expressions that might otherwise require [if-else](https://dart.dev/guides/language/language-tour#if-and-else) statements:

- `*condition* ? *expr1* : *expr2*`

  If *condition* is true, evaluates *expr1* (and returns its value); otherwise, evaluates and returns the value of *expr2*.

- `*expr1* ?? *expr2*`

  If *expr1* is non-null, returns its value; otherwise, evaluates and returns the value of *expr2*.

When you need to assign a value based on a boolean expression, consider using `?` and `:`.

```dart
var visibility = isPublic ? 'public' : 'private';
```

If the boolean expression tests for null, consider using `??`.

```dart
String playerName(String? name) => name ?? 'Guest';
```

The previous example could have been written at least two other ways, but not as succinctly:

```dart
// Slightly longer version uses ?: operator.
String playerName(String? name) => name != null ? name : 'Guest';

// Very long version uses if-else statement.
String playerName(String? name) {
  if (name != null) {
    return name;
  } else {
    return 'Guest';
  }
}
```



### Cascade notation

Cascades (`..`, `?..`) allow you to make a sequence of operations on the same object. In addition to function calls, you can also access fields on that same object. This often saves you the step of creating a temporary variable and allows you to write more fluid code.

Consider the following code:

```dart
var paint = Paint()
  ..color = Colors.black
  ..strokeCap = StrokeCap.round
  ..strokeWidth = 5.0;
```

The constructor, `Paint()`, returns a `Paint` object. The code that follows the cascade notation operates on this object, ignoring any values that might be returned.

The previous example is equivalent to this code:

```dart
var paint = Paint();
paint.color = Colors.black;
paint.strokeCap = StrokeCap.round;
paint.strokeWidth = 5.0;
```

If the object that the cascade operates on can be null, then use a *null-shorting* cascade (`?..`) for the first operation. Starting with `?..` guarantees that none of the cascade operations are attempted on that null object.

```dart
querySelector('#confirm') // Get an object.
  ?..text = 'Confirm' // Use its members.
  ..classes.add('important')
  ..onClick.listen((e) => window.alert('Confirmed!'));
```

 **Version note:** The `?..` syntax requires a [language version](https://dart.dev/guides/language/evolution#language-versioning) of at least 2.12.

The previous code is equivalent to the following:

```dart
var button = querySelector('#confirm');
button?.text = 'Confirm';
button?.classes.add('important');
button?.onClick.listen((e) => window.alert('Confirmed!'));
```

You can also nest cascades. For example:

```dart
final addressBook = (AddressBookBuilder()
      ..name = 'jenny'
      ..email = 'jenny@example.com'
      ..phone = (PhoneNumberBuilder()
            ..number = '415-555-0100'
            ..label = 'home')
          .build())
    .build();
```

Be careful to construct your cascade on a function that returns an actual object. For example, the following code fails:

```dart
var sb = StringBuffer();
sb.write('foo')
  ..write('bar'); // Error: method 'write' isn't defined for 'void'.
```

The `sb.write()` call returns void, and you can’t construct a cascade on `void`.

 **Note:** Strictly speaking, the “double dot” notation for cascades isn’t an operator. It’s just part of the Dart syntax.

### Other operators

You’ve seen most of the remaining operators in other examples:

| Operator | Name                      | Meaning                                                      |
| -------- | ------------------------- | ------------------------------------------------------------ |
| `()`     | Function application      | Represents a function call                                   |
| `[]`     | List access               | Refers to the value at the specified index in the list       |
| `.`      | Member access             | Refers to a property of an expression; example: `foo.bar` selects property `bar` from expression `foo` |
| `?.`     | Conditional member access | Like `.`, but the leftmost operand can be null; example: `foo?.bar` selects property `bar` from expression `foo` unless `foo` is null (in which case the value of `foo?.bar` is null) |

For more information about the `.`, `?.`, and `..` operators, see [Classes](https://dart.dev/guides/language/language-tour#classes).

## Control flow statements

You can control the flow of your Dart code using any of the following:

- `if` and `else`
- `for` loops
- `while` and `do`-`while` loops
- `break` and `continue`
- `switch` and `case`
- `assert`

You can also affect the control flow using `try-catch` and `throw`, as explained in [Exceptions](https://dart.dev/guides/language/language-tour#exceptions).

### If and else

Dart supports `if` statements with optional `else` statements, as the next sample shows. Also see [conditional expressions](https://dart.dev/guides/language/language-tour#conditional-expressions).

```dart
if (isRaining()) {
  you.bringRainCoat();
} else if (isSnowing()) {
  you.wearJacket();
} else {
  car.putTopDown();
}
```

Unlike JavaScript, conditions must use boolean values, nothing else. See [Booleans](https://dart.dev/guides/language/language-tour#booleans) for more information.

### For loops

You can iterate with the standard `for` loop. For example:

```dart
var message = StringBuffer('Dart is fun');
for (var i = 0; i < 5; i++) {
  message.write('!');
}
```

Closures inside of Dart’s `for` loops capture the *value* of the index, avoiding a common pitfall found in JavaScript. For example, consider:

```dart
var callbacks = [];
for (var i = 0; i < 2; i++) {
  callbacks.add(() => print(i));
}
callbacks.forEach((c) => c());
```

The output is `0` and then `1`, as expected. In contrast, the example would print `2` and then `2` in JavaScript.

If the object that you are iterating over is an Iterable (such as List or Set) and if you don’t need to know the current iteration counter, you can use the `for-in` form of [iteration](https://dart.dev/guides/libraries/library-tour#iteration):

```dart
for (var candidate in candidates) {
  candidate.interview();
}
```

 **Tip:** To practice using `for-in`, follow the [Iterable collections codelab](https://dart.dev/codelabs/iterables).

Iterable classes also have a [forEach()](https://api.dart.dev/stable/dart-core/Iterable/forEach.html) method as another option:

```dart
var collection = [1, 2, 3];
collection.forEach(print); // 1 2 3
```

### While and do-while

A `while` loop evaluates the condition before the loop:

```dart
while (!isDone()) {
  doSomething();
}
```

A `do`-`while` loop evaluates the condition *after* the loop:

```dart
do {
  printLine();
} while (!atEndOfPage());
```

### Break and continue

Use `break` to stop looping:

```dart
while (true) {
  if (shutDownRequested()) break;
  processIncomingRequests();
}
```

Use `continue` to skip to the next loop iteration:

```dart
for (int i = 0; i < candidates.length; i++) {
  var candidate = candidates[i];
  if (candidate.yearsExperience < 5) {
    continue;
  }
  candidate.interview();
}
```

You might write that example differently if you’re using an [`Iterable`](https://api.dart.dev/stable/dart-core/Iterable-class.html) such as a list or set:

```dart
candidates
    .where((c) => c.yearsExperience >= 5)
    .forEach((c) => c.interview());
```

### Switch and case

Switch statements in Dart compare integer, string, or compile-time constants using `==`. The compared objects must all be instances of the same class (and not of any of its subtypes), and the class must not override `==`. [Enumerated types](https://dart.dev/guides/language/language-tour#enumerated-types) work well in `switch` statements.

Each non-empty `case` clause ends with a `break` statement, as a rule. Other valid ways to end a non-empty `case` clause are a `continue`, `throw`, or `return` statement.

Use a `default` clause to execute code when no `case` clause matches:

```dart
var command = 'OPEN';
switch (command) {
  case 'CLOSED':
    executeClosed();
    break;
  case 'PENDING':
    executePending();
    break;
  case 'APPROVED':
    executeApproved();
    break;
  case 'DENIED':
    executeDenied();
    break;
  case 'OPEN':
    executeOpen();
    break;
  default:
    executeUnknown();
}
```

The following example omits the `break` statement in a `case` clause, thus generating an error:

```dart
var command = 'OPEN';
switch (command) {
  case 'OPEN':
    executeOpen();
    // ERROR: Missing break

  case 'CLOSED':
    executeClosed();
    break;
}
```

However, Dart does support empty `case` clauses, allowing a form of fall-through:

```dart
var command = 'CLOSED';
switch (command) {
  case 'CLOSED': // Empty case falls through.
  case 'NOW_CLOSED':
    // Runs for both CLOSED and NOW_CLOSED.
    executeNowClosed();
    break;
}
```

If you really want fall-through, you can use a `continue` statement and a label:

```dart
var command = 'CLOSED';
switch (command) {
  case 'CLOSED':
    executeClosed();
    continue nowClosed;
  // Continues executing at the nowClosed label.

  nowClosed:
  case 'NOW_CLOSED':
    // Runs for both CLOSED and NOW_CLOSED.
    executeNowClosed();
    break;
}
```

A `case` clause can have local variables, which are visible only inside the scope of that clause.

### Assert

During development, use an assert statement — `assert(*condition*, *optionalMessage*)`; — to disrupt normal execution if a boolean condition is false. You can find examples of assert statements throughout this tour. Here are some more:

```dart
// Make sure the variable has a non-null value.
assert(text != null);

// Make sure the value is less than 100.
assert(number < 100);

// Make sure this is an https URL.
assert(urlString.startsWith('https'));
```

To attach a message to an assertion, add a string as the second argument to `assert` (optionally with a [trailing comma](https://dart.dev/guides/language/language-tour#trailing-comma)):

```dart
assert(urlString.startsWith('https'),
    'URL ($urlString) should start with "https".');
```

The first argument to `assert` can be any expression that resolves to a boolean value. If the expression’s value is true, the assertion succeeds and execution continues. If it’s false, the assertion fails and an exception (an [`AssertionError`](https://api.dart.dev/stable/dart-core/AssertionError-class.html)) is thrown.

When exactly do assertions work? That depends on the tools and framework you’re using:

- Flutter enables assertions in [debug mode.](https://flutter.dev/docs/testing/debugging#debug-mode-assertions)
- Development-only tools such as [dartdevc](https://dart.dev/tools/dartdevc) typically enable assertions by default.
- Some tools, such as [`dart run`](https://dart.dev/tools/dart-run) and [`dart2js`](https://dart.dev/tools/dart2js) support assertions through a command-line flag: `--enable-asserts`.

In production code, assertions are ignored, and the arguments to `assert` aren’t evaluated.

## Exceptions

Your Dart code can throw and catch exceptions. Exceptions are errors indicating that something unexpected happened. If the exception isn’t caught, the [isolate](https://dart.dev/guides/language/language-tour#isolates) that raised the exception is suspended, and typically the isolate and its program are terminated.

In contrast to Java, all of Dart’s exceptions are unchecked exceptions. Methods don’t declare which exceptions they might throw, and you aren’t required to catch any exceptions.

Dart provides [`Exception`](https://api.dart.dev/stable/dart-core/Exception-class.html) and [`Error`](https://api.dart.dev/stable/dart-core/Error-class.html) types, as well as numerous predefined subtypes. You can, of course, define your own exceptions. However, Dart programs can throw any non-null object—not just Exception and Error objects—as an exception.

### Throw

Here’s an example of throwing, or *raising*, an exception:

```dart
throw FormatException('Expected at least 1 section');
```

You can also throw arbitrary objects:

```dart
throw 'Out of llamas!';
```

 **Note:** Production-quality code usually throws types that implement [`Error`](https://api.dart.dev/stable/dart-core/Error-class.html) or [`Exception`](https://api.dart.dev/stable/dart-core/Exception-class.html).

Because throwing an exception is an expression, you can throw exceptions in => statements, as well as anywhere else that allows expressions:

```dart
void distanceTo(Point other) => throw UnimplementedError();
```

### Catch

Catching, or capturing, an exception stops the exception from propagating (unless you rethrow the exception). Catching an exception gives you a chance to handle it:

```dart
try {
  breedMoreLlamas();
} on OutOfLlamasException {
  buyMoreLlamas();
}
```

To handle code that can throw more than one type of exception, you can specify multiple catch clauses. The first catch clause that matches the thrown object’s type handles the exception. If the catch clause does not specify a type, that clause can handle any type of thrown object:

```dart
try {
  breedMoreLlamas();
} on OutOfLlamasException {
  // A specific exception
  buyMoreLlamas();
} on Exception catch (e) {
  // Anything else that is an exception
  print('Unknown exception: $e');
} catch (e) {
  // No specified type, handles all
  print('Something really unknown: $e');
}
```

As the preceding code shows, you can use either `on` or `catch` or both. Use `on` when you need to specify the exception type. Use `catch` when your exception handler needs the exception object.

You can specify one or two parameters to `catch()`. The first is the exception that was thrown, and the second is the stack trace (a [`StackTrace`](https://api.dart.dev/stable/dart-core/StackTrace-class.html) object).

```dart
try {
  // ···
} on Exception catch (e) {
  print('Exception details:\n $e');
} catch (e, s) {
  print('Exception details:\n $e');
  print('Stack trace:\n $s');
}
```

To partially handle an exception, while allowing it to propagate, use the `rethrow` keyword.

```dart
void misbehave() {
  try {
    dynamic foo = true;
    print(foo++); // Runtime error
  } catch (e) {
    print('misbehave() partially handled ${e.runtimeType}.');
    rethrow; // Allow callers to see the exception.
  }
}

void main() {
  try {
    misbehave();
  } catch (e) {
    print('main() finished handling ${e.runtimeType}.');
  }
}
```

### Finally

To ensure that some code runs whether or not an exception is thrown, use a `finally` clause. If no `catch` clause matches the exception, the exception is propagated after the `finally` clause runs:

```dart
try {
  breedMoreLlamas();
} finally {
  // Always clean up, even if an exception is thrown.
  cleanLlamaStalls();
}
```

The `finally` clause runs after any matching `catch` clauses:

```dart
try {
  breedMoreLlamas();
} catch (e) {
  print('Error: $e'); // Handle the exception first.
} finally {
  cleanLlamaStalls(); // Then clean up.
}
```

Learn more by reading the [Exceptions](https://dart.dev/guides/libraries/library-tour#exceptions) section of the library tour.

## Classes

Dart is an object-oriented language with classes and mixin-based inheritance. Every object is an instance of a class, and all classes except `Null` descend from [`Object`](https://api.dart.dev/stable/dart-core/Object-class.html). *Mixin-based inheritance* means that although every class (except for the [top class](https://dart.dev/null-safety/understanding-null-safety#top-and-bottom),`Object?`) has exactly one superclass, a class body can be reused in multiple class hierarchies. [Extension methods](https://dart.dev/guides/language/language-tour#extension-methods) are a way to add functionality to a class without changing the class or creating a subclass.

### Using class members

Objects have *members* consisting of functions and data (*methods* and *instance variables*, respectively). When you call a method, you *invoke* it on an object: the method has access to that object’s functions and data.

Use a dot (`.`) to refer to an instance variable or method:

```dart
var p = Point(2, 2);

// Get the value of y.
assert(p.y == 2);

// Invoke distanceTo() on p.
double distance = p.distanceTo(Point(4, 4));
```

Use `?.` instead of `.` to avoid an exception when the leftmost operand is null:

```dart
// If p is non-null, set a variable equal to its y value.
var a = p?.y;
```

### Using constructors

You can create an object using a *constructor*. Constructor names can be either `*ClassName*` or `*ClassName*.*identifier*`. For example, the following code creates `Point` objects using the `Point()` and `Point.fromJson()` constructors:

```dart
var p1 = Point(2, 2);
var p2 = Point.fromJson({'x': 1, 'y': 2});
```

The following code has the same effect, but uses the optional `new` keyword before the constructor name:

```dart
var p1 = new Point(2, 2);
var p2 = new Point.fromJson({'x': 1, 'y': 2});
```

 **Version note:** The `new` keyword became optional in Dart 2.

Some classes provide [constant constructors](https://dart.dev/guides/language/language-tour#constant-constructors). To create a compile-time constant using a constant constructor, put the `const` keyword before the constructor name:

```dart
var p = const ImmutablePoint(2, 2);
```

Constructing two identical compile-time constants results in a single, canonical instance:

```dart
var a = const ImmutablePoint(1, 1);
var b = const ImmutablePoint(1, 1);

assert(identical(a, b)); // They are the same instance!
```

Within a *constant context*, you can omit the `const` before a constructor or literal. For example, look at this code, which creates a const map:

```dart
// Lots of const keywords here.
const pointAndLine = const {
  'point': const [const ImmutablePoint(0, 0)],
  'line': const [const ImmutablePoint(1, 10), const ImmutablePoint(-2, 11)],
};
```

You can omit all but the first use of the `const` keyword:

```dart
// Only one const, which establishes the constant context.
const pointAndLine = {
  'point': [ImmutablePoint(0, 0)],
  'line': [ImmutablePoint(1, 10), ImmutablePoint(-2, 11)],
};
```

If a constant constructor is outside of a constant context and is invoked without `const`, it creates a **non-constant object**:

```dart
var a = const ImmutablePoint(1, 1); // Creates a constant
var b = ImmutablePoint(1, 1); // Does NOT create a constant

assert(!identical(a, b)); // NOT the same instance!
```

 **Version note:** The `const` keyword became optional within a constant context in Dart 2.

### Getting an object’s type

To get an object’s type at runtime, you can use the `Object` property `runtimeType`, which returns a [`Type`](https://api.dart.dev/stable/dart-core/Type-class.html) object.

```dart
print('The type of a is ${a.runtimeType}');
```

Up to here, you’ve seen how to *use* classes. The rest of this section shows how to *implement* classes.

### Instance variables

Here’s how you declare instance variables:

```dart
class Point {
  double? x; // Declare instance variable x, initially null.
  double? y; // Declare y, initially null.
  double z = 0; // Declare z, initially 0.
}
```

All uninitialized instance variables have the value `null`.

All instance variables generate an implicit *getter* method. Non-final instance variables and `late final` instance variables without initializers also generate an implicit *setter* method. For details, see [Getters and setters](https://dart.dev/guides/language/language-tour#getters-and-setters).

If you initialize a non-`late` instance variable where it’s declared, the value is set when the instance is created, which is before the constructor and its initializer list execute.

```dart
class Point {
  double? x; // Declare instance variable x, initially null.
  double? y; // Declare y, initially null.
}

void main() {
  var point = Point();
  point.x = 4; // Use the setter method for x.
  assert(point.x == 4); // Use the getter method for x.
  assert(point.y == null); // Values default to null.
}
```

Instance variables can be `final`, in which case they must be set exactly once. Initialize `final`, non-`late` instance variables at declaration, using a constructor parameter, or using a constructor’s [initializer list](https://dart.dev/guides/language/language-tour#initializer-list):

```dart
class ProfileMark {
  final String name;
  final DateTime start = DateTime.now();

  ProfileMark(this.name);
  ProfileMark.unnamed() : name = '';
}
```

If you want to assign the value of a `final` instance variable after the constructor body starts, you can use `late final`, [but *be careful*](https://dart.dev/guides/language/effective-dart/design#avoid-public-late-final-fields-without-initializers).

### Constructors

Declare a constructor by creating a function with the same name as its class (plus, optionally, an additional identifier as described in [Named constructors](https://dart.dev/guides/language/language-tour#named-constructors)). The most common form of constructor, the generative constructor, creates a new instance of a class:

```dart
class Point {
  double x = 0;
  double y = 0;

  Point(double x, double y) {
    // There's a better way to do this, stay tuned.
    this.x = x;
    this.y = y;
  }
}
```

The `this` keyword refers to the current instance.

 **Note:** Use `this` only when there is a name conflict. Otherwise, Dart style omits the `this`.

The pattern of assigning a constructor argument to an instance variable is so common, Dart has syntactic sugar to make it easy:

```dart
class Point {
  double x = 0;
  double y = 0;

  // Syntactic sugar for setting x and y
  // before the constructor body runs.
  Point(this.x, this.y);
}
```

#### Default constructors

If you don’t declare a constructor, a default constructor is provided for you. The default constructor has no arguments and invokes the no-argument constructor in the superclass.

#### Constructors aren’t inherited

Subclasses don’t inherit constructors from their superclass. A subclass that declares no constructors has only the default (no argument, no name) constructor.

#### Named constructors

Use a named constructor to implement multiple constructors for a class or to provide extra clarity:

```dart
const double xOrigin = 0;
const double yOrigin = 0;

class Point {
  double x = 0;
  double y = 0;

  Point(this.x, this.y);

  // Named constructor
  Point.origin()
      : x = xOrigin,
        y = yOrigin;
}
```

Remember that constructors are not inherited, which means that a superclass’s named constructor is not inherited by a subclass. If you want a subclass to be created with a named constructor defined in the superclass, you must implement that constructor in the subclass.

#### Invoking a non-default superclass constructor

By default, a constructor in a subclass calls the superclass’s unnamed, no-argument constructor. The superclass’s constructor is called at the beginning of the constructor body. If an [initializer list](https://dart.dev/guides/language/language-tour#initializer-list) is also being used, it executes before the superclass is called. In summary, the order of execution is as follows:

1. initializer list
2. superclass’s no-arg constructor
3. main class’s no-arg constructor

If the superclass doesn’t have an unnamed, no-argument constructor, then you must manually call one of the constructors in the superclass. Specify the superclass constructor after a colon (`:`), just before the constructor body (if any).

In the following example, the constructor for the Employee class calls the named constructor for its superclass, Person. Click **Run** to execute the code.

<iframe src="https://dartpad.dev/embed-dart.html?theme=light&amp;run=dartpad&amp;split=false&amp;ga_id=non_default_superclass_constructor&amp;null_safety=true" style="box-sizing: border-box; border: 1px solid rgb(204, 204, 204); margin-bottom: 1rem; min-height: 400px; resize: vertical; width: 891.273px; height: 450px;"></iframe>

Because the arguments to the superclass constructor are evaluated before invoking the constructor, an argument can be an expression such as a function call:

```dart
class Employee extends Person {
  Employee() : super.fromJson(fetchDefaultData());
  // ···
}
```

 **Warning:** Arguments to the superclass constructor don’t have access to `this`. For example, arguments can call static methods but not instance methods.

#### Initializer list

Besides invoking a superclass constructor, you can also initialize instance variables before the constructor body runs. Separate initializers with commas.

```dart
// Initializer list sets instance variables before
// the constructor body runs.
Point.fromJson(Map<String, double> json)
    : x = json['x']!,
      y = json['y']! {
  print('In Point.fromJson(): ($x, $y)');
}
```

 **Warning:** The right-hand side of an initializer doesn’t have access to `this`.

During development, you can validate inputs by using `assert` in the initializer list.

```dart
Point.withAssert(this.x, this.y) : assert(x >= 0) {
  print('In Point.withAssert(): ($x, $y)');
}
```

Initializer lists are handy when setting up final fields. The following example initializes three final fields in an initializer list. Click **Run** to execute the code.

<iframe src="https://dartpad.dev/embed-dart.html?theme=light&amp;run=dartpad&amp;split=false&amp;ga_id=initializer_list&amp;null_safety=true" style="box-sizing: border-box; border: 1px solid rgb(204, 204, 204); margin-bottom: 1rem; min-height: 400px; resize: vertical; width: 891.273px; height: 340px;"></iframe>

#### Redirecting constructors

Sometimes a constructor’s only purpose is to redirect to another constructor in the same class. A redirecting constructor’s body is empty, with the constructor call (using `this` instead of the class name) appearing after a colon (:).

```dart
class Point {
  double x, y;

  // The main constructor for this class.
  Point(this.x, this.y);

  // Delegates to the main constructor.
  Point.alongXAxis(double x) : this(x, 0);
}
```

#### Constant constructors

If your class produces objects that never change, you can make these objects compile-time constants. To do this, define a `const` constructor and make sure that all instance variables are `final`.

```dart
class ImmutablePoint {
  static const ImmutablePoint origin = ImmutablePoint(0, 0);

  final double x, y;

  const ImmutablePoint(this.x, this.y);
}
```

Constant constructors don’t always create constants. For details, see the section on [using constructors](https://dart.dev/guides/language/language-tour#using-constructors).

#### Factory constructors

Use the `factory` keyword when implementing a constructor that doesn’t always create a new instance of its class. For example, a factory constructor might return an instance from a cache, or it might return an instance of a subtype. Another use case for factory constructors is initializing a final variable using logic that can’t be handled in the initializer list.

In the following example, the `Logger` factory constructor returns objects from a cache, and the `Logger.fromJson` factory constructor initializes a final variable from a JSON object.

```dart
class Logger {
  final String name;
  bool mute = false;

  // _cache is library-private, thanks to
  // the _ in front of its name.
  static final Map<String, Logger> _cache =
      <String, Logger>{};

  factory Logger(String name) {
    return _cache.putIfAbsent(
        name, () => Logger._internal(name));
  }

  factory Logger.fromJson(Map<String, Object> json) {
    return Logger(json['name'].toString());
  }

  Logger._internal(this.name);

  void log(String msg) {
    if (!mute) print(msg);
  }
}
```

 **Note:** Factory constructors have no access to `this`.

Invoke a factory constructor just like you would any other constructor:

```dart
var logger = Logger('UI');
logger.log('Button clicked');

var logMap = {'name': 'UI'};
var loggerJson = Logger.fromJson(logMap);
```

### Methods

Methods are functions that provide behavior for an object.

#### Instance methods

Instance methods on objects can access instance variables and `this`. The `distanceTo()` method in the following sample is an example of an instance method:

```dart
import 'dart:math';

class Point {
  double x = 0;
  double y = 0;

  Point(this.x, this.y);

  double distanceTo(Point other) {
    var dx = x - other.x;
    var dy = y - other.y;
    return sqrt(dx * dx + dy * dy);
  }
}
```

#### Operators

Operators are instance methods with special names. Dart allows you to define operators with the following names:

| `<`  | `+`  | `|`  | `[]`  |
| ---- | ---- | ---- | ----- |
| `>`  | `/`  | `^`  | `[]=` |
| `<=` | `~/` | `&`  | `~`   |
| `>=` | `*`  | `<<` | `==`  |
| `–`  | `%`  | `>>` |       |

 **Note:** You may have noticed that some [operators](https://dart.dev/guides/language/language-tour#operators), like `!=`, aren’t in the list of names. That’s because they’re just syntactic sugar. For example, the expression `e1 != e2` is syntactic sugar for `!(e1 == e2)`.

An operator declaration is identified using the built-in identifier `operator`. The following example defines vector addition (`+`) and subtraction (`-`):

```dart
class Vector {
  final int x, y;

  Vector(this.x, this.y);

  Vector operator +(Vector v) => Vector(x + v.x, y + v.y);
  Vector operator -(Vector v) => Vector(x - v.x, y - v.y);

  // Operator == and hashCode not shown.
  // ···
}

void main() {
  final v = Vector(2, 3);
  final w = Vector(2, 2);

  assert(v + w == Vector(4, 5));
  assert(v - w == Vector(0, 1));
}
```

#### Getters and setters

Getters and setters are special methods that provide read and write access to an object’s properties. Recall that each instance variable has an implicit getter, plus a setter if appropriate. You can create additional properties by implementing getters and setters, using the `get` and `set` keywords:

```dart
class Rectangle {
  double left, top, width, height;

  Rectangle(this.left, this.top, this.width, this.height);

  // Define two calculated properties: right and bottom.
  double get right => left + width;
  set right(double value) => left = value - width;
  double get bottom => top + height;
  set bottom(double value) => top = value - height;
}

void main() {
  var rect = Rectangle(3, 4, 20, 15);
  assert(rect.left == 3);
  rect.right = 12;
  assert(rect.left == -8);
}
```

With getters and setters, you can start with instance variables, later wrapping them with methods, all without changing client code.

 **Note:** Operators such as increment (++) work in the expected way, whether or not a getter is explicitly defined. To avoid any unexpected side effects, the operator calls the getter exactly once, saving its value in a temporary variable.

#### Abstract methods

Instance, getter, and setter methods can be abstract, defining an interface but leaving its implementation up to other classes. Abstract methods can only exist in [abstract classes](https://dart.dev/guides/language/language-tour#abstract-classes).

To make a method abstract, use a semicolon (;) instead of a method body:

```dart
abstract class Doer {
  // Define instance variables and methods...

  void doSomething(); // Define an abstract method.
}

class EffectiveDoer extends Doer {
  void doSomething() {
    // Provide an implementation, so the method is not abstract here...
  }
}
```

### Abstract classes

Use the `abstract` modifier to define an *abstract class*—a class that can’t be instantiated. Abstract classes are useful for defining interfaces, often with some implementation. If you want your abstract class to appear to be instantiable, define a [factory constructor](https://dart.dev/guides/language/language-tour#factory-constructors).

Abstract classes often have [abstract methods](https://dart.dev/guides/language/language-tour#abstract-methods). Here’s an example of declaring an abstract class that has an abstract method:

```dart
// This class is declared abstract and thus
// can't be instantiated.
abstract class AbstractContainer {
  // Define constructors, fields, methods...

  void updateChildren(); // Abstract method.
}
```

### Implicit interfaces

Every class implicitly defines an interface containing all the instance members of the class and of any interfaces it implements. If you want to create a class A that supports class B’s API without inheriting B’s implementation, class A should implement the B interface.

A class implements one or more interfaces by declaring them in an `implements` clause and then providing the APIs required by the interfaces. For example:

```dart
// A person. The implicit interface contains greet().
class Person {
  // In the interface, but visible only in this library.
  final String _name;

  // Not in the interface, since this is a constructor.
  Person(this._name);

  // In the interface.
  String greet(String who) => 'Hello, $who. I am $_name.';
}

// An implementation of the Person interface.
class Impostor implements Person {
  String get _name => '';

  String greet(String who) => 'Hi $who. Do you know who I am?';
}

String greetBob(Person person) => person.greet('Bob');

void main() {
  print(greetBob(Person('Kathy')));
  print(greetBob(Impostor()));
}
```

Here’s an example of specifying that a class implements multiple interfaces:

```dart
class Point implements Comparable, Location {...}
```

### Extending a class

Use `extends` to create a subclass, and `super` to refer to the superclass:

```dart
class Television {
  void turnOn() {
    _illuminateDisplay();
    _activateIrSensor();
  }
  // ···
}

class SmartTelevision extends Television {
  void turnOn() {
    super.turnOn();
    _bootNetworkInterface();
    _initializeMemory();
    _upgradeApps();
  }
  // ···
}
```



#### Overriding members

Subclasses can override instance methods (including [operators](https://dart.dev/guides/language/language-tour#_operators)), getters, and setters. You can use the `@override` annotation to indicate that you are intentionally overriding a member:

```dart
class SmartTelevision extends Television {
  @override
  void turnOn() {...}
  // ···
}
```

To narrow the type of a method parameter or instance variable in code that is [type safe](https://dart.dev/guides/language/type-system), you can use the [`covariant` keyword](https://dart.dev/guides/language/sound-problems#the-covariant-keyword).

 **Warning:** If you override `==`, you should also override Object’s `hashCode` getter. For an example of overriding `==` and `hashCode`, see [Implementing map keys](https://dart.dev/guides/libraries/library-tour#implementing-map-keys).

#### noSuchMethod()

To detect or react whenever code attempts to use a non-existent method or instance variable, you can override `noSuchMethod()`:

```dart
class A {
  // Unless you override noSuchMethod, using a
  // non-existent member results in a NoSuchMethodError.
  @override
  void noSuchMethod(Invocation invocation) {
    print('You tried to use a non-existent member: '
        '${invocation.memberName}');
  }
}
```

You **can’t invoke** an unimplemented method unless **one** of the following is true:

- The receiver has the static type `dynamic`.
- The receiver has a static type that defines the unimplemented method (abstract is OK), and the dynamic type of the receiver has an implementation of `noSuchMethod()` that’s different from the one in class `Object`.

For more information, see the informal [noSuchMethod forwarding specification.](https://github.com/dart-lang/sdk/blob/master/docs/language/informal/nosuchmethod-forwarding.md)

### Extension methods

Extension methods are a way to add functionality to existing libraries. You might use extension methods without even knowing it. For example, when you use code completion in an IDE, it suggests extension methods alongside regular methods.

Here’s an example of using an extension method on `String` named `parseInt()` that’s defined in `string_apis.dart`:

```
import 'string_apis.dart';
...
print('42'.padLeft(5)); // Use a String method.
print('42'.parseInt()); // Use an extension method.
```

For details of using and implementing extension methods, see the [extension methods page](https://dart.dev/guides/language/extension-methods).



### Enumerated types

Enumerated types, often called *enumerations* or *enums*, are a special kind of class used to represent a fixed number of constant values.

#### Using enums

Declare an enumerated type using the `enum` keyword:

```dart
enum Color { red, green, blue }
```

You can use [trailing commas](https://dart.dev/guides/language/language-tour#trailing-comma) when declaring an enumerated type.

Each value in an enum has an `index` getter, which returns the zero-based position of the value in the enum declaration. For example, the first value has index 0, and the second value has index 1.

```dart
assert(Color.red.index == 0);
assert(Color.green.index == 1);
assert(Color.blue.index == 2);
```

To get a list of all of the values in the enum, use the enum’s `values` constant.

```dart
List<Color> colors = Color.values;
assert(colors[2] == Color.blue);
```

You can use enums in [switch statements](https://dart.dev/guides/language/language-tour#switch-and-case), and you’ll get a warning if you don’t handle all of the enum’s values:

```dart
var aColor = Color.blue;

switch (aColor) {
  case Color.red:
    print('Red as roses!');
    break;
  case Color.green:
    print('Green as grass!');
    break;
  default: // Without this, you see a WARNING.
    print(aColor); // 'Color.blue'
}
```

Enumerated types have the following limits:

- You can’t subclass, mix in, or implement an enum.
- You can’t explicitly instantiate an enum.

For more information, see the [Dart language specification](https://dart.dev/guides/language/spec).

### Adding features to a class: mixins

Mixins are a way of reusing a class’s code in multiple class hierarchies.

To *use* a mixin, use the `with` keyword followed by one or more mixin names. The following example shows two classes that use mixins:

```dart
class Musician extends Performer with Musical {
  // ···
}

class Maestro extends Person
    with Musical, Aggressive, Demented {
  Maestro(String maestroName) {
    name = maestroName;
    canConduct = true;
  }
}
```

To *implement* a mixin, create a class that extends Object and declares no constructors. Unless you want your mixin to be usable as a regular class, use the `mixin` keyword instead of `class`. For example:

```dart
mixin Musical {
  bool canPlayPiano = false;
  bool canCompose = false;
  bool canConduct = false;

  void entertainMe() {
    if (canPlayPiano) {
      print('Playing piano');
    } else if (canConduct) {
      print('Waving hands');
    } else {
      print('Humming to self');
    }
  }
}
```

Sometimes you might want to restrict the types that can use a mixin. For example, the mixin might depend on being able to invoke a method that the mixin doesn’t define. As the following example shows, you can restrict a mixin’s use by using the `on` keyword to specify the required superclass:

```dart
class Musician {
  // ...
}
mixin MusicalPerformer on Musician {
  // ...
}
class SingerDancer extends Musician with MusicalPerformer {
  // ...
}
```

In the preceding code, only classes that extend or implement the `Musician` class can use the mixin `MusicalPerformer`. Because `SingerDancer` extends `Musician`, `SingerDancer` can mix in `MusicalPerformer`.

### Class variables and methods

Use the `static` keyword to implement class-wide variables and methods.

#### Static variables

Static variables (class variables) are useful for class-wide state and constants:

```dart
class Queue {
  static const initialCapacity = 16;
  // ···
}

void main() {
  assert(Queue.initialCapacity == 16);
}
```

Static variables aren’t initialized until they’re used.

 **Note:** This page follows the [style guide recommendation](https://dart.dev/guides/language/effective-dart/style#identifiers) of preferring `lowerCamelCase` for constant names.

#### Static methods

Static methods (class methods) don’t operate on an instance, and thus don’t have access to `this`. They do, however, have access to static variables. As the following example shows, you invoke static methods directly on a class:

```dart
import 'dart:math';

class Point {
  double x, y;
  Point(this.x, this.y);

  static double distanceBetween(Point a, Point b) {
    var dx = a.x - b.x;
    var dy = a.y - b.y;
    return sqrt(dx * dx + dy * dy);
  }
}

void main() {
  var a = Point(2, 2);
  var b = Point(4, 4);
  var distance = Point.distanceBetween(a, b);
  assert(2.8 < distance && distance < 2.9);
  print(distance);
}
```

 **Note:** Consider using top-level functions, instead of static methods, for common or widely used utilities and functionality.

You can use static methods as compile-time constants. For example, you can pass a static method as a parameter to a constant constructor.

## Generics

If you look at the API documentation for the basic array type, [`List`](https://api.dart.dev/stable/dart-core/List-class.html), you’ll see that the type is actually `List<E>`. The <…> notation marks List as a *generic* (or *parameterized*) type—a type that has formal type parameters. [By convention](https://dart.dev/guides/language/effective-dart/design#do-follow-existing-mnemonic-conventions-when-naming-type-parameters), most type variables have single-letter names, such as E, T, S, K, and V.

### Why use generics?

Generics are often required for type safety, but they have more benefits than just allowing your code to run:

- Properly specifying generic types results in better generated code.
- You can use generics to reduce code duplication.

If you intend for a list to contain only strings, you can declare it as `List<String>` (read that as “list of string”). That way you, your fellow programmers, and your tools can detect that assigning a non-string to the list is probably a mistake. Here’s an example:

```
var names = <String>[];
names.addAll(['Seth', 'Kathy', 'Lars']);
names.add(42); // Error
```

Another reason for using generics is to reduce code duplication. Generics let you share a single interface and implementation between many types, while still taking advantage of static analysis. For example, say you create an interface for caching an object:

```dart
abstract class ObjectCache {
  Object getByKey(String key);
  void setByKey(String key, Object value);
}
```

You discover that you want a string-specific version of this interface, so you create another interface:

```dart
abstract class StringCache {
  String getByKey(String key);
  void setByKey(String key, String value);
}
```

Later, you decide you want a number-specific version of this interface… You get the idea.

Generic types can save you the trouble of creating all these interfaces. Instead, you can create a single interface that takes a type parameter:

```dart
abstract class Cache<T> {
  T getByKey(String key);
  void setByKey(String key, T value);
}
```

In this code, T is the stand-in type. It’s a placeholder that you can think of as a type that a developer will define later.

### Using collection literals

List, set, and map literals can be parameterized. Parameterized literals are just like the literals you’ve already seen, except that you add `<*type*>` (for lists and sets) or `<*keyType*, *valueType*>` (for maps) before the opening bracket. Here is an example of using typed literals:

```dart
var names = <String>['Seth', 'Kathy', 'Lars'];
var uniqueNames = <String>{'Seth', 'Kathy', 'Lars'};
var pages = <String, String>{
  'index.html': 'Homepage',
  'robots.txt': 'Hints for web robots',
  'humans.txt': 'We are people, not machines'
};
```

### Using parameterized types with constructors

To specify one or more types when using a constructor, put the types in angle brackets (`<...>`) just after the class name. For example:

```dart
var nameSet = Set<String>.from(names);
```

The following code creates a map that has integer keys and values of type View:

```dart
var views = Map<int, View>();
```

### Generic collections and the types they contain

Dart generic types are *reified*, which means that they carry their type information around at runtime. For example, you can test the type of a collection:

```dart
var names = <String>[];
names.addAll(['Seth', 'Kathy', 'Lars']);
print(names is List<String>); // true
```

 **Note:** In contrast, generics in Java use *erasure*, which means that generic type parameters are removed at runtime. In Java, you can test whether an object is a List, but you can’t test whether it’s a `List<String>`.

### Restricting the parameterized type

When implementing a generic type, you might want to limit the types of its parameters. You can do this using `extends`.

```dart
class Foo<T extends SomeBaseClass> {
  // Implementation goes here...
  String toString() => "Instance of 'Foo<$T>'";
}

class Extender extends SomeBaseClass {...}
```

It’s OK to use `SomeBaseClass` or any of its subclasses as generic argument:

```dart
var someBaseClassFoo = Foo<SomeBaseClass>();
var extenderFoo = Foo<Extender>();
```

It’s also OK to specify no generic argument:

```dart
var foo = Foo();
print(foo); // Instance of 'Foo<SomeBaseClass>'
```

Specifying any non-`SomeBaseClass` type results in an error:

```dart
var foo = Foo<Object>();
```

### Using generic methods

Initially, Dart’s generic support was limited to classes. A newer syntax, called *generic methods*, allows type arguments on methods and functions:

```dart
T first<T>(List<T> ts) {
  // Do some initial work or error checking, then...
  T tmp = ts[0];
  // Do some additional checking or processing...
  return tmp;
}
```

Here the generic type parameter on `first` (`<T>`) allows you to use the type argument `T` in several places:

- In the function’s return type (`T`).
- In the type of an argument (`List<T>`).
- In the type of a local variable (`T tmp`).

## Libraries and visibility

The `import` and `library` directives can help you create a modular and shareable code base. Libraries not only provide APIs, but are a unit of privacy: identifiers that start with an underscore (`_`) are visible only inside the library. *Every Dart app is a library*, even if it doesn’t use a `library` directive.

Libraries can be distributed using [packages](https://dart.dev/guides/packages).

 If you’re curious why Dart uses underscores instead of access modifier keywords like `public` or `private`, see [SDK issue 33383](https://github.com/dart-lang/sdk/issues/33383).

### Using libraries

Use `import` to specify how a namespace from one library is used in the scope of another library.

For example, Dart web apps generally use the [dart:html](https://api.dart.dev/stable/dart-html) library, which they can import like this:

```dart
import 'dart:html';
```

The only required argument to `import` is a URI specifying the library. For built-in libraries, the URI has the special `dart:` scheme. For other libraries, you can use a file system path or the `package:` scheme. The `package:` scheme specifies libraries provided by a package manager such as the pub tool. For example:

```dart
import 'package:test/test.dart';
```

 **Note:** *URI* stands for uniform resource identifier. *URLs* (uniform resource locators) are a common kind of URI.

#### Specifying a library prefix

If you import two libraries that have conflicting identifiers, then you can specify a prefix for one or both libraries. For example, if library1 and library2 both have an Element class, then you might have code like this:

```dart
import 'package:lib1/lib1.dart';
import 'package:lib2/lib2.dart' as lib2;

// Uses Element from lib1.
Element element1 = Element();

// Uses Element from lib2.
lib2.Element element2 = lib2.Element();
```

#### Importing only part of a library

If you want to use only part of a library, you can selectively import the library. For example:

```dart
// Import only foo.
import 'package:lib1/lib1.dart' show foo;

// Import all names EXCEPT foo.
import 'package:lib2/lib2.dart' hide foo;
```



#### Lazily loading a library

*Deferred loading* (also called *lazy loading*) allows a web app to load a library on demand, if and when the library is needed. Here are some cases when you might use deferred loading:

- To reduce a web app’s initial startup time.
- To perform A/B testing—trying out alternative implementations of an algorithm, for example.
- To load rarely used functionality, such as optional screens and dialogs.

 **Only dart2js supports deferred loading.** Flutter, the Dart VM, and dartdevc don’t support deferred loading. For more information, see [issue #33118](https://github.com/dart-lang/sdk/issues/33118) and [issue #27776.](https://github.com/dart-lang/sdk/issues/27776)

To lazily load a library, you must first import it using `deferred as`.

```dart
import 'package:greetings/hello.dart' deferred as hello;
```

When you need the library, invoke `loadLibrary()` using the library’s identifier.

```dart
Future<void> greet() async {
  await hello.loadLibrary();
  hello.printGreeting();
}
```

In the preceding code, the `await` keyword pauses execution until the library is loaded. For more information about `async` and `await`, see [asynchrony support](https://dart.dev/guides/language/language-tour#asynchrony-support).

You can invoke `loadLibrary()` multiple times on a library without problems. The library is loaded only once.

Keep in mind the following when you use deferred loading:

- A deferred library’s constants aren’t constants in the importing file. Remember, these constants don’t exist until the deferred library is loaded.
- You can’t use types from a deferred library in the importing file. Instead, consider moving interface types to a library imported by both the deferred library and the importing file.
- Dart implicitly inserts `loadLibrary()` into the namespace that you define using `deferred as *namespace*`. The `loadLibrary()` function returns a [`Future`](https://dart.dev/guides/libraries/library-tour#future).

### Implementing libraries

See [Create Library Packages](https://dart.dev/guides/libraries/create-library-packages) for advice on how to implement a library package, including:

- How to organize library source code.
- How to use the `export` directive.
- When to use the `part` directive.
- When to use the `library` directive.
- How to use conditional imports and exports to implement a library that supports multiple platforms.



## Asynchrony support

Dart libraries are full of functions that return [`Future`](https://api.dart.dev/stable/dart-async/Future-class.html) or [`Stream`](https://api.dart.dev/stable/dart-async/Stream-class.html) objects. These functions are *asynchronous*: they return after setting up a possibly time-consuming operation (such as I/O), without waiting for that operation to complete.

The `async` and `await` keywords support asynchronous programming, letting you write asynchronous code that looks similar to synchronous code.



### Handling Futures

When you need the result of a completed Future, you have two options:

- Use `async` and `await`.
- Use the Future API, as described [in the library tour](https://dart.dev/guides/libraries/library-tour#future).

Code that uses `async` and `await` is asynchronous, but it looks a lot like synchronous code. For example, here’s some code that uses `await` to wait for the result of an asynchronous function:

```dart
await lookUpVersion();
```

To use `await`, code must be in an `async` function—a function marked as `async`:

```dart
Future<void> checkVersion() async {
  var version = await lookUpVersion();
  // Do something with version
}
```

 **Note:** Although an `async` function might perform time-consuming operations, it doesn’t wait for those operations. Instead, the `async` function executes only until it encounters its first `await` expression ([details](https://github.com/dart-lang/sdk/blob/master/docs/newsletter/20170915.md#synchronous-async-start)). Then it returns a Future object, resuming execution only after the `await` expression completes.

Use `try`, `catch`, and `finally` to handle errors and cleanup in code that uses `await`:

```dart
try {
  version = await lookUpVersion();
} catch (e) {
  // React to inability to look up the version
}
```

You can use `await` multiple times in an `async` function. For example, the following code waits three times for the results of functions:

```dart
var entrypoint = await findEntryPoint();
var exitCode = await runExecutable(entrypoint, args);
await flushThenExit(exitCode);
```

In `await *expression*`, the value of `*expression*` is usually a Future; if it isn’t, then the value is automatically wrapped in a Future. This Future object indicates a promise to return an object. The value of `await *expression*` is that returned object. The await expression makes execution pause until that object is available.

**If you get a compile-time error when using `await`, make sure `await` is in an `async` function.** For example, to use `await` in your app’s `main()` function, the body of `main()` must be marked as `async`:

```dart
Future<void> main() async {
  checkVersion();
  print('In main: version is ${await lookUpVersion()}');
}
```



### Declaring async functions

An `async` function is a function whose body is marked with the `async` modifier.

Adding the `async` keyword to a function makes it return a Future. For example, consider this synchronous function, which returns a String:

```dart
String lookUpVersion() => '1.0.0';
```

If you change it to be an `async` function—for example, because a future implementation will be time consuming—the returned value is a Future:

```dart
Future<String> lookUpVersion() async => '1.0.0';
```

Note that the function’s body doesn’t need to use the Future API. Dart creates the Future object if necessary. If your function doesn’t return a useful value, make its return type `Future<void>`.

For an interactive introduction to using futures, `async`, and `await`, see the [asynchronous programming codelab](https://dart.dev/codelabs/async-await).



### Handling Streams

When you need to get values from a Stream, you have two options:

- Use `async` and an *asynchronous for loop* (`await for`).
- Use the Stream API, as described [in the library tour](https://dart.dev/guides/libraries/library-tour#stream).

 **Note:** Before using `await for`, be sure that it makes the code clearer and that you really do want to wait for all of the stream’s results. For example, you usually should **not** use `await for` for UI event listeners, because UI frameworks send endless streams of events.

An asynchronous for loop has the following form:

```dart
await for (varOrType identifier in expression) {
  // Executes each time the stream emits a value.
}
```

The value of `*expression*` must have type Stream. Execution proceeds as follows:

1. Wait until the stream emits a value.
2. Execute the body of the for loop, with the variable set to that emitted value.
3. Repeat 1 and 2 until the stream is closed.

To stop listening to the stream, you can use a `break` or `return` statement, which breaks out of the for loop and unsubscribes from the stream.

**If you get a compile-time error when implementing an asynchronous for loop, make sure the `await for` is in an `async` function.** For example, to use an asynchronous for loop in your app’s `main()` function, the body of `main()` must be marked as `async`:

```dart
Future<void> main() async {
  // ...
  await for (var request in requestServer) {
    handleRequest(request);
  }
  // ...
}
```

For more information about asynchronous programming, in general, see the [dart:async](https://dart.dev/guides/libraries/library-tour#dartasync---asynchronous-programming) section of the library tour.



## Generators

When you need to lazily produce a sequence of values, consider using a *generator function*. Dart has built-in support for two kinds of generator functions:

- **Synchronous** generator: Returns an [`Iterable`](https://api.dart.dev/stable/dart-core/Iterable-class.html) object.
- **Asynchronous** generator: Returns a [`Stream`](https://api.dart.dev/stable/dart-async/Stream-class.html) object.

To implement a **synchronous** generator function, mark the function body as `sync*`, and use `yield` statements to deliver values:

```dart
Iterable<int> naturalsTo(int n) sync* {
  int k = 0;
  while (k < n) yield k++;
}
```

To implement an **asynchronous** generator function, mark the function body as `async*`, and use `yield` statements to deliver values:

```dart
Stream<int> asynchronousNaturalsTo(int n) async* {
  int k = 0;
  while (k < n) yield k++;
}
```

If your generator is recursive, you can improve its performance by using `yield*`:

```dart
Iterable<int> naturalsDownFrom(int n) sync* {
  if (n > 0) {
    yield n;
    yield* naturalsDownFrom(n - 1);
  }
}
```

## Callable classes

To allow an instance of your Dart class to be called like a function, implement the `call()` method.

In the following example, the `WannabeFunction` class defines a call() function that takes three strings and concatenates them, separating each with a space, and appending an exclamation. Click **Run** to execute the code.

<iframe src="https://dartpad.dev/embed-dart.html?theme=light&amp;run=dartpad&amp;split=false&amp;ga_id=callable_classes&amp;null_safety=true" style="box-sizing: border-box; border: 1px solid rgb(204, 204, 204); margin-bottom: 1rem; min-height: 400px; resize: vertical; width: 891.273px; height: 350px;"></iframe>

## Isolates

Most computers, even on mobile platforms, have multi-core CPUs. To take advantage of all those cores, developers traditionally use shared-memory threads running concurrently. However, shared-state concurrency is error prone and can lead to complicated code.

Instead of threads, all Dart code runs inside of *isolates*. Each isolate has its own memory heap, ensuring that no isolate’s state is accessible from any other isolate.

For more information, see the following:

- [Dart asynchronous programming: Isolates and event loops](https://medium.com/dartlang/dart-asynchronous-programming-isolates-and-event-loops-bffc3e296a6a)
- [dart:isolate API reference,](https://api.dart.dev/stable/dart-isolate) including [Isolate.spawn()](https://api.dart.dev/stable/dart-isolate/Isolate/spawn.html) and [TransferableTypedData](https://api.dart.dev/stable/dart-isolate/TransferableTypedData-class.html)
- [Background parsing](https://flutter.dev/docs/cookbook/networking/background-parsing) cookbook on the Flutter site
- [Isolate sample app](https://github.com/flutter/samples/tree/master/isolate_example)

## Typedefs

A type alias — often called a *typedef* because it’s declared with the keyword `typedef` — is a concise way to refer to a type. Here’s an example of declaring and using a type alias named `IntList`:

```dart
typedef IntList = List<int>;
IntList il = [1, 2, 3];
```

A type alias can have type parameters:

```dart
typedef ListMapper<X> = Map<X, List<X>>;
Map<String, List<String>> m1 = {}; // Verbose.
ListMapper<String> m2 = {}; // Same thing but shorter and clearer.
```

 **Version note:** Before 2.13, typedefs were restricted to function types. Using the new typedefs requires a [language version](https://dart.dev/guides/language/evolution#language-versioning) of at least 2.13.

We recommend using [inline function types](https://dart.dev/guides/language/effective-dart/design#prefer-inline-function-types-over-typedefs) instead of typedefs for functions, in most situations. However, function typedefs can still be useful:

```dart
typedef Compare<T> = int Function(T a, T b);

int sort(int a, int b) => a - b;

void main() {
  assert(sort is Compare<int>); // True!
}
```

## Metadata

Use metadata to give additional information about your code. A metadata annotation begins with the character `@`, followed by either a reference to a compile-time constant (such as `deprecated`) or a call to a constant constructor.

Three annotations are available to all Dart code: `@Deprecated`, `@deprecated`, and `@override`. For examples of using `@override`, see [Extending a class](https://dart.dev/guides/language/language-tour#extending-a-class). Here’s an example of using the `@Deprecated` annotation:

```dart
class Television {
  /// Use [turnOn] to turn the power on instead.
  @Deprecated('Use turnOn instead')
  void activate() {
    turnOn();
  }

  /// Turns the TV's power on.
  void turnOn() {...}
}
```

You can define your own metadata annotations. Here’s an example of defining a `@Todo` annotation that takes two arguments:

```dart
library todo;

class Todo {
  final String who;
  final String what;

  const Todo(this.who, this.what);
}
```

And here’s an example of using that `@Todo` annotation:

```dart
import 'todo.dart';

@Todo('seth', 'make this do something')
void doSomething() {
  print('do something');
}
```

Metadata can appear before a library, class, typedef, type parameter, constructor, factory, function, field, parameter, or variable declaration and before an import or export directive. You can retrieve metadata at runtime using reflection.

## Comments

Dart supports single-line comments, multi-line comments, and documentation comments.

### Single-line comments

A single-line comment begins with `//`. Everything between `//` and the end of line is ignored by the Dart compiler.

```dart
void main() {
  // TODO: refactor into an AbstractLlamaGreetingFactory?
  print('Welcome to my Llama farm!');
}
```

### Multi-line comments

A multi-line comment begins with `/*` and ends with `*/`. Everything between `/*` and `*/` is ignored by the Dart compiler (unless the comment is a documentation comment; see the next section). Multi-line comments can nest.

```dart
void main() {
  /*
   * This is a lot of work. Consider raising chickens.

  Llama larry = Llama();
  larry.feed();
  larry.exercise();
  larry.clean();
   */
}
```

### Documentation comments

Documentation comments are multi-line or single-line comments that begin with `///` or `/**`. Using `///` on consecutive lines has the same effect as a multi-line doc comment.

Inside a documentation comment, the analyzer ignores all text unless it is enclosed in brackets. Using brackets, you can refer to classes, methods, fields, top-level variables, functions, and parameters. The names in brackets are resolved in the lexical scope of the documented program element.

Here is an example of documentation comments with references to other classes and arguments:

```dart
/// A domesticated South American camelid (Lama glama).
///
/// Andean cultures have used llamas as meat and pack
/// animals since pre-Hispanic times.
///
/// Just like any other animal, llamas need to eat,
/// so don't forget to [feed] them some [Food].
class Llama {
  String? name;

  /// Feeds your llama [food].
  ///
  /// The typical llama eats one bale of hay per week.
  void feed(Food food) {
    // ...
  }

  /// Exercises your llama with an [activity] for
  /// [timeLimit] minutes.
  void exercise(Activity activity, int timeLimit) {
    // ...
  }
}
```

In the class’s generated documentation, `[feed]` becomes a link to the docs for the `feed` method, and `[Food]` becomes a link to the docs for the `Food` class.

To parse Dart code and generate HTML documentation, you can use Dart’s [documentation generation tool, dartdoc.](https://dart.dev/tools/dartdoc) For an example of generated documentation, see the [Dart API documentation.](https://api.dart.dev/stable) For advice on how to structure your comments, see [Guidelines for Dart Doc Comments.](https://dart.dev/guides/language/effective-dart/documentation)

## Summary

This page summarized the commonly used features in the Dart language. More features are being implemented, but we expect that they won’t break existing code. For more information, see the [Dart language specification](https://dart.dev/guides/language/spec) and [Effective Dart](https://dart.dev/guides/language/effective-dart).

To learn more about Dart’s core libraries, see [A Tour of the Dart Libraries](https://dart.dev/guides/libraries/library-tour).