$(function () {
    // 初始化右侧滚动条
    // 这个方法定义在scroll.js中
    resetui()

    // 将用户输入的内容渲染到聊天窗口
    // send btn bind mouce click evt
    $('#btn-send').on('click', () => {
        let text = $('#ipt').val().trim();
        if (text.length <= 0) {
            return $('#ipt').val('');
        }

        // input content to chat window
        $('#talk_list').append('<li class="right_word"><img src="img/person02.png" /> <span>' + text + '</span></li>');

        resetui();
        $('#ipt').val('');

        getMsg(text);
    })

    // get chatbot back send msg
    function getMsg(text) {
        $.ajax({
            method: 'GET',
            url: 'http://www.liulongbin.top:3006/api/robot',
            data: {
                spoken: text,
            },
            success: (res) => {
                // console.log(res);
                if (res.message === 'success') {
                    let msg = res.data.info.text;
                    $('#talk_list').append('<li class="left_word"><img src="img/person01.png" /> <span>' + msg + ' </span></li>');
                    resetui();

                    getVoice(msg);
                }
            }
        })
    }


    // text conv voice func
    function getVoice(text) {
        $.ajax({
            method: 'GET',
            url: 'http://www.liulongbin.top:3006/api/synthesize',
            data: {
                text: text,
            },
            success: (res) => {
                // console.log(res);
                if (res.status === 200) {
                    $('#voice').attr('src', res.voiceUrl);
                }
            }
        })
    }

    // get user enter key
    $('#ipt').on('keyup', (e)=>{
        // console.log(e.keyCode);
        if (e.keyCode === 13) {
            $('#btn-send').click();
        }
    }) 
})