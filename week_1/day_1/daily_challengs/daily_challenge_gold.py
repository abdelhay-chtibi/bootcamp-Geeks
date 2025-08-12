from datetime import datetime

while True:
    birthdate_str = input("Enter your birthdate (DD/MM/YYYY): ")
    try:
        birthdate = datetime.strptime(birthdate_str, "%d/%m/%Y")
        age = datetime.now().year - birthdate.year
        nombre_bougies = int(str(age)[-1]) or 1  # éviter 0 bougie

        # Calculer l'espacement pour centrer les bougies
        largeur_gateau = 19
        bougies_str = "i" * nombre_bougies
        espace_avant = (largeur_gateau - len(bougies_str)) // 2

        print("  " + " " * espace_avant + bougies_str)
        print("      -----------  ")
        print("     |:H:a:p:p:y:|")
        print("   __|___________|__")
        print("  |^^^^^^^^^^^^^^^^^|")
        print("  |:B:i:r:t:h:d:a:y:|")
        print("  |                 |")
        print("  ~~~~~~~~~~~~~~~~~~~")
        break
    except ValueError:
        print("Invalid date format. Please use DD/MM/YYYY.")
