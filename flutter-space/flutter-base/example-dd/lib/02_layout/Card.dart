import 'package:flutter/material.dart';

class Home extends StatelessWidget {
  const Home({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Card Demo'),
        leading: Icon(Icons.menu),
        actions: [Icon(Icons.settings)],
        centerTitle: true,
        elevation: 0.0,
      ),
      body: CardShow(),
    );
  }
}

class CardShow extends StatelessWidget {
  const CardShow({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        Card(
          margin: EdgeInsets.all(30),
          color: Colors.lightBlue[100],
          shadowColor: Colors.yellow,
          elevation: 20,
          shape: RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(30),
              side: BorderSide(
                color: Colors.yellow,
                width: 3,
              )),
          child: Column(
            children: [
              ListTile(
                leading: Icon(
                  Icons.verified_user_sharp,
                  size: 30,
                ),
                title: Text(
                  'Bob',
                  style: TextStyle(
                    fontSize: 50,
                  ),
                ),
                subtitle: Text(
                  '支持经理',
                  style: TextStyle(
                    fontSize: 30,
                  ),
                ),
              ),
              ListTile(
                title: Text(
                  'Phone: 134599999',
                  style: TextStyle(
                    fontSize: 20,
                  ),
                ),
              ),
              ListTile(
                title: Text(
                  'Addr: XXXXXXXXX',
                  style: TextStyle(
                    fontSize: 20,
                  ),
                ),
              ),
            ],
          ),
        ),
        Card(
          child: Column(
            children: [
              ListTile(
                leading: Icon(
                  Icons.verified_user_sharp,
                  size: 30,
                ),
                title: Text(
                  'Paul',
                  style: TextStyle(
                    fontSize: 50,
                  ),
                ),
                subtitle: Text(
                  '工程经理',
                  style: TextStyle(
                    fontSize: 30,
                  ),
                ),
              ),
              ListTile(
                title: Text(
                  'Phone: 134599999',
                  style: TextStyle(
                    fontSize: 20,
                  ),
                ),
              ),
              ListTile(
                title: Text(
                  'Addr: XXXXXXXXX',
                  style: TextStyle(
                    fontSize: 20,
                  ),
                ),
              ),
            ],
          ),
        ),
      ],
    );
  }
}
