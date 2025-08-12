# ------ Challenge 1
ma_Liste = []
number = int(input("Entrez un nombre entier : "))
length = int(input("Entrez la longueur : "))
for i in range(length):
    #print(number * (i + 1) )
    ma_Liste.append(number * (i + 1))

print(ma_Liste)

# ------ Challenge 2

mot = input("Entrez un mot : ")
mot_sans_doublon = ""
for lettre in mot:
    if lettre not in mot_sans_doublon:
        mot_sans_doublon += lettre  
print(f"le mot sans doublon est : {mot_sans_doublon}")
