import 'package:http/http.dart' as http;
import 'dart:convert';

// https://httpbin.org/ip   // get ip addr
Future getIPAddress() {
  final url = Uri.parse('https://httpbin.org/ip');

  return http.get(url).then((response) {
    var ip = jsonDecode(response.body)['origin'];
    return ip;
  });
}

void main() {
  // get instance
  getIPAddress().then((ip) => print(ip)).catchError((err) => print(err));
}
