# TODO: Écrire un programme qui demande le pourcentage de charge actuel de la batterie du bateau,
#        calcule la distance restante en km en fonction de ce pourcentage,
#        et affiche le résultat au format "XX km".
#        Assurez une gestion du pourcentage valide au cours de votre programme (% toujours dans [0 ; 100]).

battery_pourcentage = float(input("Pourcentage de batterie ? "))

while battery_pourcentage < 0 or battery_pourcentage > 100:
    battery_pourcentage = float(input("Pourcentage de batterie ? "))

if battery_pourcentage == 0:
    print(f"La batterie est vide")

elif battery_pourcentage >= 50:
    distance = (battery_pourcentage - 50) * 2 + (25 * 0.5) + (15 * 1) + (5 * 2.5) + (5 * 6)
    print(f"{distance:.1f} km")

elif battery_pourcentage >= 25:
    distance = (battery_pourcentage - 25) * 0.5 + (15 * 1) + (5 * 2.5) + (5 * 6)
    print(f"{distance:.1f} km")

elif battery_pourcentage >= 10:
    distance = (battery_pourcentage - 10) + (5 * 2.5) + (5 * 6)
    print(f"{distance:.1f} km")

elif battery_pourcentage >= 5:
    distance = (battery_pourcentage - 5) * 2.5 + (5 * 6)
    print(f"{distance:.1f} km")

else:
    distance = battery_pourcentage * 6
    print(f"{distance:.1f} km")



    
