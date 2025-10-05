const btnShow = document.getElementById("show-btn");
const inputText = document.getElementById("text-input");

const showText = ()=>{
    const text = inputText.value;

    const titleShow = document.getElementById("show-text");
    titleShow.textContent = text;

    inputText.value="";
}

btnShow.addEventListener('click',showText)

