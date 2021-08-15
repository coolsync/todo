import 'package:flutter/material.dart';

class Home extends StatelessWidget {
  const Home({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Button Demo'),
        leading: Icon(Icons.menu),
        actions: [Icon(Icons.settings)],
        elevation: 0.0,
        centerTitle: true,
      ),
      body: ButtonShow(),
    );
  }
}

class ButtonShow extends StatelessWidget {
  const ButtonShow({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: EdgeInsets.all(10),
      child: Wrap(
        children: [
          TextButton(
              onPressed: () {
                print('Click TextButton');
              },
              onLongPress: () {
                print('长按 TextButton');
              },
              child: Text(
                'Text Button',
                style: TextStyle(
                  fontSize: 30,
                  color: Colors.red,
                ),
              )),
          ElevatedButton(
              onPressed: () {
                print('Click ElevatedButton');
              },
              onLongPress: () {
                print('长按 ElevatedButton');
              },
              child: Text('ElevatedButton')),
          OutlinedButton(
              onPressed: () {
                print('Click OutlinedButton');
              },
              onLongPress: () {
                print('长按 OutlinedButton');
              },
              child: Text('OutlinedButton'))
        ],
      ),
    );
  }
}
