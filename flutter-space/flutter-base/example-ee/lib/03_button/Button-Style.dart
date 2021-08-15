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
              child: Text('OutlinedButton')),
          // Button Setting
          OutlinedButton(
            onPressed: () {
              print('Click OutlinedButton');
            },
            onLongPress: () {
              print('长按 OutlinedButton');
            },
            child: Text('Outlined(轮廓)Button'),
            style: ButtonStyle(
                textStyle: MaterialStateProperty.all(TextStyle(fontSize: 30)),
                foregroundColor: MaterialStateProperty.resolveWith((states) {
                  if (states.contains(MaterialState.pressed)) {
                    return Colors.red;
                  }
                  return Colors.blue;
                }),
                backgroundColor: MaterialStateProperty.resolveWith((states) {
                  if (states.contains(MaterialState.pressed)) {
                    return Colors.yellow;
                  }
                  return Colors.white;
                }),
                shadowColor: MaterialStateProperty.all(Colors.purple),
                elevation: MaterialStateProperty.all(10),
                side: MaterialStateProperty.all(BorderSide(
                  color: Colors.green,
                  width: 2,
                )),
                shape: MaterialStateProperty.all(StadiumBorder(
                  side: BorderSide(
                    color: Colors.black,
                    width: 3,
                  ),
                )),
                minimumSize: MaterialStateProperty.all(Size(200, 100)),
                overlayColor: MaterialStateProperty.all(Colors.cyanAccent)),
          ),
        ],
      ),
    );
  }
}
