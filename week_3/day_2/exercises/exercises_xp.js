// ===== Exercise 1
let people = ["Greg", "Mary", "Devon", "James"];

// 1. Remove “Greg”
people.shift(); // ["Mary", "Devon", "James"]

// 2. Replace “James” with “Jason”
people[people.indexOf("James")] = "Jason"; // ["Mary", "Devon", "Jason"]

// 3. Add your name to the end
people.push("Abdelhay"); // ["Mary", "Devon", "Jason", "Abdelhay"]

// 4. Console.log Mary’s index
console.log(people.indexOf("Mary")); // 0

// 5. Make a copy of the array WITHOUT "Mary" and "Abdelhay"
let peopleCopy = people.slice(1, people.length - 1); 
console.log(peopleCopy); // ["Devon", "Jason"]

// 6. Get index of “Foo”
console.log(people.indexOf("Foo")); // -1 because "Foo" is not in the array

// 7. Variable last = last element of array
let last = people[people.length - 1];
console.log(last); // "Abdelhay"

// 1. Loop through the people array and console.log each person
for (let i = 0; i < people.length; i++) {
  console.log(people[i]);
}

// 2. Loop and exit after logging “Devon”
for (let i = 0; i < people.length; i++) {
  console.log(people[i]);
  if (people[i] === "Devon") {
    break; // stops the loop
  }
}

// ===== Exercise 2
const colors = ["Blue", "Red", "Black", "White", "Green"];

// Simple version
for (let i = 0; i < colors.length; i++) {
  console.log(`My #${i + 1} choice is ${colors[i]}`);
}

// Bonus version with suffixes
const suffixes = ["st", "nd", "rd", "th", "th"];
for (let i = 0; i < colors.length; i++) {
  console.log(`My ${i + 1}${suffixes[i]} choice is ${colors[i]}`);
}


// ===== Exercise 3
let number;

do {
  number = Number(prompt("Enter a number greater than or equal to 10:"));
} while (number < 10);

console.log("Good! Your number is:", number);

// ===== Exercise 4
const building = {
  numberOfFloors: 4,
  numberOfAptByFloor: {
    firstFloor: 3,
    secondFloor: 4,
    thirdFloor: 9,
    fourthFloor: 2,
  },
  nameOfTenants: ["Sarah", "Dan", "David"],
  numberOfRoomsAndRent: {
    sarah: [3, 990],
    dan: [4, 1000],
    david: [1, 500],
  },
};

// 1. Number of floors
console.log(building.numberOfFloors);

// 2. Apartments on floors 1 and 3
console.log(
  `1st Floor: ${building.numberOfAptByFloor.firstFloor}, 3rd Floor: ${building.numberOfAptByFloor.thirdFloor}`
);

// 3. Name of second tenant + number of rooms
console.log(
  `${building.nameOfTenants[1]} has ${building.numberOfRoomsAndRent.dan[0]} rooms`
);

// 4. Check rent condition
const sarahRent = building.numberOfRoomsAndRent.sarah[1];
const davidRent = building.numberOfRoomsAndRent.david[1];
const danRent = building.numberOfRoomsAndRent.dan[1];

if (sarahRent + davidRent > danRent) {
  building.numberOfRoomsAndRent.dan[1] = 1200;
}
console.log(building.numberOfRoomsAndRent.dan);

// ===== Exercise 5
const family = {
  father: "Ali",
  mother: "Aicha",
  child: "Mohamed",
};

// Console.log keys
for (let key in family) {
  console.log(key);
}

// Console.log values
for (let key in family) {
  console.log(family[key]);
}

// ===== Exercise 6
const details = {
  my: "name",
  is: "Rudolf",
  the: "reindeer",
};

let sentence = "";
for (let key in details) {
  sentence += key + " " + details[key] + " ";
}
console.log(sentence.trim()); // "my name is Rudolf the reindeer"

// ===== Exercise 7
const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];

let societyName = names
  .map(name => name[0]) // take first letter
  .sort()               // sort alphabetically
  .join("");            // join to string

console.log(societyName); // "ABJKPS"
