#TODO: Analyser la chaîne de caractères saisie et compter le nombre de médailles.
#      Attention si la chaîne est invalide, un message d'erreur est attendu.

country = input("Pays concerné ? ")
medals = input("Chaine représentant les médailles ? ")
G = 0
S = 0
B = 0

for i in range (len(medals)):
    if medals[i] == "G":
        G += 1
    elif medals[i] == "S":
        S += 1
    elif medals[i] == "B":
        B += 1
    else:
        print("Ceci est une chaine invalide.")
        break
    if i == (len(medals) - 1):
        print(f"{country}:\n- {G} Or\n- {S} Argent\n- {B} Bronze")
