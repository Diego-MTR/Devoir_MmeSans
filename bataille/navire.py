import random
from bataille import random

class Navire:
    def __init__(self, nom, taille):
        """
        Initialise un navire avec un nom, une taille, et garde en mémoire ses positions.
        """
        self.nom = nom  # Nom du navire
        self.taille = taille  # Taille du navire
        self.positions = []  # Positions occupées par le navire
        self.touchees = []  # Positions touchées
        self.est_coule_flag = False  # État du navire (coulé ou non)

    def ajouter_positions(self, positions):
        """
        Définit les positions du navire.
        """
        self.positions = positions  # Définit les positions du navire
        print(f"[LOG] Navire {self.nom} placé aux positions : {self.positions}")
        

    def est_touche(self, position):
        """
        Marque une position comme touchée.
        """
        if position in self.positions and position not in self.touchees:
            self.touchees.append(position)  # Ajoute la position aux touchées
            print(f"[LOG] Navire {self.nom} touché à la position : {position}")
        else:
            print(f"[LOG] Navire {self.nom} déjà touché ou position invalide : {position}")

    def verifier_etat(self):
        """
        Vérifie si le navire est complètement coulé.
        """
        if all(position in self.touchees for position in self.positions):
            self.est_coule_flag = True  # Marque le navire comme coulé
            print(f"[LOG] Navire {self.nom} est maintenant coulé avec succès.")
            return True  # Navire coulé
        return False  # Navire non coulé
    
    
    # Fonction pour générer des positions aléatoires pour les navires
    def generer_positions_aleatoires(taille, plateau):
        """
        Génère une liste de positions valides aléatoires pour un navire.
        """
        while True:
            orientation = random.choice(["horizontal", "vertical"])  # Choisit une orientation aléatoire
            if orientation == "horizontal":
                ligne = random.randint(0, plateau.taille - 1)
                colonne = random.randint(0, plateau.taille - taille)
                positions = [(ligne, colonne + i) for i in range(taille)]
            else:  # Vertical
                ligne = random.randint(0, plateau.taille - taille)
                colonne = random.randint(0, plateau.taille - 1)
                positions = [(ligne + i, colonne) for i in range(taille)]

            # Vérifie que toutes les positions sont valides et libres
            if plateau.est_position_valide(positions):
                return positions


    def placer_navire_manuellement(self, navire, positions):
            """
            Permet à un joueur humain de placer un navire.
            """
            return self.plateau.placer_navire(navire, positions)  # Place le navire sur le plateau

    def placer_navires_aleatoirement(self, navires):
            """
            Place les navires aléatoirement (pour l'ordinateur).
            """
            for navire in navires:
                while True:
                    orientation = random.choice(["horizontal", "vertical"])  # Choisit une orientation aléatoire
                    if orientation == "horizontal":
                        ligne = random.randint(0, self.plateau.taille - 1)
                        colonne = random.randint(0, self.plateau.taille - navire.taille)
                        positions = [(ligne, colonne + i) for i in range(navire.taille)]
                    else:  # Vertical
                        ligne = random.randint(0, self.plateau.taille - navire.taille)
                        colonne = random.randint(0, self.plateau.taille - 1)
                        positions = [(ligne + i, colonne) for i in range(navire.taille)]

                    if self.plateau.placer_navire(navire, positions):
                        break  # Sort de la boucle si le navire est placé avec succès