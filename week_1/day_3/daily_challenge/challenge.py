class Farm:
    def __init__(self, farm_name):
        self.name = farm_name
        self.animals = {}

    def add_animal(self, animal_type, count=1):
        """Ajoute un animal à la ferme ou incrémente son nombre"""
        if animal_type in self.animals:
            self.animals[animal_type] += count
        else:
            self.animals[animal_type] = count

    def get_info(self):
        """Retourne les informations complètes de la ferme"""
        info = f"{self.name}'s farm\n\n"
        for animal, count in sorted(self.animals.items()):
            info += f"{animal} : {count}\n"
        info += "\nE-I-E-I-0!"
        return info

    def get_animal_types(self):
        """Retourne une liste triée de tous les types d'animaux"""
        return sorted(self.animals.keys())

    def get_short_info(self):
        """Retourne une phrase courte décrivant la ferme et ses animaux"""
        animal_types = self.get_animal_types()
        animals_str_list = []
        for animal in animal_types:
            if self.animals[animal] > 1:
                animals_str_list.append(animal + "s")
            else:
                animals_str_list.append(animal)
        animals_str = ", ".join(animals_str_list)
        return f"{self.name}'s farm has {animals_str}."


# -------------------------------
# Exemple d'utilisation
# -------------------------------
macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)

# Affiche les infos complètes
print(macdonald.get_info())

print("\n----------------------\n")

# Affiche la phrase courte
print(macdonald.get_short_info())
