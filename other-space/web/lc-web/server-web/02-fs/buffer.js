// str conv buffer obj

let str = 'hello'

let buf = Buffer.from(str)

console.log(buf)    // <Buffer 68 65 6c 6c 6f>

console.log(buf.toString());

// alloc new memery space
let buf1 = Buffer.alloc(10)
buf1[0] = 255
console.log(buf1)


let buf2 = Buffer.allocUnsafe(10)
console.log(buf2);