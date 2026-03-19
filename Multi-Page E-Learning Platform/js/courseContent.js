const courseModules = {
    "HTML Basics": [
        { title: "Week 1", content: "<p>Introduction to HTML. HTML builds structure of web pages.</p>" },
        { title: "Week 2", content: "<p>HTML Tags like h1, p, a define content.</p>" },
        { title: "Week 3", content: "<p>Forms collect user input using inputs and buttons.</p>" }
    ],

    "CSS Layout": [
        { title: "Week 1", content: "<p>Selectors target elements.</p>" },
        { title: "Week 2", content: "<p>Flexbox helps alignment.</p>" },
        { title: "Week 3", content: "<p>Grid builds layouts.</p>" },
        { title: "Week 4", content: "<p>Responsive design adapts screens.</p>" }
    ],

    "JavaScript": [
        { title: "Week 1", content: "<p>Variables store data.</p>" },
        { title: "Week 2", content: "<p>Functions execute logic.</p>" },
        { title: "Week 3", content: "<p>DOM manipulates HTML.</p>" },
        { title: "Week 4", content: "<p>Events handle actions.</p>" },
        { title: "Week 5", content: "<p>Async handles delays.</p>" },
        { title: "Week 6", content: "<p>ES6 modern JS features.</p>" }
    ]
};

let currentCourse = localStorage.getItem("currentCourse");
let modules = courseModules[currentCourse];

window.onload = function(){

    document.getElementById("courseTitle").innerText = currentCourse;
    document.getElementById("courseName").innerText = currentCourse;

    let container = document.getElementById("moduleContainer");

    let progress = JSON.parse(localStorage.getItem("moduleProgress")) || {};
    let completed = progress[currentCourse] || [];

    modules.forEach((mod, index) => {

        let div = document.createElement("div");
        div.className = "course-box mt-3";

        div.innerHTML = `
            <h5>${mod.title}</h5>
            <button class="btn" onclick="openModule(${index})">
                ${completed.includes(index) ? "Revisit" : "Start"}
            </button>
        `;

        container.appendChild(div);
    });

    updateProgress();
};

function openModule(index){
    localStorage.setItem("currentModule", index);
    window.location.href = "module.html";
}

function updateProgress(){

    let progress = JSON.parse(localStorage.getItem("moduleProgress")) || {};
    let done = (progress[currentCourse] || []).length;

    let percent = Math.round((done / modules.length) * 100);

    document.getElementById("progressText").innerText =
        "Progress: " + percent + "%";

    let courseProgress = JSON.parse(localStorage.getItem("courseProgress")) || {};
    courseProgress[currentCourse] = percent;

    localStorage.setItem("courseProgress", JSON.stringify(courseProgress));

    if(percent === 100){
        let completedCourses = JSON.parse(localStorage.getItem("completedCourses")) || [];
        if(!completedCourses.includes(currentCourse)){
            completedCourses.push(currentCourse);
        }
        localStorage.setItem("completedCourses", JSON.stringify(completedCourses));
    }
}