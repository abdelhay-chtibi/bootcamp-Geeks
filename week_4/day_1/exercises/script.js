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