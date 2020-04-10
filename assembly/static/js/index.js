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

    let promise1 = document.querySelectorAll('.promise1');
    let promise2 = document.querySelectorAll('.promise2');
    let promise3 = document.querySelectorAll('.promise3');
    let promise4 = document.querySelectorAll('.promise4');
    let promise5 = document.querySelectorAll('.promise5');
    let promise6 = document.querySelectorAll('.promise6');


    let promise_list = [promise1,promise2,promise3,promise4,promise5,promise6]

    for(let i=0; i<6; i++){
        for(let j=0; j<promise_list[i].length; j++){
            promise_list[i][j].style.display="none"
        }
    }
    const makeshadow = "0 0px 10px 6px rgba(0,0,0,0.4)"
    

    if (e.target === button1){
        e.target.style.boxShadow = makeshadow;
        for(let i=0; i<promise1.length; i++){
            promise1[i].style.display="block"
        }
    } if (e.target === button2){
        e.target.style.boxShadow = makeshadow;
        for(let i=0; i<promise2.length; i++){
            promise2[i].style.display="block"
        }
    } if (e.target === button3){
        e.target.style.boxShadow = makeshadow;
        for(let i=0; i<promise3.length; i++){
            promise3[i].style.display="block"
        }
    } if (e.target === button4){
        e.target.style.boxShadow = makeshadow;
        for(let i=0; i<promise4.length; i++){
            promise4[i].style.display="block"
        }
    } if (e.target === button5){
        e.target.style.boxShadow = makeshadow;
        for(let i=0; i<promise5.length; i++){
            promise5[i].style.display="block"
        }
    } if (e.target === button6){
        e.target.style.boxShadow = makeshadow;
        for(let i=0; i<promise6.length; i++){
            promise6[i].style.display="block"
        }
    } 
}