# Fonction pour saisir les données des étudiants
def saisir_donnees():
    # Demander le nombre d'étudiants
    nombres_etudiants = int(input("Combien d'étudiants souhaitez-vous saisir ? "))
    noms = []  # Liste pour stocker les noms des étudiants
    notes = []  # Liste pour stocker les notes des étudiants

    # Boucle pour saisir le nom et la note de chaque étudiant
    for i in range(nombres_etudiants):
        nom = input(f"Nom de l'étudiant {i + 1} : ")
        note = float(input(f"Note de {nom} : "))
        noms.append(nom)
        notes.append(note)

    return noms, notes  # Retourner les listes de noms et de notes

# Fonction pour calculer la moyenne des notes
def calculer_moyenne(notes):
    return sum(notes) / len(notes)  # Retourner la moyenne

# Fonction pour afficher la répartition des réussites et des échecs
def afficher_repartition(noms, notes):
    reussite = []  # Liste pour stocker les noms des étudiants ayant réussi
    echec = []  # Liste pour stocker les noms des étudiants en échec

    # Boucle pour classer les étudiants en fonction de leurs notes
    for i in range(len(notes)):
        if notes[i] >= 10:
            reussite.append(noms[i])
        else:
            echec.append(noms[i])

    # Afficher les noms des étudiants ayant réussi et échoué
    print("\nÉtudiants ayant réussi :", ", ".join(reussite))
    print("Étudiants en échec :", ", ".join(echec))

# Fonction pour trouver et afficher l'étudiant avec la meilleure note
def meilleure_note(noms, notes):
    index_meilleure_note = notes.index(max(notes))  # Trouver l'index de la meilleure note
    print(f"\nL'étudiant ayant la meilleure note est {noms[index_meilleure_note]} avec {notes[index_meilleure_note]}.")

def trier_etudiants(noms, notes):
    # Combiner les noms et les notes dans une liste de tuples
    etudiants = list(zip(noms, notes))
    # Trier les étudiants par note décroissante
    etudiants_triees = sorted(etudiants, key=lambda x: x[1], reverse=True)
    
    # Afficher les étudiants triés avec leurs notes
    print("\nClassement des étudiants par note décroissante :")
    for nom, note in etudiants_triees:
        print(f"{nom} : {note}")
        
def rechercher_etudiants(noms, notes):
    nom_recherche = input("\nEntrez le nom de l'étudiant à rechercher : ")
    if nom_recherche in noms:
        index_etudiant = noms.index(nom_recherche)
        print(f"L'étudiant {nom_recherche} a obtenu la note {notes[index_etudiant]}.")
    else:
        print(f"L'étudiant {nom_recherche} n'a pas été trouvé dans la liste.")


# Fonction principale pour exécuter le programme
def main():
    noms, notes = saisir_donnees()  # Saisir les données des étudiants

    moyenne = calculer_moyenne(notes)  # Calculer la moyenne des notes
    print(f"\nLa moyenne de la classe est de {moyenne:.2f}.")

    afficher_repartition(noms, notes)  # Afficher la répartition des réussites et des échecs
    meilleure_note(noms, notes)  # Afficher l'étudiant avec la meilleure note
    trier_etudiants(noms, notes)    # Afficher le tri par ordre décroissant des notes
    rechercher_etudiants(noms, notes)  # Rechercher un étudiant par son nom


# Point d'entrée du programme
if __name__ == "__main__":
    main()
