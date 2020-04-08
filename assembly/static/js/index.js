function getValue(){
    var sido = document.getElementById("sido");
    var sidoselect = document.getElementById("sidoselect");

    sidoselect.value=sido.value;
};


function candidate_info(name,job){
    document.getElementById('cd_dt_info').innerHTML = "<div>"+name+"후보는 재선 후보에요.</div><br><div>"+
        "직업은" +job+"이구요."+"</div><br><div> 이 후보의 지난 국회 본회의 출석률은 00%에요.</div><br>"
}