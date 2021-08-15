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
      floatingActionButton: FloatingActionButton(
        onPressed: () {},
        tooltip: 'Increment',
        child: Icon(Icons.add),
        backgroundColor: Colors.green,
        elevation: 0.0,
      ),
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
          OutlinedButtonTheme(
            data: OutlinedButtonThemeData(
                style: ButtonStyle(
                    overlayColor: MaterialStateProperty.all(Colors.yellow))),
            child: OutlinedButton(
              onPressed: () {
                print('Click Pressed');
              },
              onLongPress: () {
                print('长按 OutlinedButton');
              },
              child: Text('Outlined Button'),
              style: ButtonStyle(
                  overlayColor: MaterialStateProperty.all(Colors.red)),
            ),
          ),
          // ------------ Button Icons ------------
          IconButton(
            onPressed: () {
              print('Icon Button');
            },
            icon: Icon(Icons.ac_unit_rounded),
            color: Colors.pink,
            highlightColor: Colors.blue,
            splashColor: Colors.lightGreen,
          ),
          TextButton.icon(
              onPressed: () {},
              icon: Icon(Icons.add_a_photo),
              label: Text('文本 Button')),
          ElevatedButton.icon(
              onPressed: () {},
              icon: Icon(Icons.add_a_photo),
              label: Text('凸起 Button')),
          OutlinedButton.icon(
              onPressed: () {},
              icon: Icon(Icons.add_a_photo),
              label: Text('轮廓 Button')),
          Container(
            color: Colors.pink[100],
            width: double.infinity,
            child: ButtonBar(
              children: [
                ElevatedButton(onPressed: () {}, child: Text('BUTTON 1')),
                ElevatedButton(onPressed: () {}, child: Text('BUTTON 2')),
                ElevatedButton(onPressed: () {}, child: Text('BUTTON 3')),
                ElevatedButton(
                    // this line: cross axis 排布
                    onPressed: () {},
                    child: Text('BUTTON 4')),
              ],
            ),
          ),
          BackButton(
            onPressed: () {},
            color: Colors.red,
          ),
          CloseButton(onPressed: () {}, color: Colors.red),
          // ------------ Button Icons ------------
        ],
      ),
    );
  }
}
