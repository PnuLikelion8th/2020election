function getValue(){
    var sido = document.getElementById("sido");
    var sidoselect = document.getElementById("sidoselect");

    sidoselect.value=sido.value;
};


function candidate_info(name,job){
    document.getElementById('cd_dt_info').innerHTML = "<div>"+name+"후보는 재선 후보에요.</div><br><div>"+
        "직업은" +job+"이구요."+"</div><br><div> 이 후보의 지난 국회 본회의 출석률은 00%에요.</div><br>"
}

function drop_open(){
    if (document.querySelector('.dropdown-content').classList.contains('show')){
        document.querySelector('.dropdown-content').classList.remove('show')

    }else{
        document.querySelector('.dropdown-content').classList.add('show')

    }

}

function open_gugundrop(){
    if (document.querySelector('.dropdown-content2').classList.contains('show')) {
        document.querySelector('.dropdown-content2').classList.remove('show')

    } else {
        document.querySelector('.dropdown-content2').classList.add('show')

    }
}