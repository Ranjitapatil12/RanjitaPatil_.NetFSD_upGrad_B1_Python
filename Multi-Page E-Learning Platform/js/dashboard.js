function animateCounter(id, target){

    let count = 0;
    let increment = target / 50;

    let element = document.getElementById(id);
    if(!element) return;

    let interval = setInterval(()=>{

        count += increment;

        if(count >= target){
            count = target;
            clearInterval(interval);
        }

        element.innerText = Math.floor(count);

    },30);
}

window.onload = function(){

    animateCounter("courseCount", 3);

    
    let attempts = parseInt(localStorage.getItem("quizAttempts")) || 0;
    animateCounter("quizAttempts", attempts);

   
    let progress = JSON.parse(localStorage.getItem("courseProgress")) || {};

    
    let htmlValue = progress["HTML Basics"] || 0;
    document.getElementById("htmlProgress").value = htmlValue;
    document.getElementById("htmlText").innerText = htmlValue + "% Completed";

    
    let cssValue = progress["CSS Layout"] || 0;
    document.getElementById("cssProgress").value = cssValue;
    document.getElementById("cssText").innerText = cssValue + "% Completed";


    let jsValue = progress["JavaScript"] || 0;
    document.getElementById("jsProgress").value = jsValue;
    document.getElementById("jsText").innerText = jsValue + "% Completed";

    let values = Object.values(progress);

    let avg = 0;
    if(values.length > 0){
        avg = values.reduce((a,b)=>a+b,0) / values.length;
    }

    animateCounter("avgScore", Math.round(avg));
};