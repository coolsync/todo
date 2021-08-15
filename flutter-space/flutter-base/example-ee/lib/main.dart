import 'package:flutter/material.dart';

// import '03_button/Button.dart';
// import '03_button/Button_Style.dart';
// import '03_button/Button-Theme.dart';
// import '03_button/Button-Icons.dart';
import '04_images/image.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      home: Home(),
      debugShowCheckedModeBanner: false,
    );
  }
}
