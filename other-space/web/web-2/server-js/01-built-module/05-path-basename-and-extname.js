const path = require('path');


const file_path = '/a/b/c/index.html';

// basename
let file_name = path.basename(file_path)
console.log(file_name); // index.html

const name_no_suffiex = path.basename(file_path, '.html')
console.log(name_no_suffiex);   // index

// extname
let file_ext = path.extname(file_path);

console.log(file_ext);  // .html