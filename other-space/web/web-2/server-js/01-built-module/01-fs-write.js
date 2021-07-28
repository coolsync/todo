// import fs module
const fs = require('fs')

// call fs.writeFile method, finish writer
// fs.writeFile('./files/2.txt', 'hello, es', (err)=>{
fs.writeFile('f:/files/2.txt', 'hello, es', (err)=>{

    if(err) {
        console.log('ERR INFO: ', err.message)
    }
    
    console.log('Write OK!')
})