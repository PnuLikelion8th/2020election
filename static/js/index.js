function getValue(){
    var sido = document.getElementById("sido");
    var sidoselect = document.getElementById("sidoselect");

    sidoselect.innerHTML = sido.value;

    var submit = document.querySelectorById('sidosubmit');
    submit.submit();
}