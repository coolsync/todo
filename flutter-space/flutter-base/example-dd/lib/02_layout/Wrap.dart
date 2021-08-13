import 'package:flutter/material.dart';

class Home extends StatelessWidget {
  const Home({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Wrap Demo'),
        leading: Icon(Icons.menu),
        actions: [Icon(Icons.settings)],
        centerTitle: true,
        elevation: 0.0,
      ),
      body: WrapShow(),
    );
  }
}

class WrapShow extends StatelessWidget {
  List<String> _list = ['孙权', '孙策', '周瑜', '鲁肃', '陆逊', '小乔', '张城'];

  List<Widget> _wuGuo() {
    return _list
        .map(
          // Iterable type
          (item) => Chip(
              avatar: CircleAvatar(
                backgroundColor: Colors.green,
                child: Text('吴'),
              ),
              label: Text(item)),
        )
        .toList(); // convet List type
  }

  @override
  Widget build(BuildContext context) {
    return Column(
      mainAxisAlignment: MainAxisAlignment.spaceEvenly,
      children: [
        Wrap(
          children: _wuGuo(),
          // main axis direction
          spacing: 18,
          alignment: WrapAlignment.spaceEvenly,
          // cross axis direction
          runSpacing: 100,
          runAlignment: WrapAlignment.spaceAround,
        ),
        Wrap(
          children: [
            Chip(
                avatar: CircleAvatar(
                  backgroundColor: Colors.blue,
                  child: Text('汉'),
                ),
                label: Text('刘备')),
            Chip(
                avatar: CircleAvatar(
                  backgroundColor: Colors.blue,
                  child: Text('汉'),
                ),
                label: Text('关羽')),
            Chip(
                avatar: CircleAvatar(
                  backgroundColor: Colors.blue,
                  child: Text('汉'),
                ),
                label: Text('张飞')),
            Chip(
                avatar: CircleAvatar(
                  backgroundColor: Colors.blue,
                  child: Text('汉'),
                ),
                label: Text('赵云')),
            Chip(
                avatar: CircleAvatar(
                  backgroundColor: Colors.blue,
                  child: Text('汉'),
                ),
                label: Text('主课娘')),
            Chip(
                avatar: CircleAvatar(
                  backgroundColor: Colors.blue,
                  child: Text('汉'),
                ),
                label: Text('黄忠')),
          ],
        ),
      ],
    );
  }
}
