
const form = document.getElementById("libform");
const storySpan = document.getElementById("story");
const shuffleBtn = document.getElementById("shuffle-button");

let lastInputs = {}; // pour stocker les derniers mots entrés par l'utilisateur

// tableau de modèles de phrases
const stories = [
  ({ noun, adjective, person, verb, place }) =>
    `${person} went to ${place} with a ${adjective} ${noun} and decided to ${verb} all day.`,
  ({ noun, adjective, person, verb, place }) =>
    `In ${place}, ${person} found a ${adjective} ${noun} and tried to ${verb} but failed hilariously.`,
  ({ noun, adjective, person, verb, place }) =>
    `${person} couldn't stop ${verb} when they saw a ${adjective} ${noun} at ${place}.`,
  ({ noun, adjective, person, verb, place }) =>
    `Once upon a time, a ${adjective} ${noun} made ${person} ${verb} across ${place}.`
];

// écouteur pour soumission du formulaire
form.addEventListener("submit", function (e) {
  e.preventDefault();

  const noun = document.getElementById("noun").value.trim();
  const adjective = document.getElementById("adjective").value.trim();
  const person = document.getElementById("person").value.trim();
  const verb = document.getElementById("verb").value.trim();
  const place = document.getElementById("place").value.trim();

  // Vérification que tout est rempli
  if (!noun || !adjective || !person || !verb || !place) {
    alert("Please fill in all fields!");
    return;
  }

  // stocker les valeurs pour les utiliser avec shuffle
  lastInputs = { noun, adjective, person, verb, place };

  // afficher une histoire aléatoire
  displayRandomStory();

  // afficher le bouton shuffle
  shuffleBtn.style.display = "inline-block";
});

// fonction qui choisit une histoire au hasard
function displayRandomStory() {
  if (Object.keys(lastInputs).length === 0) return;

  const randomIndex = Math.floor(Math.random() * stories.length);
  storySpan.textContent = stories[randomIndex](lastInputs);
}

// bouton shuffle pour changer l'histoire
shuffleBtn.addEventListener("click", displayRandomStory);
