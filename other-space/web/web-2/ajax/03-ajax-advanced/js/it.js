// conv obj to url query string
function resolveData(data) {
    let arr = []
    
    for (let k in data) {
        // let str = k + '=' + data[k];
        // arr.push(str)
        arr.push(k + '=' + data[k])
    }

    return arr.join('&')
}

// let res = resolveData({"name": "bob", "age": 80})
// console.log(res)

function it(options) {
    let xhr = new XMLHttpRequest();

    let qs = resolveData(options.data);

    if (options.method.toUpperCase() === 'GET') {
        // handle get req
        xhr.open(options.method, options.url + '?' + qs);
        xhr.send();

    } else if (options.method.toUpperCase() === 'POST') {
        // handle post req
        xhr.open(options.method, options.url);
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded')
        xhr.send(qs)
    }

    xhr.onreadystatechange = ()=>{
        if (xhr.readyState === 4 && xhr.status === 200) {
            let res = JSON.parse(xhr.responseText)
            options.success(res)
        }
    }
}