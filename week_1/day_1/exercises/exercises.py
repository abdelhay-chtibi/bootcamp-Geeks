# ------ Exercise 1
for i in range(4):
    print("Hello, World!")
# ------ Exercise 2
result = (99**3) * 8
print(result)
# ------ Exercise 3
name = input("Enter your name: ")
user_name = "Abdelhay"
if name == user_name:
    print("incroyable ! On a le même prénom !")
# ------ Exercise 4
try:
    taille = int(input("Entez la taille en cm: "))
    if taille > 145:
        print("t'es suffisamment grands pour rouler.")
    else:
        print("t'es pas assez grands pour rouler.")
except ValueError:
    print("Erreur : veuillez entrer un nombre entier pour la taille.")
# ------ Exercise 5
my_fav_numbers = {7, 8, 9, 10}
my_fav_numbers.add(11)
my_fav_numbers.add(99)
 
print(my_fav_numbers)

remove_number = 8
if remove_number in my_fav_numbers: 
    my_fav_numbers.remove(remove_number)     

print(my_fav_numbers)

friend_fav_numbers = set([1, 2, 3, 4, 5])
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)

print(our_fav_numbers)
# ------ Exercise 6
#Non
# ------ Exercise 7
basket = ["Banana", "Apples", "Oranges", "Blueberries"]

basket.remove("Banana") 

basket.remove("Blueberries") 

basket.append("Kiwi")

basket.insert(0, "Apples")

nombre_basket = basket.count("Apples")

print(nombre_basket)

basket.clear()

print(basket)
# ------ Exercise 8
sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]

while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")

#print("Pastrami sandwich est bien supprimer.")

finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)  
    finished_sandwiches.append(current_sandwich)

for sandwich in finished_sandwiches:
    print(f"I made your {sandwich}")

