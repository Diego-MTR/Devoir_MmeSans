import csv
from functools import reduce

# Lire les données du fichier CSV
with open('employes.csv', mode='r', encoding='utf-8-sig') as file:
    reader = csv.DictReader(file, delimiter=';')
    employes = list(reader)

# Convertir tous les noms en majuscules
for employe in employes:
    if 'Nom' in employe:
        employe['Nom'] = employe['Nom'].upper()

# Filtrer les employés avec un salaire supérieur à 50 000 euros
employes_salaire_sup_50000 = list(filter(lambda x: float(x['Salaire']) > 50000, employes))

# Calculer le salaire total des employés filtrés
salaire_total = reduce(lambda x, y: x + y, [float(emp['Salaire']) for emp in employes_salaire_sup_50000])

# Ajouter une colonne pour indiquer le niveau de l'employé
for employe in employes:
    salaire = float(employe['Salaire'])
    if salaire < 30000:
        employe['Niveau'] = 'Junior'
    elif 30000 <= salaire <= 50000:
        employe['Niveau'] = 'Intermédiaire'
    else:
        employe['Niveau'] = 'Senior'

# Écrire les données modifiées dans un nouveau fichier CSV
with open('C:\\Users\\diego\\OneDrive\\BACHELOR\\Cours\\Paradigmes de programmation\\paradigme\\employes_modifies.csv', mode='w', encoding='utf-8', newline='') as file:
    fieldnames = ['Nom', 'Âge', 'Salaire', 'Niveau']
    writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=';')

    writer.writeheader()
    writer.writerows(employes)

# Afficher toutes les informations
print("Informations des employés :")
for employe in employes:
    print(employe)
    
print("Salaire total des employés filtrés :", salaire_total)

print("Employés avec un salaire supérieur à 50 000 euros :")
for employe in employes_salaire_sup_50000:
    print(employe)

print("Données mises à jour enregistrées dans 'employes_modifies.csv'.")
