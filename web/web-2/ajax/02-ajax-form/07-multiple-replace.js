let s1 = '<div>I am {{name}}, Age is {{ age }}</div>'

let regObj = /{{\s*([a-zA-Z]+)\s*}}/        // \s* 消除多个空白char

let r1 = regObj.exec(s1) // regObj pattern s1

// 第一次匹配
s1 = s1.replace(r1[0], r1[1])
console.log(s1) // <div>I am name, Age is {{age}}</div>

// 第二次匹配
r1 = regObj.exec(s1)
s1 = s1.replace(r1[0], r1[1])   
console.log(s1) //<div>I am name, Age is age</div>

// 第三次匹配
r1 = regObj.exec(s1)
s1 = s1.replace(r1[0], r1[1])   
console.log(s1) //TypeError: Cannot read property '0' of null

