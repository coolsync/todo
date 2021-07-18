let a = '<div>i am {{name}}</div>'

let pattern = /{{([a-zA-Z]+)}}/

let r = pattern.exec(a)

a = a.replace(r[0], r[1])

console.log(r);
console.log(a)  // <div>i am name</div>