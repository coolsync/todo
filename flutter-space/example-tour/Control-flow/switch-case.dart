void main(List<String> args) {
  var command = 'OPEN';

  switch (command) {
    case 'CLOSE':
      print('CLOSE...');
      break;
    case 'OPEN':
      print('OPEN');
      break;
    default:
      print('default...');
  }
}
