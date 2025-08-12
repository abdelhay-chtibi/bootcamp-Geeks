# ------ Exercise 1
try: 
    nombre = int(input("Entrez un nombre entier entre 1 et 12 : ")) 
    if 3 <= nombre <= 5:
        print("Spring ")
    elif 6 <= nombre <= 8:
        print("Summer ")
    elif 9 <= nombre <= 11:
        print("Autumn ") 
    elif nombre == 12 or nombre == 1 or nombre == 2:
        print("Winter ")
except ValueError:
    print("Erreur : veuillez entrer un nombre entier valide.")
# ------ Exercise 2
for i in range(1,21):
    if i % 2 == 0:
        print(i)
# ------ Exercise 3
mon_prenom = "abdelhay"

while True: 
    prenom = input("Entrez votre prénom: ")
    if prenom.lower() == mon_prenom:
        print("Bonjour, Abdelhay!")
        break   
    else:
        print("Ce n'est pas votre prénom, essayez encore.")

# ------ Exercise 4
names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
name = input("Enter a name to search: ")
if name in names:
    print(f"{name} is in the list.")
    print(names.index(name))
# ------ Exercise 5
first_number = int(input("Entrez le premier nombre : "))
second_number = int(input("Entrez le deuxième nombre : "))
third_number = int(input("Entrez le troisième nombre : "))

max_number = max(first_number, second_number, third_number)
print(f"Le plus grand nombre est : {max_number}")
# ------ Exercise 6
import random
number = None
random_number = random.randint(1, 9)
tentation = 0
try:    
    while number != 0:
        number = int(input("Entrez un nombre entier entre 1 et 9, Si tu veux arrete entez 0: "))
        tentation += 1
        if number < 1 or number > 9:
            print("Erreur : le nombre doit être entre 1 et 9.")
        else:
            print(f"Le nombre aléatoire est : {random_number}")
            if number == random_number:
                print("Winner !")
                break
            else:
                print("Better luck next time.")
    print("Fin du jeu.")
    print("Nombre de tentatives :", tentation)
except ValueError:
    print("Ce n'est pas un nombre entier valide.")
