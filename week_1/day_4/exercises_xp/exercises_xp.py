# ------ Exercise 1
class Pets:
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat:
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} se promène tranquillement'


class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'


# Créer la classe Siamese qui hérite de Cat
class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'


# Créer une liste all_cats avec 3 instances
cat1 = Bengal("Simba", 3)
cat2 = Chartreux("Luna", 4)
cat3 = Siamese("Milo", 2)

all_cats = [cat1, cat2, cat3]

# Créer sara_pets comme instance de Pets avec all_cats
sara_pets = Pets(all_cats)

#  Faire marcher tous les chats
sara_pets.walk()

# ------ Exercise 2
class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age  
        self.weight = weight

    def bark(self):
        return f'{self.name} aboie'
    
    def run_speed(self):
        return self.weight / self.age * 10
    
    def fight(self, other_dog):
        if self.run_speed() * self.weight > other_dog.run_speed() * other_dog.weight:
            return f'{self.name} gagne le combat contre {other_dog.name}'
        elif self.run_speed() * self.weight < other_dog.run_speed() * other_dog.weight:
            return f'{other_dog.name} gagne le combat contre {self.name}'
        else:
            return f'{self.name} et {other_dog.name} sont à égalité'
        

dog1 = Dog("Rex", 5, 20)
dog2 = Dog("Buddy", 3, 15)  
dog3 = Dog("Max", 4, 18)
print(dog1.bark())
print(dog2.bark())
print(dog1.run_speed())
print(dog2.run_speed())
print(dog1.fight(dog2))
print(dog2.fight(dog3))
print(dog1.fight(dog3))


# ------ Exercise 3
import random

class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False  # Par défaut, le chien n'est pas entraîné

    def train(self):
        print(self.bark())  # On affiche le résultat de bark()
        self.trained = True
        print(f"{self.name} est maintenant entraîné !")

    def play(self, *dog_names):
        all_dogs = ", ".join(dog_names)
        print(f"{all_dogs} jouent tous ensemble.")

    def do_a_trick(self):
        if self.trained:
            tricks = [
                f"{self.name} fait un tonneau.",
                f"{self.name} se met debout sur ses pattes arrière.",
                f"{self.name} vous serre la main.",
                f"{self.name} fait le mort."
            ]
            print(random.choice(tricks))
        else:
            print(f"{self.name} n'est pas encore entraîné et ne peut pas faire de tour.")

# Création de chiens
dog1 = PetDog("Rex", 4, 20)
dog2 = PetDog("Buddy", 3, 18)
dog3 = PetDog("Luna", 5, 15)

# 🐶 Jouer ensemble
dog1.play(dog1.name, dog2.name, dog3.name)

# 🐶 Entraîner Rex
dog1.train()

# 🐶 Rex fait un tour
dog1.do_a_trick()

# 🐶 Buddy tente un tour sans entraînement
dog2.do_a_trick()

# ------ Exercise 4
class Family:
    def __init__(self, last_name, members):
        self.last_name = last_name
        self.members = members 

    def born(self, **kwargs):
        self.members.append(kwargs)
        print(f"Félicitations à la famille {self.last_name} pour la naissance de {kwargs['name']} !")

    def is_18(self, name):
        for member in self.members:
            if member['name'] == name:
                return member['age'] >= 18
        return False

    def family_presentation(self):
        print(f"Famille {self.last_name} :")
        for member in self.members:
            print(f"Nom : {member['name']}, Âge : {member['age']}, Genre : {member['gender']}, Enfant : {member['is_child']}")

members_list = [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}
]

my_family = Family("Smith", members_list)

# Présentation initiale
my_family.family_presentation()

# Vérifier si Michael a 18 ans
print(my_family.is_18("Michael"))  # True

# Ajouter un enfant
my_family.born(name="Emma", age=0, gender="Female", is_child=True)

# Présentation après ajout
my_family.family_presentation()

# ------ Exercise 5
class TheIncredibles(Family):
    def __init__(self, last_name, members):
        super().__init__(last_name, members)

    def use_power(self, name):
        for member in self.members:
            if member['name'] == name:
                if member['age'] >= 18:
                    print(f"{name} utilise son pouvoir : {member['power']}")
                else:
                    raise Exception(f"{name} n'a pas encore 18 ans pour utiliser ses pouvoirs !")

    def incredible_presentation(self):
        print("\n✨ Voici notre famille incroyable ✨")
        super().family_presentation()
        print("Pouvoirs des membres :")
        for member in self.members:
            print(f"{member['incredible_name']} ({member['name']}) → {member['power']}")


incredible_members = [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False,
     'power': 'voler', 'incredible_name': 'MikeFly'},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False,
     'power': 'lire dans les pensées', 'incredible_name': 'SuperWoman'}
]

# Création de la famille incroyable
incredible_family = TheIncredibles("Incredibles", incredible_members)

# Présentation initiale
incredible_family.incredible_presentation()

# Michael utilise son pouvoir
incredible_family.use_power("Michael")

# Ajout de Baby Jack
incredible_family.born(name="Baby Jack", age=1, gender="Male", is_child=True,
                       power="Pouvoir inconnu", incredible_name="JackJack")

# Nouvelle présentation après ajout du bébé
incredible_family.incredible_presentation()


