// let course = "100 days of code";
// let price = 300;
// let mainGoals = ["practice", "job", "cool"];
// alert(course);
// alert(price);
// alert(mainGoals);

// let onlineCourse = {
//   name: "100 days of code",
//   price: 300,
//   goals: ["practice", "job", "cool"],
// };

// alert(onlineCourse.name);
// alert(onlineCourse.price);
// alert(onlineCourse.goals[1]);

// function getListItem(array, arrayIndex) {
//   let arrayElement = array[arrayIndex];
//   return arrayElement;
// }

// let firstGoal = getListItem(onlineCourse.goals, 0);

// let person = {
//   name: "Soft", // Porperty
//   greet() {
//     console.log("Hello youtube");
//   },
// };
// person.greet();

// document.body.children[1].children[0].href = "https://google.com";
// console.dir(document);

// console.log(document.getElementById("external-link"));

let h1Element = document.body.firstElementChild;
h1Element = document.body.children[0];

console.dir(h1Element.parentElement);

h1Element = document.getElementById("first-title");

console.dir(h1Element);

// querySelector use to select css
let highlightedParagraph = document.querySelector(".highlighted-paragraph");

console.dir(highlightedParagraph);

highlightedParagraph.textContent = "This was changed by God";
