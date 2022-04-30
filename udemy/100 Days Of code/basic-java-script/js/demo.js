let productNameInputElement = document.getElementById("product-name");
let remainingCharsElement = document.getElementById("remaining-chars");

// console.dir(productNameInputElement);
const maxAllowedChars = productNameInputElement.maxLength;

function updateRemainingCharacters(event) {
  const enteredText = event.target.value;
  const enteredTextLength = enteredText.length;

  const remainingCharacters = maxAllowedChars - enteredTextLength;
  remainingCharsElement.textContent = remainingCharacters;

  if (remainingCharacters <= 10) {
    remainingCharacters.classList.add("warning");
    productNameInputElement.classList.add("warning");
  } else {
    remainingCharacters.classList.remove("warning");
    productNameInputElement.classList.remove("warning");
  }
}

productNameInputElement.addEventListener("input", updateRemainingCharacters);
