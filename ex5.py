#TODO: Analyser la chaîne de caractères saisie et compter le nombre de médailles.
#      Attention si la chaîne est invalide, un message d'erreur est attendu.

country = input("Pays concerné ? ")
code_medals = input("Chaine représentant les médailles ? ")
G = 0
S = 0
B = 0

for j in code_medals:
    if j == "G":
        G += 1
    elif j == "S":
        S += 1
    elif j == "B":
        B += 1
    if j == code_medals[len(code_medals) - 1]:
        print(f"{country}:\n- {G} OR\n- {S} Argent\n- {B} Bronze\n")
    else:
        print("Ceci est une chaîne invalide.")
        break



