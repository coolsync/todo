// obj conv json
let obj = {'a': 'hello1', 'b': 'hello2'};

let jsonStr = JSON.stringify(obj)

console.log(jsonStr);

// json conv obj
jsonStr2 = '{"a":"hello1","b":"hello2", "c": false}'
let obj2 = JSON.parse(jsonStr2)
console.log(obj2)

