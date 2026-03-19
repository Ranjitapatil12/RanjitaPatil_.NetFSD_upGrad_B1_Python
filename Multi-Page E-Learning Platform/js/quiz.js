let selectedResponses = [];
let timeLeft = 60;
let timerInterval;
let quizSubmitted = false;

function loadQuizData(){
    return new Promise(resolve => {
        setTimeout(() => {
            resolve(window.quizBank);
        }, 1000); 
    });
}


function renderQuiz(data){

    let html = `<div class="timer">Time Left: <span id="timer">${timeLeft}</span>s</div>`;

    data.forEach((q,i)=>{

        html += `
        <div class="quiz-question">
            <h5>Q${i+1}. ${q.question}</h5>

            <div class="options-container">
                ${q.options.map((opt,index)=>`
                    <label class="option-box">
                        <input type="radio"
                        name="q${i}"
                        value="${index}"
                        onchange="saveResponse(${i}, ${index})">
                        ${opt.replace(/</g,"&lt;").replace(/>/g,"&gt;")}
                    </label>
                `).join("")}
            </div>
        </div>
        `;
    });

    document.getElementById("quizContainer").innerHTML = html;

    startTimer();
}


async function startQuiz(){

    clearInterval(timerInterval);
    quizSubmitted = false;
    timeLeft = 60;
    selectedResponses = [];

   
    document.getElementById("quizContainer").innerHTML = "<p>Loading quiz...</p>";

 
    let data = await loadQuizData();

    renderQuiz(data);
}


function saveResponse(qIndex, option){
    selectedResponses[qIndex] = Number(option);
}


function startTimer(){

    clearInterval(timerInterval);

    timerInterval = setInterval(()=>{

        if(timeLeft <= 0){
            clearInterval(timerInterval);
            submitQuiz();
            return;
        }

        timeLeft--;
        document.getElementById("timer").innerText = timeLeft;

    },1000);
}


function submitQuiz(){

    if(quizSubmitted) return;

    quizSubmitted = true;
    clearInterval(timerInterval);

    let correct = 0;

    window.quizBank.forEach((q,i)=>{
        if(selectedResponses[i] === q.correctAnswer){
            correct++;
        }
    });

    let percent = calculatePercentage(correct, window.quizBank.length);
    let grade = determineGrade(percent);
    let status = checkPassStatus(percent);
    let feedback = getFeedback(grade);

    
    let attempts = parseInt(localStorage.getItem("quizAttempts")) || 0;
    attempts++;
    localStorage.setItem("quizAttempts", attempts);

    
    localStorage.setItem("quizScore", percent);
    localStorage.setItem("quizGrade", grade);
    localStorage.setItem("quizStatus", status);

    
    document.getElementById("resultPanel").innerHTML = `
        <h4>Result</h4>
        <p>Score: <strong>${percent}%</strong></p>
        <p>Grade: <strong>${grade}</strong></p>
        <p>Status: <strong>${status}</strong></p>
        <p>Attempts: <strong>${attempts}</strong></p>
        <p>${feedback}</p>
    `;
}