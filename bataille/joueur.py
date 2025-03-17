# Remove the import of random and bataille
# from bataille import Plateau
# from bataille import random
# from bataille import Navire

from plateau import Plateau
from navire import Navire
import random
from tkinter import messagebox

class Joueur:
    def __init__(self, nom, est_humain=True):
        """
        Initialise un joueur (humain ou ordinateur).
        """
        self.nom = nom  # Nom du joueur
        self.plateau = Plateau()  # Plateau du joueur
        self.est_humain = est_humain  # Indique si le joueur est humain

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

    def tirer(self, adversaire, position):
        """
        Tente un tir sur le plateau de l'adversaire.
        """
        return adversaire.plateau.tirer(position)  # Effectue un tir sur le plateau de l'adversaire


    def tirer_sur_ordinateur(self, x, y):
        """
        Gère un tir sur le plateau de l'ordinateur.
        """
        position = (x, y)

        if self.ordinateur.plateau.grille[x][y] is None:
            print(f"[LOG] Tir à la position {position} manqué.")
            self.computer_buttons[x][y].config(bg="blue", state="disabled")  # Marque la case comme manquée
            self.jouer_son("eau.wav")  # Joue le son de l'eau
        else:
            navire = self.ordinateur.plateau.grille[x][y]
            navire.touchees.append(position)  # Marque la position comme touchée
            print(f"[LOG] Tir à la position {position} a touché le navire {navire.nom}.")
            self.computer_buttons[x][y].config(bg="red", state="disabled")  # Marque la case comme touchée
            self.jouer_son("explosion.wav")  # Joue le son de l'explosion

            if navire.verifier_etat():
                for px, py in navire.positions:
                    self.computer_buttons[px][py].config(bg="darkred", state="disabled")  # Marque le navire comme coulé
                print(f"[LOG] Navire {navire.nom} coulé.")
                self.ordinateur_bateaux_restants -= 1  # Diminue le compteur de navires restants
                self.bateaux_label.config(
                    text=f"Bateaux restants : Joueur = {self.joueur1_bateaux_restants}, Ordinateur = {self.ordinateur_bateaux_restants}"
                )

            self.jouer_son("explosion.wav")  # Joue le son de l'explosion

        if self.verifier_fin_de_jeu():
            return  # Vérifie la fin de jeu

    def tir_ordinateur(self):
        """
        L'ordinateur effectue un tir sur le plateau du joueur.
        """
        while True:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            if self.joueur1.plateau.grille[x][y] is None or isinstance(self.joueur1.plateau.grille[x][y], Navire):
                break  # Sort de la boucle si la case est libre ou contient un navire

        position = (x, y)
        resultat = self.ordinateur.tirer(self.joueur1, position)  # Effectue un tir sur le plateau du joueur

        if resultat == "manqué":
            self.grille_buttons[x][y].config(bg="blue", state="disabled")  # Marque la case comme manquée
            self.jouer_son("eau.wav")  # Joue le son de l'eau
        elif resultat == "touché":
            self.grille_buttons[x][y].config(bg="red", state="disabled")  # Marque la case comme touchée
            self.jouer_son("explosion.wav")  # Joue le son de l'explosion
        elif resultat == "coulé":
            navire = self.joueur1.plateau.grille[x][y]
            for px, py in navire.positions:
                self.grille_buttons[px][py].config(bg="darkred", state="disabled")  # Marque le navire comme coulé
            messagebox.showinfo("Navire touché !", "L'ordinateur a coulé un de vos navires.")
            
            # Diminue le compteur de navires restants
            self.joueur1_bateaux_restants -= 1
            self.bateaux_label.config(
                text=f"Bateaux restants : Joueur 1 = {self.joueur1_bateaux_restants}, Ordinateur = {self.ordinateur_bateaux_restants}"
            )
            self.jouer_son("explosion.wav")  # Joue le son de l'explosion

        # Vérifie la fin de jeu
        if self.verifier_fin_de_jeu():
            return

        # Passe au tour du joueur
        self.tour_joueur = True
        self.label_tour.config(text="À votre tour de tirer !")

    def disable_grids(self):
        """
        Désactive les grilles après la fin de la partie.
        """
        for row in self.grille_buttons:
            for btn in row:
                btn.config(state="disabled")  # Désactive chaque bouton de la grille du joueur

        for row in self.computer_buttons:
            for btn in row:
                btn.config(state="disabled")  # Désactive chaque bouton de la grille de l'ordinateur