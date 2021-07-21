// 1. import module, create reg, pattern css, js
const fs = require('fs');
const path = require('path');

const reg_style = /<style>[\s\S]*<\/style>/

const reg_js = /<script>[\s\S]*<\/script>/

// 2. read index.html file, get html str
fs.readFile(path.join(__dirname, '../material/index.html'), 'utf8', (err, html_str) => {
    if (err) return console.log('read html file failed!' + err.message);

    // console.log(html_str);

    resolve_css(html_str)

    resolve_js(html_str)

    resolve_html(html_str)
})

// 3. parse css
function resolve_css(htmlStr) {
    const r1 = reg_style.exec(htmlStr);

    // console.log(r1);

    // get pattern data
    const new_css = r1[0].replace('<style>', '').replace('</style>', '')

    // console.log(new_css);
    fs.writeFile(path.join(__dirname, './clock/index.css'), new_css, err =>{
        if (err) return console.log('Write css file failed!' + err.message);

        console.log('Write CSS OK!');
    })
}

// 4 parse js 
function resolve_js(htmlStr) {
    const r2 = reg_js.exec(htmlStr);

    // get pattern data
    const new_js = r2[0].replace('<script>', '').replace('</script>', '')
    // console.log(new_js);
    fs.writeFile(path.join(__dirname, './clock/index.js'), new_js, err =>{
        if (err) return console.log('Write JS failed!' + err.message);

        console.log('Write JS OK!');
    })
}

// 5 parse html file
function resolve_html(html_str) {
    
    let new_html = html_str.replace(reg_style, '<link rel="stylesheet" href="./index.css">')
    .replace(reg_js, '<script src="./index.js"></script>')

    // console.log(new_html);
    fs.writeFile(path.join(__dirname, './clock/index.html'), new_html, err=>{
        if (err) return console.log('Write HTML failed!' + err.message);

        console.log('Write HTML OK!');

    })
}