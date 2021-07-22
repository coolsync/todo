let a = 123;
let b = 456;
let c = 789;
let s1 = {username: 'employee'};
console.log(s1);

exports.a = a;

module.exports.c = c;

// module.exports = {name: 'bob'};
module.exports = s1;
