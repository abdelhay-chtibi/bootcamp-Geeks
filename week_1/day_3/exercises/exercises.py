# ------ Exercise 1
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

cat1 = Cat("anna", 3)
cat2 = Cat("bob", 5)   
cat3 = Cat("charlie", 2)

def get_older_cat(*cats):
    oldest_cat = None
    for cat in cats:
        if oldest_cat is None or cat.age > oldest_cat.age:
            oldest_cat = cat
    return oldest_cat

print(f"The oldest cat is {get_older_cat(cat1, cat2, cat3).name}.")


# ------ Exercise 2
class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height
    
    def bark(self):
        return f"{self.name} does Woof!"
    
    def jump(self):
        return f"{self.name} jumps {self.height * 2} cm high!"
         
davids_dog = Dog("Rex", 50)
print(davids_dog.bark())
print(davids_dog.jump())

sarahs_dog = Dog("Teacup", 20)
print(sarahs_dog.bark())
print(sarahs_dog.jump())    

if davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name} is taller than {sarahs_dog.name}.")
else:
    print(f"{sarahs_dog.name} is taller than {davids_dog.name}.")

# ------ Exercise 3
class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
    
stairway = Song(["Il y a une dame qui est sûre", "que tout ce qui brille est de l'or", "et elle achète un escalier vers le paradis"])
stairway.sing_me_a_song()
# ------ Exercise 4
class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        print("Animaux du zoo :", self.animals)
    
    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
        else:
            print(f"{animal_sold} n'est pas dans le zoo.")

    def sort_animals(self):
        sorted_animals = sorted(self.animals)
        grouped = {}
        for animal in sorted_animals:
            first_letter = animal[0].upper()
            if first_letter not in grouped:
                grouped[first_letter] = [animal]
            else:
                grouped[first_letter].append(animal)
        return grouped

    def get_groups(self):
        groups = self.sort_animals()
        for letter, animals in groups.items():
            print(f"{letter}: {animals}")


new_york_zoo = Zoo("New York Zoo")

new_york_zoo.add_animal("Giraffe")
new_york_zoo.add_animal("Bear")
new_york_zoo.add_animal("Ape")
new_york_zoo.add_animal("Cougar")
new_york_zoo.add_animal("Cat")

new_york_zoo.get_animals()
new_york_zoo.sell_animal("Bear")
new_york_zoo.get_animals()

print("\nAnimaux triés et regroupés :")
new_york_zoo.get_groups()
