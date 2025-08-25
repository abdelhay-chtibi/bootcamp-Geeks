import sys
sys.path.append(r"C:\Users\acer\Documents\Desktop Document\Geeks\bootcamp_geeks_ain_chock\week_1\day_5\mini_project_1")
from game import Game

def get_user_menu_choice():
    """Affiche le menu et récupère le choix de l'utilisateur"""
    print("\n=== Menu ===")
    print("1. Jouer une nouvelle partie")
    print("2. Afficher les scores")
    print("x. Quitter")
    choice = input("Votre choix: ").lower()
    return choice

def print_results(results):
    """Affiche le résumé des scores"""
    print("\n=== Résultats ===")
    print(f"Gagné : {results['win']}")
    print(f"Perdu : {results['loss']}")
    print(f"Égalité : {results['draw']}")
    print("\nMerci d'avoir joué!")

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

if __name__ == "__main__":
    main()
