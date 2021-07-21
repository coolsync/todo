let http = require('http');

http.createServer((req, res) => {
    
    res.writeHead(200, {'Content-Type': 'text/plain'})

    res.end('hello\n');
}).listen(8888)

console.log('server at 127.0.0.1:8888');