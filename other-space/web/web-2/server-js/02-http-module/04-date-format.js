// formate date method
function dateFormat(dtStr) {
    let dt = new Date(dtStr);

    let y = dt.getFullYear();
    let m = padZero(dt.getMonth() + 1);
    let d = padZero(dt.getDate());

    let hh = padZero(dt.getHours())
    let mm = padZero(dt.getMinutes())
    let ss = padZero(dt.getSeconds())

    return `${y}-${m}-${d} ${hh}:${mm}:${ss}`
}

function padZero(n){
    return n > 9 ? n : '0' + n 
}

module.exports = {
    dateFormat
}