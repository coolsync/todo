const fs = require('fs');

// fs.readFile('./files/2.txt', { encoding: 'utf8' }, (err, dataStr) => {
//     if (err) {
//         return console.log('read file failed: ' + err.message);
//     }
//     console.log(dataStr);
// })

// __dirname 当前文件所处的目录
fs.readFile(__dirname + '/files/2.txt', { encoding: 'utf8' }, (err, dataStr) => {
    if (err) {
        return console.log('read file failed: ' + err.message);
    }
    console.log(dataStr);
})