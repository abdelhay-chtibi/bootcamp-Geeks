# ------ Exercise 1
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
resultat = dict(zip(keys, values))
print(resultat)
# ------ Exercise 2
# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

family = {}

while True:
    name = input("Entrez le nom d'un membre de la famille (ou 'stop' pour terminer) : ")
    if name.lower() == "stop":
        break
    age = int(input(f"Entrez l'âge de {name} : "))
    family[name] = age

total_cost = 0

for name, age in family.items():
    if age < 3:
        cost = 0
    elif age <= 12:
        cost = 10
    else:
        cost = 15
    print(f"{name.capitalize()} doit payer {cost}€")
    total_cost += cost

print(f"Le coût total pour la famille est : {total_cost}€")

# ------ Exercise 3
brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"]
    }
}
brand["number_stores"] = 2
print(f"Zara's clients are {', '.join(brand['type_of_clothes'])}.")
brand["country_creation"] = "Spain"

if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")

del brand["creation_date"]
# Affichage
print(brand["international_competitors"][-1]) 

print(brand["major_color"]["US"])

print(len(brand))
print(brand.keys())

more_on_zara = {
    "creation_date": 1975,
    "number_stores": 10000
}


print(more_on_zara)

brand.update(more_on_zara)
print(brand)

print(brand["number_stores"])


# ------ Exercise 4
def describe_city(city, contry = "france"):
    print(f"{city} is in {contry}")

describe_city("casablanca", "Maroc")
# ------ Exercise 5

# ------ Exercise 6

# ------ Exercise 7

# ------ Exercise 8
