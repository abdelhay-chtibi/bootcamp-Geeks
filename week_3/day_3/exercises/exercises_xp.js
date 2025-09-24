// ===== Exercise 1
// Version sans paramètre
function displayNumbersDivisible() {
  let sum = 0;
  for (let i = 0; i <= 500; i++) {
    if (i % 23 === 0) {
      console.log(i);
      sum += i;
    }
  }
  console.log("Sum:", sum);
}

displayNumbersDivisible();

// Bonus : version avec paramètre
function displayNumbersDivisibleBy(divisor) {
  let sum = 0;
  for (let i = 0; i <= 500; i++) {
    if (i % divisor === 0) {
      console.log(i);
      sum += i;
    }
  }
  console.log(`Sum of numbers divisible by ${divisor}:`, sum);
}

displayNumbersDivisibleBy(3); // Exemple

// ===== Exercise 2

const stock = { 
  banana: 6, 
  apple: 0,
  pear: 12,
  orange: 32,
  blueberry: 1
};

const prices = {    
  banana: 4, 
  apple: 2, 
  pear: 1,
  orange: 1.5,
  blueberry: 10
};

const shoppingList = ["banana", "orange", "apple"];

function myBill() {
  let total = 0;
  for (let item of shoppingList) {
    if (item in stock && stock[item] > 0) {
        // console.log(stock[item])
      total += prices[item];
      stock[item]--; // bonus : on diminue le stock
    }
  }
  console.log("Total price:", total);
  return total;
}

myBill();
console.log("Stock restant :", stock);

// ===== Exercise 3
function changeEnough(itemPrice, amountOfChange) {
  const [quarters, dimes, nickels, pennies] = amountOfChange;
  const total = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01;
  return total >= itemPrice;
}

// Tests
console.log(changeEnough(4.25, [25, 20, 5, 0])); // true
console.log(changeEnough(14.11, [2, 100, 0, 0])); // false
console.log(changeEnough(0.75, [0, 0, 20, 5])); // true

// ===== Exercise 4

function hotelCost(nights) {
    return nights * 140;
}

function planeRideCost(destination) {
    destination = destination.toLowerCase();
    if (destination === "london") return 183;
    if (destination === "paris") return 220;
    return 300;
}

function rentalCarCost(days) {
    let cost = days * 40;
    if (days > 10) cost *= 0.95; // 5% discount
    return cost;
}

function totalVacationCost() {
    const nights = Number(prompt("How many nights in the hotel?"));
    const destination = prompt("Where do you want to go?");
    const days = Number(prompt("How many days do you need a car?"));

    const hotel = hotelCost(nights);
    const plane = planeRideCost(destination);
    const car = rentalCarCost(days);

    console.log(`The car cost: $${car}, the hotel cost: $${hotel}, the plane tickets cost: $${plane}`);
    console.log(`Total: $${hotel + plane + car}`);
}

totalVacationCost();

// ===== Exercise 5
// Supposons que tu as ajouté le HTML dans ton fichier index.html
const div = document.getElementById("container");
console.log(div);

const lists = document.querySelectorAll(".list");
lists[0].children[1].textContent = "Richard";
lists[1].children[1].remove();

for (let ul of lists) {
    ul.children[0].textContent = "Abdelhay";
}

// Ajouter classes
lists.forEach(ul => ul.classList.add("student_list"));
lists[0].classList.add("university", "attendance");

// Style
div.style.backgroundColor = "lightblue";
div.style.padding = "10px";
lists[1].lastElementChild.style.display = "none";
lists[0].children[1].style.border = "2px solid black";
document.body.style.fontSize = "20px";

if (div.style.backgroundColor === "lightblue") {
    alert(`Hello ${lists[0].children[0].textContent} and ${lists[0].children[1].textContent}`);
}

//Exercise 6
const navBar = document.getElementById("navBar");
navBar.setAttribute("id", "socialNetworkNavigation");

const ul = navBar.querySelector("ul");
const li = document.createElement("li");
li.textContent = "Logout";
ul.appendChild(li);

console.log("First link:", ul.firstElementChild.textContent);
console.log("Last link:", ul.lastElementChild.textContent);

//Exercise 7
const allBooks = [
    {
        title: "Clean Code",
        author: "Robert C. Martin",
        image: "https://m.media-amazon.com/images/I/41xShlnTZTL._SX258_BO1,204,203,200_.jpg",
        alreadyRead: true
    },
    {
        title: "You Don't Know JS",
        author: "Kyle Simpson",
        image: "https://m.media-amazon.com/images/I/51bRhyVTVGL._SX331_BO1,204,203,200_.jpg",
        alreadyRead: false
    }
];

const section = document.querySelector(".listBooks");

allBooks.forEach(book => {
    const div = document.createElement("div");
    div.innerHTML = `<p>${book.title} written by ${book.author}</p>
                   <img src="${book.image}" style="width:100px;">`;
    if (book.alreadyRead) {
        div.style.color = "red";
    }
    section.appendChild(div);
});
