// $(() => {
//     function getItList() {
//         $.get('http://www.liulongbin.top:3006/api/news', (res) => {
//             if (res.status !== 200) {
//                 return alert('get it news failed!');
//             }

//             for (let i = 0; i < res.data.length; i++) {
//                 res.data[i].tags = res.data[i].tags.split(',');

//             }
            
//             console.log(res)


//             let htmlStr = template('tpl-list', res);
//             $('#news-list').html(htmlStr);
//         })
//     }

//     getItList();
// })

// 1 get it news list
// 2 def tpl
// 3 compier tpl
// 4 time filter