import 'package:flutter/material.dart';

class Home extends StatelessWidget {
  const Home({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Column Row Layout'),
        leading: Icon(Icons.menu),
        actions: [Icon(Icons.settings)],
        centerTitle: true,
        elevation: 0.0,
      ),
      body: ColumnRowDemo(),
    );
  }
}

class ColumnRowDemo extends StatelessWidget {
  const ColumnRowDemo({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Container(
      color: Colors.lightGreen,
      width: double.infinity,
      child: Column(
        // 主轴排布
        mainAxisAlignment: MainAxisAlignment.spaceEvenly,
        // 交叉轴排布
        crossAxisAlignment: CrossAxisAlignment.center,
        children: [
          Icon(Icons.access_alarm, size: 50),
          Icon(Icons.account_balance, size: 50),
          Icon(Icons.add_box, size: 50),
          Icon(Icons.anchor_outlined, size: 50),
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceAround,
            children: [
              Icon(Icons.access_alarm, size: 50),
              Icon(Icons.account_balance, size: 50),
              Icon(Icons.add_box, size: 50),
              Icon(Icons.anchor_outlined, size: 50),
            ],
          )
        ],
      ),
    );
  }
}
