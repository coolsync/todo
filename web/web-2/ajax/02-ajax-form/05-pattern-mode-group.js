let a = '<div>{{name}}</div>'

let reg = /{{([a-zA-Z]+)}}/

let r = reg.exec(a)

console.log(r);


/* 
[
  '{{name}}',
  'name',
  index: 5,
  input: '<div>{{name}}</div>',
  groups: undefined
]
*/