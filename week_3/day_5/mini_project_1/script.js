const palette = document.getElementById("color-palette");
const grid = document.getElementById("grid");
const clearBtn = document.getElementById("clear-btn");

// Liste des couleurs
const colors = [
  "red", "orange", "gold",
  "yellow", "yellowgreen", "lightgreen",
  "green", "turquoise", "cyan",
  "lightskyblue", "dodgerblue", "blue",
  "darkblue", "purple", "magenta",
  "violet", "pink", "lightgray",
  "gray", "black", "white"
];

let selectedColor = colors[0];
let isDrawing = false;

// Générer la palette
colors.forEach((color, index) => {
  const div = document.createElement("div");
  div.classList.add("color");
  div.style.background = color;
  if (index === 0) div.classList.add("selected");
  div.addEventListener("click", () => {
    document.querySelectorAll(".color").forEach(c => c.classList.remove("selected"));
    div.classList.add("selected");
    selectedColor = color;
  });
  palette.appendChild(div);
});

// Générer la grille
for (let i = 0; i < 30 * 20; i++) {
  const cell = document.createElement("div");
  cell.classList.add("cell");

  cell.addEventListener("mousedown", () => {
    isDrawing = true;
    cell.style.background = selectedColor;
  });

  cell.addEventListener("mouseover", () => {
    if (isDrawing) {
      cell.style.background = selectedColor;
    }
  });

  grid.appendChild(cell);
}

// Arrêter de dessiner quand on relâche la souris
document.body.addEventListener("mouseup", () => {
  isDrawing = false;
});

// Effacer toute la grille
clearBtn.addEventListener("click", () => {
  document.querySelectorAll(".cell").forEach(cell => {
    cell.style.background = "white";
  });
});
