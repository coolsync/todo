// 1 import fs
// 2 read file
// 3 handle file content
// 4 write to new file

const fs = require('fs');

fs.readFile('./files/score.txt', {encoding: 'utf8', flag: 'r'}, (err, dataStr)=>{
    if (err){
        return console.log('ERR INFO: ', err.message)
    }

    // console.log('OK: ', dataStr)

    // Get old array
    let oldArr = dataStr.split(' ')
    
    let newArr = []

    // for old arr, string replace  '=' --> ':'
    oldArr.forEach(item => {
        newArr.push(item.replace('=', ': '))
    })

    // new arr wrap line, get new string
    let newStr = newArr.join('\n')
    
    fs.writeFile('./files/score-ok.txt', newStr, (err)=>{
        if (err) {
            return console.log('Write Failed!', err.message)
        }
        console.log('Write OK!'
        );
    })
})