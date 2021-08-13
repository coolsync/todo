import 'package:flutter/material.dart';

class Home extends StatelessWidget {
  const Home({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Text'),
        leading: Icon(Icons.menu),
        actions: [Icon(Icons.settings)],
        centerTitle: true,
        elevation: 0.0,
      ),
      body: ContainerDemo(),
    );
  }
}

class ContainerDemo extends StatelessWidget {
  const ContainerDemo({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Container(
      child: Text(
        "Flutter 是 Google 开源的 UI 工具包，帮助开发者通过一套代码库高效构建多平台精美应用，支持移动、Web、桌面和嵌入式平台。",
        style: TextStyle(
          fontSize: 25,
          // color: Colors.blue,
        ),
      ),
      width: 200,
      height: 400,
      // width: double.infinity, // self fit
      // height: double.infinity,
      padding: EdgeInsets.all(10.0),
      margin: EdgeInsets.fromLTRB(10.0, 30.0, 0.0, 5.0),
      alignment: Alignment.center,
      transform: Matrix4.skewX(.2),
      // transform: Matrix4.rotationZ(-0.1),
      // transform: Matrix4.translationValues(100, 0, 0),
      decoration: BoxDecoration(
          //   border: Border(
          //       top: BorderSide(width: 10, color: Colors.red),
          //       bottom: BorderSide(width: 10, color: Colors.red),
          //       right: BorderSide(width: 10, color: Colors.red),
          //       left: BorderSide(width: 10, color: Colors.red)),
          // ),
          border: Border.all(width: 10, color: Colors.blue),
          // borderRadius: BorderRadius.all(Radius.circular(30)),
          borderRadius: BorderRadius.only(
            topLeft: Radius.circular(30),
          ),
          color: Colors.lightBlue[200],
          gradient: LinearGradient(colors: [Colors.lightBlue, Colors.white12])),
    );
  }
}
