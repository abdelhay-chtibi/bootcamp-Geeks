import random

# -------------------------
# Classe Game
# -------------------------
class Game:
    def get_user_item(self):
        """Demande à l'utilisateur de choisir rock, paper ou scissors"""
        while True:
            user_choice = input("Choisissez [rock/paper/scissors]: ").lower()
            if user_choice in ["rock", "paper", "scissors"]:
                return user_choice
            else:
                print("Choix invalide. Essayez encore.")

    def get_computer_item(self):
        """Retourne un choix aléatoire pour l'ordinateur"""
        return random.choice(["rock", "paper", "scissors"])

    def get_game_result(self, user_item, computer_item):
        """Détermine le résultat du jeu"""
        if user_item == computer_item:
            return "draw"
        elif (
            (user_item == "rock" and computer_item == "scissors") or
            (user_item == "paper" and computer_item == "rock") or
            (user_item == "scissors" and computer_item == "paper")
        ):
            return "win"
        else:
            return "loss"

    def play(self):
        """Joue une partie et retourne le résultat"""
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)

        if result == "win":
            print(f"Vous avez choisi {user_item}. L'ordinateur a choisi {computer_item}. Vous avez gagné!")
        elif result == "loss":
            print(f"Vous avez choisi {user_item}. L'ordinateur a choisi {computer_item}. Vous avez perdu!")
        else:
            print(f"Vous avez choisi {user_item}. L'ordinateur a choisi {computer_item}. Égalité!")

        return result

# -------------------------
# Fonctions pour le menu et les scores
# -------------------------
def get_user_menu_choice():
    print("\n=== Menu ===")
    print("1. Jouer une nouvelle partie")
    print("2. Afficher les scores")
    print("x. Quitter")
    choice = input("Votre choix: ").lower()
    return choice

def print_results(results):
    print("\n=== Résultats ===")
    print(f"Gagné : {results['win']}")
    print(f"Perdu : {results['loss']}")
    print(f"Égalité : {results['draw']}")
    print("\nMerci d'avoir joué!")

# -------------------------
# Fonction principale
# -------------------------
def main():
    results = {"win": 0, "loss": 0, "draw": 0}

    while True:
        choice = get_user_menu_choice()

        if choice == "1":
            game = Game()
            result = game.play()
            results[result] += 1  # Incrémente win/loss/draw

        elif choice == "2":
            print_results(results)

        elif choice == "x":
            print_results(results)
            break

        else:
            print("Choix invalide. Réessayez.")

# -------------------------
# Exécution
# -------------------------
if __name__ == "__main__":
    main()
