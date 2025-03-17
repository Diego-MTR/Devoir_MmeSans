import tkinter as tk
from tkinter import messagebox


class Plateau:
    def __init__(self, taille=10):
        """
        Initialise un plateau de jeu avec une grille.
        """
        self.taille = taille  # Taille de la grille
        self.grille = [[None for _ in range(taille)] for _ in range(taille)]  # Grille initialisée avec des None
        self.navires = []  # Liste des navires placés


    def est_position_valide(self, positions):
        """
        Vérifie si toutes les positions sont valides (dans la grille et libres).
        """
        for x, y in positions:
            if not (0 <= x < self.taille and 0 <= y < self.taille) or self.grille[x][y] is not None:
                return False  # Position invalide si hors de la grille ou déjà occupée
        return True  # Toutes les positions sont valides

    def placer_navire(self, navire, positions):
        """
        Place un navire sur le plateau.
        """
        if self.est_position_valide(positions):
            for x, y in positions:
                self.grille[x][y] = navire  # Place le navire sur chaque position
            navire.ajouter_positions(positions)  # Ajoute les positions au navire
            self.navires.append(navire)  # Ajoute le navire à la liste des navires
            return True  # Placement réussi
        return False  # Placement échoué

    def tirer(self, position):
        """
        Tente un tir sur une position.
        """
        x, y = position
        if not (0 <= x < self.taille and 0 <= y < self.taille):
            print(f"[LOG] Position {position} invalide pour un tir.")
            return "invalide"  # Position invalide

        if self.grille[x][y] is None:
            print(f"[LOG] Tir à la position {position} manqué.")
            return "manqué"  # Tir manqué
        else:
            navire = self.grille[x][y]
            navire.est_touche(position)  # Marque la position comme touchée
            print(f"[LOG] Positions du navire {navire.nom} : {navire.positions}")
            print(f"[LOG] Positions touchées : {navire.touchees}")

            if navire.verifier_etat():
                print(f"[LOG] Navire {navire.nom} coulé avec succès.")
                return "coulé"  # Navire coulé
            print(f"[LOG] Tir à la position {position} a touché le navire {navire.nom}.")
            return "touché"  # Navire touché
        

    def disable_grids(self):
        """
        Désactive les grilles après la fin de la partie.
        """
        for row in self.grille_buttons:
            for btn in row:
                btn.config(state="disabled")
        for row in self.computer_buttons:
            for btn in row:
                btn.config(state="disabled")
        

    def changer_orientation(self, event=None):
        """
        Change l'orientation entre horizontal et vertical et réinitialise les couleurs des cases prévisualisées.
        """
        if self.orientation == "horizontal":
            self.orientation = "vertical"
        else:
            self.orientation = "horizontal"

        # Met à jour le label d'orientation
        self.orientation_label.config(text=f"Orientation (Ctrl) : {self.orientation.capitalize()}")

        # Réinitialise les couleurs des cases prévisualisées
        for row in self.grille_buttons:
            for btn in row:
                if btn.cget("bg") == "lightgreen":
                    btn.config(bg="#ADD8E6")  # Bleu clair

        # Vérifie si tous les navires sont placés et supprime les widgets
        if self.navire_actuel_index >= len(self.navires):
            self.orientation_label.destroy()
            self.orientation_button.destroy()



    def disable_player_grid(self):
        """
        Désactive la grille du joueur après la fin de la partie.
        """
        for row in self.grille_buttons:
            for btn in row:
                btn.config(state="disabled")
                
                

    def creer_grilles(self):
        """
        Crée ou réinitialise les grilles du joueur et de l'ordinateur.
        """
        # Réinitialiser les grilles
        self.joueur1.grille = [[None for _ in range(10)] for _ in range(10)]
        self.ordinateur.grille = [[None for _ in range(10)] for _ in range(10)]

        # Réinitialiser les navires
        self.joueur1.navires = []
        self.ordinateur.navires = []

        print("[LOG] Grilles réinitialisées.")

    def creer_interface_grille(self, frame, joueur, est_joueur):
        """
        Crée l'interface graphique pour une grille.
        """
        for i in range(10):
            for j in range(10):
                btn = tk.Button(frame, text=" ", width=2, height=1)
                btn.grid(row=i, column=j)
                
                if est_joueur:
                    # Actions spécifiques pour la grille du joueur
                    pass
                else:
                    # Actions spécifiques pour la grille de l'ordinateur
                    btn.config(command=lambda x=i, y=j: self.tirer_sur_ordinateur(x, y))



                    
    def selectionner_case(self, x, y):
        """
        Permet au joueur de sélectionner les cases pour placer un navire.
        """
        navire = self.navires[self.navire_actuel_index]
        positions = []

        if self.orientation == "horizontal":
            positions = [(x, y + i) for i in range(navire.taille) if y + i < 10]
        else:  # Vertical
            positions = [(x + i, y) for i in range(navire.taille) if x + i < 10]

        if len(positions) == navire.taille and self.joueur1.plateau.est_position_valide(positions):
            # Place le navire immédiatement
            if self.joueur1.placer_navire_manuellement(navire, positions):
                for px, py in positions:
                    self.grille_buttons[px][py].config(bg="lightgreen", state="disabled")  # Vert clair pour les navires placés
                self.navire_actuel_index += 1
                if self.navire_actuel_index >= len(self.navires):
                    self.label_tour.config(text="À votre tour de tirer !")
                    # Remettre les cases des navires en vert foncé
                    for navire in self.navires:
                        for px, py in navire.positions:
                            self.grille_buttons[px][py].config(bg="green")
            else:
                messagebox.showerror("Erreur", "Placement invalide. Réessayez.")
        else:
            messagebox.showerror("Erreur", f"Veuillez sélectionner {navire.taille} cases valides pour le {navire.nom}.")
        if self.navire_actuel_index >= len(self.navires):
            messagebox.showinfo("Placement terminé", "Tous vos navires sont placés.")
            self.label_tour.config(text="À votre tour de tirer !")
            
            # Supprime les boutons et labels liés à l'orientation
            self.orientation_label.destroy()




    def previsualiser_navire(self, x, y):
        """
        Colorie les cases en vert pour prévisualiser le placement du navire.
        Si le placement est invalide, colorie les cases en orange.
        """
        navire = self.navires[self.navire_actuel_index]
        positions = []

        if self.orientation == "horizontal":
            positions = [(x, y + i) for i in range(navire.taille) if y + i < 10]
        else:  # Vertical
            positions = [(x + i, y) for i in range(navire.taille) if x + i < 10]

        if len(positions) == navire.taille:
            if self.joueur1.plateau.est_position_valide(positions):
                for px, py in positions:
                    if self.grille_buttons[px][py].cget("bg") != "green":  # Ignorer les cases déjà validées
                        self.grille_buttons[px][py].config(bg="lightgreen")
            else:
                for px, py in positions:
                    if px < 10 and py < 10:
                        self.grille_buttons[px][py].config(bg="orange")

    def reinitialiser_previsualisation(self, x, y):
        """
        Réinitialise les couleurs des cases après le survol, sauf pour les cases validées.
        """
        if self.navire_actuel_index >= len(self.navires):  # Vérifie si tous les navires ont été placés
            return

        navire = self.navires[self.navire_actuel_index]
        positions = []

        if self.orientation == "horizontal":
            positions = [(x, y + i) for i in range(navire.taille) if y + i < 10]
        else:  # Vertical
            positions = [(x + i, y) for i in range(navire.taille) if x + i < 10]

        if len(positions) == navire.taille:
            for px, py in positions:
                if self.grille_buttons[px][py].cget("bg") in ["lightgreen", "orange"]:  # Réinitialiser uniquement les cases en prévisualisation
                    self.grille_buttons[px][py].config(bg="#ADD8E6")  # Bleu clair