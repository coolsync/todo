const http = require('http');

let server = http.createServer();

// listen server request event
server.on('request', (req, res) => {
    let res_str = `Your request URL is: ${req.url}, request method: ${req.method}`

    res.setHeader('Content-Type', 'text/html', 'charset=utf-8');    // 解决中文乱码问题

    res.end(res_str); // send to client content
})

// listen port visit
server.listen(8081, ()=>{
    console.log('server running at http://localhost:8081');
})

