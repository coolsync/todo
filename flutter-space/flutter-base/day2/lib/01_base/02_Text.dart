import 'package:flutter/material.dart';

class Home extends StatelessWidget {
  const Home({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('首页'),
        leading: Icon(Icons.menu),
        actions: [Icon(Icons.settings)],
        centerTitle: true,
        elevation: 0.0,
      ),
      body: TextShow(),
    );
  }
}

class TextShow extends StatelessWidget {
  const TextShow({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        Text(
          "Flutter 是 Google 开源的 UI 工具包，帮助开发者通过一套代码库高效构建多平台精美应用，支持移动、Web、桌面和嵌入式平台。",
          textDirection: TextDirection.ltr,
          style: TextStyle(
            fontSize: 30,
            color: Colors.red,
            fontWeight: FontWeight.w500,
            fontStyle: FontStyle.italic,
            decoration: TextDecoration.underline,
            decorationColor: Colors.blue[200],
            fontFamily: 'CascadiaCode',
          ),
          textAlign: TextAlign.left,
          maxLines: 3,
          overflow: TextOverflow.ellipsis,
          textScaleFactor: 1.5, // 40
        ),
        RichText(
          text: TextSpan(
              text: 'Hello',
              style: TextStyle(
                fontSize: 40,
                color: Color.fromARGB(255, 0, 0, 255),
              ),
              children: [
                TextSpan(
                    text: 'Flutter',
                    style: TextStyle(
                        fontSize: 40, color: Color.fromRGBO(255, 0, 255, 0.5))),
                TextSpan(
                    text: '青凤古剑',
                    style: TextStyle(
                        fontSize: 40,
                        color: Color.fromARGB(0xFF, 0x00, 0xFF, 0x00)))
              ]),
        ),
      ],
    );
  }
}
