# TODO: Créer un script pour calculer les ressources nécessaires pour assainir la Seine.
# TODO: Importer les modules nécessaires.
import math

water_quantity = float(input("Quelle quantité d'eau faut-il assainir ? "))
n_filter = water_quantity/5
n_light = water_quantity/5*3
kg_chlorine = water_quantity/10


print(f"""Voici les éléments requis pour assainir {water_quantity}L d'eau:\n
        \t- Filtre(s) : {n_filter}\n
        \t- Lampe(s) UV : {n_light}\n
        \t- Chlore : {kg_chlorine}kg\n""")
