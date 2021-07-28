let data = {name: 'bob', age: 18}   // replace 替换成data 的值

let s1 = '<div>{{name}}, {{ age }}</div>'

let regObj = /{{\s*([a-zA-Z]+)\s*}}/

let result = null

while (result = regObj.exec(s1)) {
    // s1 = s1.replace(result[0], result[1])
    s1 = s1.replace(result[0], data[result[1]])
}

console.log(s1)