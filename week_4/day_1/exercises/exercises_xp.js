// Exercise 1
// Résultat : "inside the funcOne function 3"
// Affiche : 3
// Avec const → Erreur (Assignment to constant variable)

// Affiche : 0
// Change a = 5
// Affiche : 5
// Avec const → Erreur (Assignment to constant variable)

// Définit une variable globale a = "hello"
// Affiche : "hello"

// Résultat : "inside the funcSix function test"
// Affiche : test
// Avec const → Même résultat (pas d’erreur)

// Résultat : "in the if block 5"
// Résultat : "outside of the if block 2"
// Avec const → Même résultat que let


// Exercise 2
const WinBattle = () => true;
let experiencePoints = WinBattle() ? 10 : 1;
console.log(experiencePoints);

// Exercise 3
const isString = (value) => typeof value === "string";
console.log(isString("hello"));
console.log(isString(123));

// Exercise 4
const somme = (a, b) => a + b;
console.log(somme(3, 5));

// Exercise 5
const enGrammes = (kg) => kg * 1000;
console.log(enGrammes(2));


// Différence : une Function Declaration est "hoistée" (on peut l’appeler avant sa définition),
// tandis qu’une Function Expression ne l’est pas (on doit la définir avant de l’utiliser).

function convertKgToGrammes(kg) {
    return kg * 1000;
}

const convertKgToGrammesExpr = function(kg) {
    return kg * 1000;
};

console.log(convertKgToGrammes(3));
console.log(convertKgToGrammesExpr(3));

// Exercise 6
(function(children, partner, location, job) {
    // Créer une phrase avec les arguments
    const message = `You will be a ${job} in ${location}, and married to ${partner} with ${children} kids.`;
    
    // Afficher dans le DOM
    document.body.innerHTML = message;
})(3, "Sofia", "Morocco", "Doctor");

// 🌟 Exercise 7 : Welcome

// Fonction auto-invoquée (IIFE) qui prend le nom de l'utilisateur
(function(userName) {
    // Créer un conteneur
    const userDiv = document.createElement("div");
    userDiv.classList.add("user-info");

    // Ajouter l'image de profil (exemple image générique)
    const userImg = document.createElement("img");
    userImg.src = "https://via.placeholder.com/40"; // image par défaut
    userImg.alt = `${userName}'s profile picture`;

    // Ajouter le nom
    const userText = document.createElement("span");
    userText.textContent = userName;

    // Assembler les éléments
    userDiv.appendChild(userImg);
    userDiv.appendChild(userText);

    // Ajouter dans la navbar
    document.querySelector(".navbar").appendChild(userDiv);

})("John"); 

// 🌟 Exercise 8 : Juice Bar

function makeJuice(size) {
    function addIngredients(ing1, ing2, ing3) {
        const message = `The client wants a ${size} juice, containing ${ing1}, ${ing2}, ${ing3}.`;
        document.body.innerHTML += `<p>${message}</p>`;
    }

    // On appelle la fonction interne une seule fois
    addIngredients("apple", "banana", "orange");
}

// Invocation de la fonction principale
makeJuice("large");

function makeJuice(size) {
    let ingredients = [];

    function addIngredients(ing1, ing2, ing3) {
        ingredients.push(ing1, ing2, ing3);
    }

    function displayJuice() {
        console.log(`The client wants a ${size} juice, containing ${ingredients.join(", ")}.`);
    }

    addIngredients("apple", "banana", "orange");
    addIngredients("kiwi", "mango", "pineapple");

    displayJuice();
}

makeJuice("medium");
