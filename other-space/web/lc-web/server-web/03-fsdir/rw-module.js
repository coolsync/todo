let fs = require('fs')

function fsRead(path) {
    return new Promise((resolve, reject) => {
        fs.readFile(path, { flag: 'r', encoding: 'utf8' }, (err, data) => {
            if (err) {
                reject(err)
                // console.log(err);
            } else {
                resolve(data)
                // console.log(data);
            }
        })
    })
}

function fsWrite(path, content) {
    return new Promise((resolve, reject) => {
        fs.writeFile(path, content, { flag: 'a', encoding: 'utf8' }, (err) => {
            if (err) {
                reject(err)
            } else {
                resolve(err)
            }
        })
    })
}

module.exports = {fsRead, fsWrite}