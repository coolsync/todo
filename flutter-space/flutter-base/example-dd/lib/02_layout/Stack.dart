import 'package:flutter/material.dart';

class Home extends StatelessWidget {
  const Home({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Stack Demo'),
        leading: Icon(Icons.menu),
        actions: [Icon(Icons.settings)],
        centerTitle: true,
        elevation: 0.0,
      ),
      body: StackShow(),
    );
  }
}

class StackShow extends StatelessWidget {
  const StackShow({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Container(
      child: Stack(
        textDirection: TextDirection.rtl,
        alignment: AlignmentDirectional.bottomEnd,
        children: [
          CircleAvatar(
            backgroundImage: NetworkImage(
                'http://www.yymeitu.com/upload/54243/2019/10-31/20191031204955_8356sxediytv_small.jpg'),
            radius: 200,
          ),
          Positioned(
            child: Container(
              color: Colors.red,
              padding: EdgeInsets.all(10),
              child: Text(
                '热图',
                style: TextStyle(color: Colors.white, fontSize: 30),
              ),
            ),
            top: 200,
            right: 20,
          ),
          Text(
            'HELLO',
            style: TextStyle(color: Colors.black, fontSize: 30),
          ),
        ],
      ),
    );
  }
}
