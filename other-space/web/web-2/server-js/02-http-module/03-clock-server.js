const http = require('http');
const fs = require('fs');
const path = require('path');

const server = http.createServer();

server.on('request', (req, res) => {

    const url = req.url;

    let file_path = '';

    if (url === '/') {
        file_path = path.join(__dirname, './clock/index.html')
    } else {
        file_path = path.join(__dirname, './clock' + url)
    }

    fs.readFile(file_path, 'utf-8', (err, data) => {
        if (err) {
            return res.end('404 NOT FOUND')
        }
        // not work, future checkout
        // res.setHeader('Content-Type', 'text/html, charset=utf-8')

        res.end(data)
    })
})

server.listen(8081, () => {
    console.log('server running at http://localhost:8081');
})
