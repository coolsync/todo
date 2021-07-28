let XMLHttpRequest = require('xmlhttprequest').XMLHttpRequest;

let xhr = new XMLHttpRequest();

// set timeout
xhr.timeout = 30

// Set the processing function after the timeout
xhr.ontimeout = ()=>{
    console.log('request timeout!')
}

xhr.open('GET', 'http://www.liulongbin.top:3006/api/getbooks')

xhr.send()

xhr.onreadystatechange = ()=>{
    if (xhr.readyState === 4 && xhr.status === 200) {
        console.log(xhr.responseText)
    }
}

