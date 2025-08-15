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
import random

def guess_number(user_number):
    # Vérification que le nombre est entre 1 et 100
    if user_number < 1 or user_number > 100:
        print("Veuillez entrer un nombre entre 1 et 100.")
        return
    
    # Générer un nombre aléatoire entre 1 et 100
    random_number = random.randint(1, 100)
    
    # Comparaison
    if user_number == random_number:
        print(f"Bravo ! Vous avez deviné le bon nombre : {random_number} !")
    else:
        print(f"Dommage  Votre nombre : {user_number}, Nombre généré : {random_number}")


try:
    user_input = int(input("Entrez un nombre entre 1 et 100 : "))
    guess_number(user_input)
except ValueError:
    print("Erreur : veuillez entrer un nombre entier valide.")

# ------ Exercise 6
def make_shirt(size="Large", text="I love Python"):
    print(f"The size of the shirt is {size} and the text is '{text}'.")

make_shirt("Large", "Hello World!")
make_shirt()
make_shirt(size="Medium")
make_shirt("Small", "Coding is Life")
make_shirt(text="Custom Message", size="XL")

# ------ Exercise 7
import random

def get_season_from_month(month):
    if month in [12, 1, 2]:
        return "winter"
    elif month in [3, 4, 5]:
        return "spring"
    elif month in [6, 7, 8]:
        return "summer"
    elif month in [9, 10, 11]:
        return "autumn"
    else:
        return None

# Génère une température aléatoire en fonction de la saison
def get_random_temp(season):
    if season == "winter":
        return round(random.uniform(-10, 16), 1)  
    elif season == "spring":
        return round(random.uniform(5, 20), 1)
    elif season == "summer":
        return round(random.uniform(20, 40), 1)
    elif season == "autumn":
        return round(random.uniform(5, 25), 1)
    else:
        return round(random.uniform(-10, 40), 1)

def main():
    mois = int(input("Entrez le numéro du mois (1 = Janvier, 12 = Décembre) : "))
    season = get_season_from_month(mois)

    if season is None:
        print("Mois invalide. Utilisation de la saison par défaut.")
        season = "default"

    temperature = get_random_temp(season)
    print(f"\nLa saison est {season.capitalize()}, et la température actuelle est de {temperature}°C.\n")

    
    if temperature < 0:
        print("Brrr, il fait glacial ! Porte plusieurs couches aujourd'hui.")
    elif 0 <= temperature <= 16:
        print("Il fait assez froid, n'oublie pas ton manteau.")
    elif 17 <= temperature <= 23:
        print("Il fait doux, profite bien de ta journée.")
    elif 24 <= temperature <= 32:
        print("Il fait chaud, pense à bien t'hydrater.")
    else:  # >32
        print("Waouh, il fait très chaud ! Reste à l'ombre et bois beaucoup d'eau.")

main()

# ------ Exercise 8
# Quiz Data
data = [
    {"question": "What is Baby Yoda's real name?", "answer": "Grogu"},
    {"question": "Where did Obi-Wan take Luke after his birth?", "answer": "Tatooine"},
    {"question": "What year did the first Star Wars movie come out?", "answer": "1977"},
    {"question": "Who built C-3PO?", "answer": "Anakin Skywalker"},
    {"question": "Anakin Skywalker grew up to be who?", "answer": "Darth Vader"},
    {"question": "What species is Chewbacca?", "answer": "Wookiee"}
]

# Function to ask questions and check answers
def ask_questions():
    correct = 0
    incorrect = 0
    wrong_answers = []

    print("\n--- Welcome to the Star Wars Quiz! ---\n")

    for item in data:
        user_answer = input(item["question"] + " ").strip()
        if user_answer.lower() == item["answer"].lower():
            print("✅ Correct!\n")
            correct += 1
        else:
            print(f"❌ Wrong! The correct answer was: {item['answer']}\n")
            incorrect += 1
            wrong_answers.append({
                "question": item["question"],
                "your_answer": user_answer,
                "correct_answer": item["answer"]
            })

    return correct, incorrect, wrong_answers

# Function to display results
def show_results(correct, incorrect, wrong_answers):
    print("\n--- Quiz Results ---")
    print(f"✅ Correct answers: {correct}")
    print(f"❌ Wrong answers: {incorrect}\n")

    if incorrect > 0:
        print("Here are the questions you got wrong:\n")
        for item in wrong_answers:
            print(f"Question: {item['question']}")
            print(f"Your answer: {item['your_answer']}")
            print(f"Correct answer: {item['correct_answer']}\n")

    if incorrect > 3:
        replay = input("You had more than 3 wrong answers. Do you want to play again? (yes/no): ").strip().lower()
        if replay == "yes":
            start_quiz()
        else:
            print("Thanks for playing! May the Force be with you!")
    else:
        print("Great job! You know your Star Wars well! 🌟")

def start_quiz():
    correct, incorrect, wrong_answers = ask_questions()
    show_results(correct, incorrect, wrong_answers)

# Start the quiz
start_quiz()
