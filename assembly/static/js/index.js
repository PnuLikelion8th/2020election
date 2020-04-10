function getValue(){
    var sido = document.getElementById("sido");
    var sidoselect = document.getElementById("sidoselect");

    sidoselect.value=sido.value;
};


function candidate_info(name,job){
    document.getElementById('cd_dt_info').innerHTML = "<div>"+name+"후보는 재선 후보에요.</div><br><div>"+
        "직업은" +job+"이구요."+"</div><br><div> 이 후보의 지난 국회 본회의 출석률은 00%에요.</div><br>";
    document.querySelector('.show_info').style.display="block"


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

function x_btn(){
    document.querySelector('.x_btn').parentElement.style.display="none";
}



// window.onload = () =>{
//     const buttons = document.querySelectorAll('.choice_type');
//     for (let i=0; i<buttons.length; i++){
//         buttons[i].addEventListener("click",function(){
//             this.style.background="buttonface";
//             // this.style.background="black";
//         })
//     }
// }


function chocie_check(e){
    
    const button1 = document.querySelector('.choice_type1');
    const button2 = document.querySelector('.choice_type2');
    const button3 = document.querySelector('.choice_type3');
    const button4 = document.querySelector('.choice_type4');
    const button5 = document.querySelector('.choice_type5');
    const button6 = document.querySelector('.choice_type6');
    
    
    //init
    button1.style.boxShadow=""
    button2.style.boxShadow=""
    button3.style.boxShadow=""
    button4.style.boxShadow=""
    button5.style.boxShadow=""
    button6.style.boxShadow=""

    const makeshadow = "0 0px 10px 6px rgba(0,0,0,0.4)"
    

    if (e.target === button1){
        e.target.style.boxShadow = makeshadow;
    } if (e.target === button2){
        e.target.style.boxShadow = makeshadow;
    } if (e.target === button3){
        e.target.style.boxShadow = makeshadow;
    } if (e.target === button4){
        e.target.style.boxShadow = makeshadow;
    } if (e.target === button5){
        e.target.style.boxShadow = makeshadow;
    } if (e.target === button6){
        e.target.style.boxShadow = makeshadow;
    } 
}