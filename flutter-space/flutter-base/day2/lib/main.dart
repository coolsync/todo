import 'package:flutter/material.dart';

// import '01_base/01_Hello.dart';
// import '01_base/02_Text.dart';
import '02_layout/Container.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flluter Show',
      home: Home(),
      // theme: ThemeData(fontFamily: 'CascadiaCode'),
      debugShowCheckedModeBanner: false,
    );
  }
}
