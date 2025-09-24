// ===== Exercise 1
// 1. Retrieve h1
const h1 = document.querySelector("h1");
console.log(h1.textContent);

// 2. Remove last paragraph
const article = document.querySelector("article");
article.lastElementChild.remove();

// 3. Change h2 background on click
const h2 = document.querySelector("h2");
h2.addEventListener("click", () => {
  h2.style.backgroundColor = "red";
});

// 4. Hide h3 on click
const h3 = document.querySelector("h3");
h3.addEventListener("click", () => {
  h3.style.display = "none";
});

// 5. Button to make paragraphs bold
const button = document.getElementById("makeBold");
button.addEventListener("click", () => {
  document.querySelectorAll("p").forEach(p => {
    p.style.fontWeight = "bold";
  });
});

// BONUS: random font size for h1 on hover
h1.addEventListener("mouseover", () => {
  h1.style.fontSize = `${Math.floor(Math.random() * 100)}px`;
});

// BONUS: fade out 2nd paragraph on hover
const secondParagraph = document.querySelectorAll("p")[1];
secondParagraph.style.transition = "opacity 1s";
secondParagraph.addEventListener("mouseover", () => {
  secondParagraph.style.opacity = 0;
});
secondParagraph.addEventListener("mouseout", () => {
  secondParagraph.style.opacity = 1;
});

// ===== Exercise 2
const form2 = document.querySelector("#myForm");
console.log(form);

const fname = document.getElementById("fname");
const lname = document.getElementById("lname");
console.log(fname, lname);

const inputsByName = document.getElementsByName("firstname");
console.log(inputsByName);

const ul = document.querySelector(".usersAnswer");

form2.addEventListener("submit", (event) => {
  event.preventDefault(); // Empêche le rechargement de la page

  ul.innerHTML = ""; // reset de la liste

  if (fname.value.trim() && lname.value.trim()) {
    const li1 = document.createElement("li");
    li1.textContent = fname.value;
    ul.appendChild(li1);

    const li2 = document.createElement("li");
    li2.textContent = lname.value;
    ul.appendChild(li2);
  } else {
    alert("Veuillez remplir les deux champs !");
  }
});

// ===== Exercise 3
let allBoldItems = [];

function getBoldItems() {
  allBoldItems = document.querySelectorAll("#myParagraph strong");
}

function highlight() {
  allBoldItems.forEach(item => item.style.color = "blue");
}

function returnItemsToDefault() {
  allBoldItems.forEach(item => item.style.color = "black");
}

getBoldItems();

const paragraph = document.getElementById("myParagraph");
paragraph.addEventListener("mouseover", highlight);
paragraph.addEventListener("mouseout", returnItemsToDefault);

// ===== Exercise 4
const form = document.getElementById("MyForm");

form.addEventListener("submit", (e) => {
  e.preventDefault();

  const radius = parseFloat(document.getElementById("radius").value);
  if (isNaN(radius)) {
    alert("Please enter a valid number!");
    return;
  }

  const volume = (4/3) * Math.PI * Math.pow(radius, 3);
  document.getElementById("volume").value = volume.toFixed(2);
});
