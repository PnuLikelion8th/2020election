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


// function chocie_check(){
//     for (let i=0; i<6; i++){
//         const button{i} = document.querySelector('choice_type1');

//     }
    
// }