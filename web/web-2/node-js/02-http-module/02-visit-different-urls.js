const http = require('http');

let server = http.createServer();

server.on('request', (req, res) => {
    const url = req.url;

    let content = '<h1>404 Not Found</h1>'

    if (url === '/' || url === '/index.html') {
        content = '<h1>Index Page 乱码</h1>'
    } else if (url === '/about.html') {
        content = '<h1>About Page</h1>'
    }

    res.setHeader('Content-Type', 'text/html; charset=utf-8');    // 解决中文乱码问题

    res.end(content);
})

server.listen(8081, ()=>{
    console.log('server running at http://localhost:8081');
})