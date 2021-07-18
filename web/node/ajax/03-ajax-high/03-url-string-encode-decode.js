let str = '使用好编辑器很重要'

let encode_str = encodeURI(str)

console.log(encode_str)

console.log('------------');

let decode_str = decodeURI('%E4%BD%BF%E7%94%A8')

console.log(decode_str)