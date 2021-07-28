const fs = require('fs');

// sync
// let content = fs.readFileSync('hi.txt', {flag: 'r', encoding: 'utf8'})

// console.log(content);

// 异步
// fs.readFile('hi.txt', { flag: 'r', encoding: 'utf8' }, (err, data) => {
//     if (err) {
//         console.log(err);
//     } else {
//         console.log(data);
//     }
//     console.log(456);
// })
// console.log(123);

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

// let f1 = fsRead('hi.txt');

// f1.then((res) => {
//     console.log(res)
// })

async function readList() {
    let f2 = await fsRead('hi.txt')
    // console.log(f2)
    let f3 = await fsRead(f2 + '.txt')
    // console.log(f3)

    let f3Content = await fsRead(f3 + '.txt')
    console.log(f3Content);
}

readList();