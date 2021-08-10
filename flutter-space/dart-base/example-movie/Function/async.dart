import 'package:http/http.dart' as http;
import 'dart:convert';

// https://httpbin.org/ip   // get ip addr
Future getIPAddress() async {
  final url = Uri.parse('https://httpbin.org/ip');
  final response = await http.get(url);

  var ip = jsonDecode(response.body)['origin'];
  return ip;
}

void main() async {
  try {
    final ip = await getIPAddress();
    print(ip);
  } catch (e) {
    print(e);
  }
}
