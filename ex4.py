# TODO: Écrire un programme qui demande le pourcentage de charge actuel de la batterie du bateau,
#        calcule la distance restante en km en fonction de ce pourcentage,
#        et affiche le résultat au format "XX km".
#        Assurez une gestion du pourcentage valide au cours de votre programme (% toujours dans [0 ; 100]).

battery_level = float(input("Quelle est votre pourcentage de batterie ? "))

while   battery_level < 0 or battery_level > 100 :

    print("Votre niveau de batterie est erronée")
    battery_level = float(input("Reentrez le bon niveau de batterie : "))

if 50 < battery_level <= 100 :
    distance = battery_level * 2 

if 25 < battery_level <= 50 :
    distance = battery_level * 0.5 

if 10 < battery_level <= 25 :
    distance = battery_level * 1 

if 5 < battery_level <= 10 :
    distance = battery_level * 2.5 

if 0 < battery_level <= 5 :
    distance = battery_level * 6 

if battery_level == 0 :
    print("La batterie est vide.")

print(f"La distance possible est de {distance} km.")
    
