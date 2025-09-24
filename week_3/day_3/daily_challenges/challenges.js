
// Tableau d'objets : chaque planète a un nom, une couleur et un nombre de lunes
const planets = [
  { name: "Mercury", color: "gray", moons: 0 },
  { name: "Venus", color: "yellow", moons: 0 },
  { name: "Earth", color: "blue", moons: 1 },
  { name: "Mars", color: "red", moons: 2 },
  { name: "Jupiter", color: "orange", moons: 79 },
  { name: "Saturn", color: "goldenrod", moons: 83 },
  { name: "Uranus", color: "lightblue", moons: 27 },
  { name: "Neptune", color: "darkblue", moons: 14 }
];

// Sélection de la section dans le HTML
const section = document.querySelector(".listPlanets");

// Boucle sur chaque planète
planets.forEach(planet => {
  // Créer la div planète
  const planetDiv = document.createElement("div");
  planetDiv.classList.add("planet");
  planetDiv.style.backgroundColor = planet.color;
  planetDiv.textContent = planet.name;

  // Ajouter les lunes
  for (let i = 0; i < planet.moons; i++) {
    const moon = document.createElement("div");
    moon.classList.add("moon");
    // Positionner chaque lune de façon décalée autour de la planète
    moon.style.left = `${110 + i * 35}px`;
    moon.style.top = `${i * 35}px`;
    planetDiv.appendChild(moon);
  }

  // Ajouter la planète dans la section
  section.appendChild(planetDiv);
});

