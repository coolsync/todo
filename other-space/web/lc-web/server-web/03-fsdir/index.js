// import { readFile } from 'fs';

let fsDir = require('fs');

let { fsRead, fsWrite } = require('./rw-module')

console.log(fsRead);
const txtPath = './all.txt'

fsDir.readdir('../02-fs', (err, files) => {
    if (err) {
        console.log(err);
    } else {
        //   console.log(data);
        files.forEach(async (filename, i) => {
            let content = await fsRead('../02-fs/' + filename);
            fsWrite(txtPath, content)
        })
    }
});