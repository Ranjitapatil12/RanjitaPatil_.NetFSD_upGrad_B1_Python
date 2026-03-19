window.onload = function(){

    let score = localStorage.getItem("quizScore");
    let attempts = parseInt(localStorage.getItem("quizAttempts")) || 0;

    let message = "";
    let gradeText = "";

    if(attempts === 0 || score === null){
        message = "No quiz attempted yet";
        gradeText = "";
    }
    else{

        let percent = parseInt(score);

        let grade = determineGrade(percent);
        let status = checkPassStatus(percent);
        let feedback = getFeedback(grade);

        message = `
        Last Quiz Score: ${percent}% <br>
        Attempts: ${attempts} <br>
        Status: ${status}
        `;

        gradeText = `
        Grade: ${grade} <br>
        ${feedback}
        `;

        if(percent >= 80){
            message += '<br><span class="badge bg-success">Top Learner</span>';
        }
    }

    
    document.getElementById("scoreText").innerHTML = message;
    document.getElementById("gradeText").innerHTML = gradeText;

    
    let courses = JSON.parse(localStorage.getItem("completedCourses")) || [];

    let list = document.getElementById("completedCourses");

    if(courses.length > 0){
        list.innerHTML = "";

        courses.forEach(course => {
            let li = document.createElement("li");
            li.innerText = course;
            list.appendChild(li);
        });
    }
};