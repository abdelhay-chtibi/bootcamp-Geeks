let client = "John";

const groceries = {
    fruits: ["pear", "apple", "banana"],
    vegetables: ["tomatoes", "cucumber", "salad"],
    totalPrice: "20$",
    other: {
        paid: true,
        meansOfPayment: ["cash", "creditCard"]
    }
};

// 1️⃣ Fonction pour afficher les fruits
const displayGroceries = () => {
    groceries.fruits.forEach(fruit => console.log(fruit));
};

// 2️⃣ Fonction pour cloner (en testant la valeur/référence)
const cloneGroceries = () => {
    // --- Pass by Value ---
    let user = client;   // copie de la valeur
    client = "Betty";    // modification de la variable originale

    console.log("user:", user);   // reste "John"
    console.log("client:", client); // devient "Betty"
    // ⚡ Explication : les strings sont copiées par valeur, pas par référence.

    // --- Pass by Reference ---
    let shopping = groceries;  // référence au même objet
    shopping.totalPrice = "35$";  
    shopping.other.paid = false;

    console.log("groceries.totalPrice:", groceries.totalPrice); 
    console.log("groceries.other.paid:", groceries.other.paid); 
    // ⚡ Explication : les objets sont copiés par référence → les deux pointent vers la même mémoire.
};

// 🔥 Tester les fonctions
displayGroceries();
cloneGroceries();
