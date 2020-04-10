function getValue(){
    var sido = document.getElementById("sido");
    var sidoselect = document.getElementById("sidoselect");

    sidoselect.value=sido.value;
};


function candidate_info(giho,jd_name,name,age,job,edu,career1,career2,attend){
    document.getElementById('cd_dt_info').innerHTML = 
            "<div class='name_label'> -이름- </div>"+
            "<div class='name'>안녕하세요! "+name+"후보입니다.</div>"+

            "<div class='belong_label'> -소속- </div>" +
            "<div class='belong'>우리 지역구의 " + giho + "번" +jd_name +"소속이에요</div>"+

            "<div class='age_label'> -나이- </div>" +
            "<div class='age'>현재 나이는" + age + "세 입니다" + "</div>"+

            "<div class='edu_label'> -학력&직업- </div>" +
            "<div class='edu'>"+edu +"를 나와서<br> 현재 " + job+" 일을 하고 있습니다.</div>"+

            "<div class='career_label'> -경력- </div>" +
            "<div class='career'>지금까지<br> " +career1+ ",<br>" + career2 +"를 했었습니다.</div>"+


            (attend === "미확인" ? "" : "<div class='attend_label'>20대 본회의 출석률</div><div>지난 본회의 출석률은" + attend + "에요.</div>")

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