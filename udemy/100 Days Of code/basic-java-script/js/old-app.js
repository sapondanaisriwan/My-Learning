// let anchorElement = document.getElementById("external-link");
// anchorElement.href = "https://google.com";

// anchorElement = document.querySelector("p a");
// anchorElement.href = "https://academind.com";

// create new element
let newAnchorElement = document.createElement("a");
newAnchorElement.href = "https://google.com";
newAnchorElement.textContent = "This is google";

let firstParagraph = document.querySelector("p");
firstParagraph.append(newAnchorElement);

// remove elements
// 1. select tge element that should be removed
let firstH1element = document.querySelector("h1");
// remove element
firstH1element.remove();
// it's the same but for the old browser
// firstH1element.parentElement.removeChild(firstH1element);

// Move elements
firstParagraph.parentElement.append(firstParagraph);

// InnerHTML
console.log(firstParagraph.innerHTML);

// firstParagraph.textContent = "Hi! this is <strong>important</strong>";
firstParagraph.innerHTML = "Hi! this is <strong>important</strong>";
