function calculatePercentage(correct, total){
    return Math.round((correct / total) * 100);
}

function determineGrade(percent){
    if(percent >= 80) return "A";
    else if(percent >= 60) return "B";
    else if(percent >= 40) return "C";
    else return "F";
}

function checkPassStatus(percent){
    return percent >= 40 ? "Pass" : "Fail";
}


function getFeedback(grade){
    switch(grade){
        case "A":
            return "Excellent performance!";
        case "B":
            return "Good job!";
        case "C":
            return "Needs improvement.";
        default:
            return "Try again.";
    }
}



window.calculatePercentage = calculatePercentage;
window.determineGrade = determineGrade;
window.checkPassStatus = checkPassStatus;
window.getFeedback = getFeedback;


if(typeof module !== "undefined"){
    module.exports = {
        calculatePercentage,
        determineGrade,
        checkPassStatus,
        getFeedback
    };
}