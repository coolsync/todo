import 'package:flutter/material.dart';

import '01_base/01_Hello.dart';

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
      debugShowCheckedModeBanner: false,
    );
  }
}
