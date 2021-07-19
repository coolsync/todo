let fs = require('fs');

// fs.writeFile('write.txt', '今晚 aready eat!\n', {flag: 'w', encoding: 'utf8'}, (err)=>{
//     if (err){
//         console.log('write file failed!');
//     } else {
//         console.log('ok');
//     }
// })

function writefs(path, content) {
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

// async function writeList() {
//     await writefs('eat.txt', '吃了吗\n')
//     await writefs('eat.txt', '吃了吗\n')
//     await writefs('eat.txt', '吃了吗\n')
// }

async function writeList() {
    await writefs('eat.html', '<h1>吃了吗</h1>')
    await writefs('eat.html', '<h1>吃了吗</h1>')
    await writefs('eat.html', '<h1>吃了吗</h1>')
}

writeList();