// get cmt list
function getCmtList() {
    $.ajax({
        method: 'GET',
        url: 'http://www.liulongbin.top:3006/api/cmtlist',
        success: (res) => {
            if (res.status !== 200) return alert('get data failed!');

            let rows = [];

            $.each(res.data, (i, item) => {
                let str = '<li class="list-group-item"><span class="badge" style="background-color:blue;">comment time: ' + item.time + '</span><span class="badge" style="background-color: fuchsia;">comment person:' + item.username + '</span>' + item.content + '</li>'
                rows.push(str)
            })

            $('#cmt-list').empty().append(rows.join(''));
        }
    })
}

getCmtList();

// post cmt
$(() => {
    $('#addcmt').submit((e) => {
        e.preventDefault();
        let data = $('#addcmt').serialize();
        // console.log(data);
        $.post('http://www.liulongbin.top:3006/api/addcmt', data, (res) => {
            // console.log(res)
            if (res.status != 201) return alert('add cmt failed!');

            getCmtList();

            $('#addcmt')[0].reset() // conv dom obj, and reset form cont
        })
    })
})