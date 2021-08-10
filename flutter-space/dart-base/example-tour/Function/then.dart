import 'dart:convert';

import 'package:http/http.dart' as http;

Future getIpAddress() {
  final url = Uri.parse('https://httpbin.org/ip');

  return http.get(url).then((value) {
    var ip = jsonDecode(value.body)['origin'];
    return ip;
  });
}

void main() {
  getIpAddress().then((ip) => print(ip)).catchError((err) => print(err));
}
