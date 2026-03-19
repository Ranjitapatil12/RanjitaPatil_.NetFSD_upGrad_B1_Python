function openCourse(courseName){
    localStorage.setItem("currentCourse", courseName);
    window.location.href = "CourseContent.html";
}