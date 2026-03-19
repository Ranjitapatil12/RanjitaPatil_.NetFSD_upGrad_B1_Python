const courseModules = {

    "HTML Basics": [
        {
            title: "Week 1",
            content: `
            <h4>Introduction to HTML (Beginner - Level)</h4>

            <p>HTML is the fundamental building block used to create the structure of all web pages.</p>
            <p>It helps in organizing content like text, images, and links in a meaningful way.</p>
            <p>Every website you visit on the internet is built using HTML at its core.</p>

            <ul>
                <li>Defines headings and paragraphs clearly</li>
                <li>Creates links and embeds images</li>
                <li>Organizes content in structured format</li>
            </ul>

            <p>HTML is simple to learn and is considered beginner friendly for new developers.</p>
            <p>It works together with CSS for styling and JavaScript for functionality.</p>
            <p>Web browsers read HTML code and convert it into visible web pages.</p>
            <p>Learning HTML is the first step towards becoming a web developer.</p>
            `
        },

        {
            title: "Week 2",
            content: `
            <h4>HTML Tags</h4>

            <p>HTML tags are used to define elements and structure content inside a webpage.</p>

            <ul>
                <li>&lt;h1&gt; → Used for main headings</li>
                <li>&lt;p&gt; → Used for paragraphs of text</li>
                <li>&lt;a&gt; → Used to create hyperlinks</li>
                <li>&lt;img&gt; → Used to display images</li>
            </ul>

            <p>Each HTML tag has a specific role in defining the structure of the content.</p>
            <p>Most tags come in pairs with opening and closing tags to wrap content.</p>
            <p>Attributes provide additional information like links, sizes, or styles.</p>
            <p>Using proper tags makes the webpage more readable and structured.</p>
            <p>Practicing tags is essential for beginners to build strong fundamentals.</p>
            `
        },

        {
            title: "Week 3",
            content: `
            <h4>HTML Forms</h4>

            <p>HTML forms are used to collect user input such as names, emails, and passwords.</p>
            <p>They are commonly used in login pages, signup forms, and surveys.</p>

            <p>Common form elements include the following:</p>

            <ul>
                <li>Text input fields for user data</li>
                <li>Password fields for secure input</li>
                <li>Submit buttons to send data</li>
            </ul>

            <p>Forms send user data to servers for processing and storage.</p>
            <p>Validation ensures that users enter correct and required information.</p>
            <p>Forms play a major role in user interaction on websites.</p>
            <p>Understanding forms is important for building real-world applications.</p>
            `
        }
    ],

    
    "CSS Layout": [
        {
            title: "Week 1",
            content: `
            <h4>CSS (Intermediate - Level)</h4>

            <p>CSS is used to style and design web pages by applying colors, layouts, and fonts.</p>
            <p>It enhances the visual appearance of HTML elements and improves user experience.</p>

            <p>Some common uses of CSS include:</p>

            <ul>
                <li>Changing text color and font styles</li>
                <li>Adding spacing using margin and padding</li>
                <li>Applying background colors and layouts</li>
            </ul>

            <p>CSS helps separate content from design, making code more maintainable.</p>
            <p>Selectors are used to target specific HTML elements for styling.</p>
            <p>Properties define how elements should look on the webpage.</p>
            <p>CSS plays a major role in making websites visually appealing.</p>
            `
        },

        {
            title: "Week 2",
            content: `
            <h4>Flexbox</h4>

            <p>Flexbox is a layout system used to arrange elements in rows or columns efficiently.</p>

            <ul>
                <li>Supports row and column layouts</li>
                <li>Provides flexible alignment options</li>
                <li>Controls spacing between items</li>
            </ul>

            <p>Flexbox works in a single direction, either horizontally or vertically.</p>
            <p>justify-content aligns items along the main axis of the layout.</p>
            <p>align-items aligns elements along the cross axis.</p>
            <p>Flexbox is widely used in responsive web design.</p>
            <p>It simplifies complex layout structures.</p>
            `
        },

        {
            title: "Week 3",
            content: `
            <h4>Grid System</h4>

            <p>CSS Grid is a powerful layout system that works in both rows and columns.</p>
            <p>It allows developers to create complex layouts easily.</p>

            <ul>
                <li>Defines rows and columns clearly</li>
                <li>Supports grid areas and positioning</li>
                <li>Provides better layout control</li>
            </ul>

            <p>Grid is useful for designing entire page layouts.</p>
            <p>It provides more flexibility compared to Flexbox.</p>
            <p>It supports responsive design techniques.</p>
            <p>Modern websites often use Grid for structure.</p>
            `
        },

        {
            title: "Week 4",
            content: `
            <h4>Responsive Design</h4>

            <p>Responsive design ensures that websites work properly on all screen sizes.</p>

            <ul>
                <li>Uses media queries to adapt layout</li>
                <li>Supports mobile-first design approach</li>
                <li>Makes layouts flexible and scalable</li>
            </ul>

            <p>It improves usability across devices like phones, tablets, and desktops.</p>
            <p>Responsive design is essential for modern web development.</p>
            <p>Layouts automatically adjust based on screen width.</p>
            <p>It enhances overall user experience.</p>
            <p>Every professional website follows responsive design principles.</p>
            `
        }
    ],

    "JavaScript": [
        {
            title: "Week 1",
            content: `
            <h4>Variables (Advanced - Level)</h4>

            <p>Variables are used to store and manage data dynamically in JavaScript programs.</p>

            <ul>
                <li>var is function scoped</li>
                <li>let is block scoped</li>
                <li>const is used for constant values</li>
            </ul>

            <p>Variables help in building logic and controlling application flow.</p>
            <p>They are used to store numbers, strings, arrays, and objects.</p>
            <p>Proper use of variables improves code readability.</p>
            <p>They are fundamental to all JavaScript programs.</p>
            <p>Advanced applications rely heavily on variables.</p>
            `
        },

        {
            title: "Week 2",
            content: `
            <h4>Functions</h4>

            <p>Functions are reusable blocks of code used to perform specific tasks.</p>
            <p>They help in organizing code and improving reusability.</p>

            <ul>
                <li>Arrow functions provide shorter syntax</li>
                <li>Callbacks allow asynchronous operations</li>
                <li>Higher-order functions handle functions as values</li>
            </ul>

            <p>Functions can accept inputs and return outputs.</p>
            <p>They are widely used in real-world applications.</p>
            <p>Functions help in writing clean and modular code.</p>
            <p>They are essential for scalable applications.</p>
            `
        },

        {
            title: "Week 3",
            content: `
            <h4>DOM Manipulation</h4>

            <p>DOM allows JavaScript to interact with and modify HTML elements dynamically.</p>

            <ul>
                <li>getElementById selects elements by ID</li>
                <li>querySelector selects elements using CSS selectors</li>
                <li>Event handling updates UI dynamically</li>
            </ul>

            <p>DOM manipulation helps create interactive web pages.</p>
            <p>It allows changing text, styles, and structure.</p>
            <p>Used in dynamic applications like dashboards.</p>
            <p>It is a core concept in frontend development.</p>
            <p>Understanding DOM is essential for advanced JS.</p>
            `
        },

        {
            title: "Week 4",
            content: `
            <h4>Events</h4>

            <p>Events are actions triggered by user interactions such as clicks and key presses.</p>
            <p>They make web pages interactive and responsive.</p>

            <ul>
                <li>Click events for buttons</li>
                <li>Keyboard events for inputs</li>
                <li>Mouse events for interactions</li>
            </ul>

            <p>addEventListener is used to handle multiple events efficiently.</p>
            <p>Events improve user experience significantly.</p>
            <p>They are used in forms and interactive UI elements.</p>
            <p>Events are important in dynamic applications.</p>
            `
        },

        {
            title: "Week 5",
            content: `
            <h4>Async JavaScript</h4>

            <p>Asynchronous JavaScript allows handling tasks like API calls without blocking execution.</p>

            <ul>
                <li>Promises handle asynchronous results</li>
                <li>async/await simplifies async code</li>
                <li>Callbacks manage delayed execution</li>
            </ul>

            <p>Async programming improves application performance.</p>
            <p>It is used in fetching data from servers.</p>
            <p>It prevents UI freezing.</p>
            <p>It is widely used in modern applications.</p>
            <p>Understanding async is important for advanced JS.</p>
            `
        },

        {
            title: "Week 6",
            content: `
            <h4>ES6 Features</h4>

            <p>ES6 introduced modern JavaScript features that improve coding efficiency.</p>
            <p>These features are widely used in professional development.</p>

            <ul>
                <li>Arrow functions simplify syntax</li>
                <li>Template literals support multi-line strings</li>
                <li>Destructuring extracts values easily</li>
            </ul>

            <p>ES6 improves code readability and maintainability.</p>
            <p>It supports modular programming.</p>
            <p>It is used in frameworks like React and Angular.</p>
            <p>Learning ES6 is important for interviews.</p>
            `
        }
    ]
};



let currentCourse = localStorage.getItem("currentCourse");
let currentModule = parseInt(localStorage.getItem("currentModule"));

let module = courseModules[currentCourse][currentModule];

window.onload = function(){
    document.getElementById("moduleTitle").innerText = module.title;
    document.getElementById("moduleContent").innerHTML = module.content;
};

function markComplete(){

    let progress = JSON.parse(localStorage.getItem("moduleProgress")) || {};

    if(!progress[currentCourse]){
        progress[currentCourse] = [];
    }

    if(!progress[currentCourse].includes(currentModule)){
        progress[currentCourse].push(currentModule);
    }

    localStorage.setItem("moduleProgress", JSON.stringify(progress));

    alert("Completed!");

    window.location.href = "CourseContent.html";
}