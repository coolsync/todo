const path = require('path');

const pathname = path.join('/a', '/b/c', '../', '/d', 'e')
console.log(pathname);

const pathname2 = path.join(__dirname, './files/2.txt')
console.log(pathname2); // 当前所处目录 + /files/2.txt
