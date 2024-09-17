# TODO: Calculer la distance qu'un poids peut atteindre en utilisant la formule de la portée d'un projectile.
# TODO: Importer les modules nécessaires.

import math

speed = float(input("Vitesse initiale (m/s): "))
angle = float(input("Angle de lancer (en degrés): "))
distance = round(((speed ** 2) * math.sin(2 * angle / 360 * (math.pi * 2))) / 9.8, 2)

print(f"Distance parcourue: {distance}m")
