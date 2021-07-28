function template(id, data) {
    let str = document.querySelector('#'+id).innerHTML;

    let pattern = /{{\s*([a-zA-Z]+)\s*}}/

    let result = null

    while(result = pattern.exec(str)){
        str = str.replace(result[0], data[result[1]])
    }

    return str
}