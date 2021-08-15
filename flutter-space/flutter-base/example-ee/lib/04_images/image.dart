import 'package:flutter/material.dart';

class Home extends StatelessWidget {
  const Home({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Image Demo'),
        leading: Icon(Icons.menu),
        actions: [Icon(Icons.settings)],
        elevation: 0.0,
        centerTitle: true,
      ),
      body: ImageShow(),
    );
  }
}

class ImageShow extends StatelessWidget {
  const ImageShow({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        // 加载本地图片
        Image.asset(
          'images/bg1.jpg',
          width: 200,
          height: 200,
          fit: BoxFit.fill,
        ),
        // 加载网洛图片
        Image.network(
          // 'https://oss.suning.com/adpp/creative_kit/material/picture/20210812-3b64a67306234eb1a14117aa357cc2087a48842b0b54481b.png',
          'https://picsum.photos/250?image=9',
          width: 200,
          height: 200,
          repeat: ImageRepeat.repeatY,
          colorBlendMode: BlendMode.colorBurn,
          color: Colors.yellow,
        ),
      ],
    );
  }
}
