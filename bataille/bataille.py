import tkinter as tk
from tkinter import messagebox
import random
from tkinter import ttk  # Import nécessaire pour les Combobox
import pygame
from PIL import Image, ImageTk  # Ajouter ces imports pour gérer les images
import os
from navire import Navire
from plateau import Plateau
from joueur import Joueur


# Définir un chemin absolu vers le dossier "sounds"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Répertoire de bataille.py
SOUNDS_DIR = os.path.join(BASE_DIR, "sounds")  # Répertoire des sons

# Vérification
print("Chemin des sons :", SOUNDS_DIR)


pygame.mixer.init()  # Initialisation de Pygame


def tester_les_sons():
    """
    Teste tous les fichiers sons dans le dossier 'sounds'.
    """
    print("Test des fichiers sons...")
    for fichier in ["eau.wav", "explosion.wav", "victory.wav", "defeat.wav"]:
        chemin = os.path.join(SOUNDS_DIR, fichier)
        if os.path.exists(chemin):
            print(f"Lecture de {fichier}...")
            pygame.mixer.Sound(chemin).play()  # Joue le son
            pygame.time.wait(2000)  # Attendre 2 secondes entre chaque son
        else:
            print(f"Fichier introuvable : {fichier}")


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


# Interface graphique avec Tkinter
class BatailleNavaleApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Jeu de la Bataille Navale")

        # Configure the grid layout to center elements
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_rowconfigure(1, weight=1)
        self.master.grid_rowconfigure(2, weight=1)
        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_columnconfigure(1, weight=1)
        self.master.grid_columnconfigure(2, weight=1)

        # Joueurs
        self.joueur1 = Joueur("Joueur 1")
        self.ordinateur = Joueur("Ordinateur")

        # Phase de placement des navires
        self.navires = [
            Navire("Porte-avions", 5),
            Navire("Croiseur", 4),
            Navire("Paquebot", 6),
            Navire("Mini-yatch", 2),
            Navire("Voilier", 3)
        ]
        
        # Charger l'image d'arrière-plan pour les cases
        water_path = os.path.join(BASE_DIR, "assets", "water.jpg")
        water_image = Image.open(water_path).resize((40, 40))  # Adapter la taille de l'image aux cases
        self.water_photo = ImageTk.PhotoImage(water_image)
        
        self.navire_actuel_index = 0  # Index du navire actuel à placer
        self.positions_actuelles = []  # Positions actuelles du navire
        self.grille_buttons = []  # Boutons de la grille du joueur
        self.computer_buttons = []  # Boutons de la grille de l'ordinateur
        self.nombre_tours = 0  # Nombre de tours joués
        self.tirs_joueur_touches = 0  # Nombre de tirs touchés par le joueur
        self.tirs_joueur_manques = 0  # Nombre de tirs manqués par le joueur
        self.navires_joueur_coules = 0  # Nombre de navires coulés par le joueur

        self.tirs_ordinateur_touches = 0  # Nombre de tirs touchés par l'ordinateur
        self.tirs_ordinateur_manques = 0  # Nombre de tirs manqués par l'ordinateur
        self.navires_ordinateur_coules = 0  # Nombre de navires coulés par l'ordinateur

        # Placement des navires de l'ordinateur
        self.placer_navires_ordinateur()
  

        # Indicateur de tour
        self.tour_joueur = True  # Indique si c'est le tour du joueur
        self.label_tour = tk.Label(
            self.master,
            text="À votre tour de tirer !",
            font=("Arial", 14, "bold"),
            bg="gray",
            fg="white"
        )
        self.label_tour.grid(row=2, column=1, pady=10)  # Centré entre les grilles


        self.orientation = "horizontal"  # Orientation par défaut

        self.orientation_label = tk.Label(self.master, text="Orientation (Ctrl) : Horizontal", font=("Arial", 10))
        self.orientation_label.grid(row=3, column=1)

        self.master.config(bg="gray")

        # Cadre pour les grilles
        self.player_frame = tk.Frame(self.master, bg="gray", padx=5, pady=5)
        self.player_frame.grid(row=1, column=0, padx=10)  # Grille du joueur

        self.computer_frame = tk.Frame(self.master, bg="gray", padx=5, pady=5)
        self.computer_frame.grid(row=1, column=2, padx=10)  # Grille de l'ordinateur

        self.grille_buttons = []  # Boutons de la grille du joueur
        self.computer_buttons = []  # Boutons de la grille de l'ordinateur
        
        # Créer les grilles
        self.create_player_grid()
        self.create_computer_grid()
        
        # Labels pour les grilles
        self.player_label = tk.Label(
            self.master, text="Votre Grille", font=("Arial", 14), bg="gray", fg="white"
        )
        self.player_label.grid(row=0, column=0)

        self.computer_label = tk.Label(
            self.master, text="Grille de l'Ordinateur", font=("Arial", 14), bg="gray", fg="white"
        )
        self.computer_label.grid(row=0, column=2)

        self.joueur1_bateaux_restants = len(self.navires)  # Nombre de navires du joueur 1
        self.ordinateur_bateaux_restants = len(self.navires)  # Nombre de navires de l'ordinateur

        # Label pour afficher le nombre de bateaux restants
        self.bateaux_label = tk.Label(
            self.master,
            text=f"Bateaux restants : Joueur 1 = {self.joueur1_bateaux_restants}, Ordinateur = {self.ordinateur_bateaux_restants}",
            font=("Arial", 12),
            bg="gray",
            fg="white"
        )
        self.bateaux_label.grid(row=4, column=1)
        
        self.master.bind("<Control_L>", self.changer_orientation)
        self.master.bind("<Control_R>", self.changer_orientation)
        
    def afficher_menu_accueil(self):
        """
        Affiche un menu d'accueil avec les règles du jeu.
        """
        self.menu_frame = tk.Frame(self.master, bg="black")
        self.menu_frame.grid(row=0, column=0, columnspan=3, rowspan=3)

        # Titre
        titre_label = tk.Label(
            self.menu_frame,
            text="Bienvenue dans la Bataille Navale",
            font=("Arial", 18, "bold"),
            bg="black",
            fg="white",
            pady=20,
        )
        titre_label.pack()

        # Règles du jeu
        regles = (
            "Rèles du jeu :\n"
            "- Placez vos navires sur votre grille.\n"
            "- Devinez où se trouvent les navires de l'ordinateur.\n"
            "- Un tir touché est marqué en rouge, manqué en bleu.\n"
            "- Le premier à couler tous les navires adverses gagne.\n\n"
            "Cliquez sur Commencer pour jouer."
        )
        regles_label = tk.Label(
            self.menu_frame,
            text=regles,
            font=("Arial", 12),
            bg="black",
            fg="white",
            justify="left",
            padx=20,
            pady=10,
        )
        regles_label.pack()
        
        # Liste déroulante pour choisir la difficulté
        self.difficulte = tk.StringVar()
        self.difficulte.set("Facile")  # Valeur par défaut

        difficulte_label = tk.Label(
            self.menu_frame,
            text="Choisissez la difficulté :",
            font=("Arial", 12),
            bg="gray",
            fg="white",
        )
        difficulte_label.pack(pady=10)

        difficulte_combobox = ttk.Combobox(
            self.menu_frame,
            textvariable=self.difficulte,
            values=["Facile", "Difficile"],
            state="readonly",
        )
        difficulte_combobox.pack()

        # Bouton Commencer
        commencer_button = tk.Button(
            self.menu_frame,
            text="Commencer le jeu",
            font=("Arial", 14),
            bg="green",
            fg="white",
            command=self.lancer_jeu
        )
        commencer_button.pack(pady=20)

    def lancer_jeu(self):
        """
        Ferme le menu d'accueil et affiche la grille du jeu.
        """
        self.menu_frame.destroy()  # Supprime le menu d'accueil

    def create_player_grid(self):
        """
        Création de la grille pour le joueur.
        """
        for i in range(10):
            row = []
            for j in range(10):
                btn = tk.Button(
                    self.player_frame,
                    width=40, height=40, bg="#ADD8E6", relief="raised",
                    bd=2, command=lambda x=i, y=j: self.selectionner_case(x, y)
                )
                btn.config(image=self.water_photo, compound="center")
                btn.grid(row=i, column=j, padx=0, pady=0)  # Suppression de l'espacement
                btn.bind("<Enter>", lambda event, x=i, y=j: self.previsualiser_navire(x, y))
                btn.bind("<Leave>", lambda event, x=i, y=j: self.reinitialiser_previsualisation(x, y))
                row.append(btn)
            self.grille_buttons.append(row)

    def create_computer_grid(self):
        """
        Création de la grille pour l'ordinateur.
        """
        for i in range(10):
            row = []
            for j in range(10):
                btn = tk.Button(
                    self.computer_frame,
                    width=40, height=40, bg="#ADD8E6", relief="raised",
                    bd=2, command=lambda x=i, y=j: self.tirer_sur_ordinateur(x, y)
                )
                btn.config(image=self.water_photo, compound="center")
                btn.grid(row=i, column=j, padx=0, pady=0)  # Suppression de l'espacement
                row.append(btn)
            self.computer_buttons.append(row)

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
            self.orientation_button.destroy()




    def valider_placement(self):
        """
        Valide le placement d'un navire.
        """
        navire = self.navires[self.navire_actuel_index]
        if len(self.positions_actuelles) == navire.taille:
            if self.joueur1.placer_navire_manuellement(navire, self.positions_actuelles):
                messagebox.showinfo("Placement validé", f"{navire.nom} placé !")
                self.navire_actuel_index += 1
                self.positions_actuelles = []

                if self.navire_actuel_index >= len(self.navires):
                    messagebox.showinfo("Placement terminé", "Tous vos navires sont placés.")
                    self.validate_button.config(state="disabled")
                    self.label_tour.config(text="À votre tour de tirer !")
            else:
                messagebox.showerror("Erreur", "Placement invalide. Réessayez.")
        else:
            messagebox.showerror("Erreur", f"Veuillez sélectionner {navire.taille} cases pour le {navire.nom}.")


    def placer_navires_ordinateur(self):
        """
        Place les navires de l'ordinateur sans chevauchement et uniquement des navires autorisés.
        """
        self.ordinateur.plateau = Plateau()  # Réinitialise le plateau

        navires_a_placer = [
            Navire("Porte-avions", 5),
            Navire("Croiseur", 4),
            Navire("Paquebot", 6),
            Navire("Mini-yatch", 2),
            Navire("Voilier", 3)
        ]

        for navire in navires_a_placer:
            while True:
                positions = generer_positions_aleatoires(navire.taille, self.ordinateur.plateau)
                # Vérifie que toutes les positions sont libres
                if all(self.ordinateur.plateau.grille[x][y] is None for x, y in positions):
                    if self.ordinateur.plateau.placer_navire(navire, positions):
                        print(f"[LOG] Navire {navire.nom} placé aux positions : {positions}")
                        break
                    else:
                        print(f"[LOG] Échec du placement pour {navire.nom}. Réessai...")





    def tirer_sur_ordinateur(self, x, y):
        """
        Gère un tir sur le plateau de l'ordinateur.
        """
        self.nombre_tours += 0.5  # Ajout de 0.5 pour compter un tour complet après le tir du joueur.
        if not self.tour_joueur:
            print("[LOG] Tentative de tir alors que ce n'est pas le tour du joueur.")
            return

        position = (x, y)
        resultat = self.joueur1.tirer(self.ordinateur, position)
        print(f"[LOG] Résultat du tir du joueur sur la position {position} : {resultat}")

        if resultat == "manqué":
            self.computer_buttons[x][y].config(bg="blue", state="disabled")
            self.tirs_joueur_manques += 1
            self.jouer_son("eau.wav")
        elif resultat == "touché":
            self.computer_buttons[x][y].config(bg="red", state="disabled")
            self.tirs_joueur_touches += 1
            self.jouer_son("explosion.wav")
        elif resultat == "coulé":
            navire = self.ordinateur.plateau.grille[x][y]
            for px, py in navire.positions:
                self.computer_buttons[px][py].config(bg="darkred", state="disabled")
                self.tirs_joueur_touches += 1
            print(f"[LOG] Navire coulé : {navire.nom}.")
            self.navires_ordinateur_coules += 1
            self.ordinateur_bateaux_restants -= 1
            self.bateaux_label.config(
                text=f"Bateaux restants : Joueur 1 = {self.joueur1_bateaux_restants}, Ordinateur = {self.ordinateur_bateaux_restants}"
            )
            self.jouer_son("explosion.wav")

        if self.verifier_fin_de_jeu():
            return

        # Passe au tour de l'ordinateur
        self.tour_joueur = False
        self.label_tour.config(text="Tour de l'ordinateur")
        self.master.after(1000, self.tir_ordinateur)


    def tir_ordinateur(self):
        """
        L'ordinateur effectue un tir sur le plateau du joueur, en suivant une logique différente selon la difficulté.
        """
        self.nombre_tours += 0.5  # Ajout de 0.5 pour compter un tour complet après le tir du joueur.
        if not hasattr(self, "cibles_prioritaires"):
            self.cibles_prioritaires = []  # Liste pour stocker les cibles prioritaires

        position = None

        # Mode "Difficile" : Priorité aux cases adjacentes si un navire est en cours d'attaque
        if self.difficulte.get() == "Difficile" and self.cibles_prioritaires:
            position = self.cibles_prioritaires.pop(0)
        else:
            # Sinon, tir aléatoire
            while True:
                x = random.randint(0, 9)
                y = random.randint(0, 9)
                if self.joueur1.plateau.grille[x][y] is None or isinstance(self.joueur1.plateau.grille[x][y], Navire):
                    position = (x, y)
                    break

        resultat = self.ordinateur.tirer(self.joueur1, position)
        print(f"[LOG] Résultat du tir de l'ordinateur sur la position {position} : {resultat}")

        if resultat == "manqué":
            self.grille_buttons[position[0]][position[1]].config(bg="blue", state="disabled")
            self.tirs_ordinateur_manques += 1
            self.jouer_son("eau.wav")
        elif resultat == "touché":
            self.grille_buttons[position[0]][position[1]].config(bg="red", state="disabled")
            self.tirs_ordinateur_touches += 1
            self.jouer_son("explosion.wav")

            # Si on est en "Difficile", ajouter les cases adjacentes aux priorités
            if self.difficulte.get() == "Difficile":
                x, y = position
                adjacentes = [
                    (x - 1, y), (x + 1, y),  # Haut et Bas
                    (x, y - 1), (x, y + 1)   # Gauche et Droite
                ]
                for adj in adjacentes:
                    if (0 <= adj[0] < 10 and 0 <= adj[1] < 10 and
                            adj not in self.cibles_prioritaires and
                            (self.joueur1.plateau.grille[adj[0]][adj[1]] is None or
                            isinstance(self.joueur1.plateau.grille[adj[0]][adj[1]], Navire))):
                        self.cibles_prioritaires.append(adj)

        elif resultat == "coulé":
            navire = self.joueur1.plateau.grille[position[0]][position[1]]
            for px, py in navire.positions:
                self.grille_buttons[px][py].config(bg="darkred", state="disabled")
                self.tirs_ordinateur_touches += 1
            print(f"[LOG] Navire coulé par l'ordinateur : {navire.nom}.")
            self.joueur1_bateaux_restants -= 1
            self.navires_joueur_coules += 1
            self.bateaux_label.config(
                text=f"Bateaux restants : Joueur 1 = {self.joueur1_bateaux_restants}, Ordinateur = {self.ordinateur_bateaux_restants}"
            )
            self.jouer_son("explosion.wav")

            # Si un navire est coulé, réinitialiser les priorités
            self.cibles_prioritaires = []

        if self.verifier_fin_de_jeu():
            return
        
        self.tour_joueur = True

        # Passe au tour du joueur
        self.tour_joueur = True
        self.label_tour.config(text="À votre tour de tirer !")
        self.joueur1.verifier_tir_ordinateur()  # Vérifie que l'ordinateur a bien joué


    def jouer_son(self, fichier):
        """
        Joue un son donné.
        """
        try:
            chemin = os.path.join(SOUNDS_DIR, fichier)
            son = pygame.mixer.Sound(chemin)
            son.play()
        except Exception as e:
            print(f"Erreur lors de la lecture du son {fichier}: {e}")



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


                

    def verifier_fin_de_jeu(self):
        """
        Vérifie si la partie est terminée et affiche l'écran de fin si nécessaire.
        """
        if self.ordinateur_bateaux_restants == 0:
            statistiques = (
                f"Tours joués : {self.nombre_tours}\n"
                f"Tirs du joueur :\n"
                f"- Touchés : {self.tirs_joueur_touches}\n"
                f"- Manqués : {self.tirs_joueur_manques}\n"
                f"- Navires coulés : {self.navires_ordinateur_coules}\n\n"
                f"Tirs de l'ordinateur :\n"
                f"- Touchés : {self.tirs_ordinateur_touches}\n"
                f"- Manqués : {self.tirs_ordinateur_manques}\n"
                f"- Navires coulés : {self.navires_joueur_coules}"
            )
            self.afficher_ecran_fin("Victoire ! Félicitations !", statistiques)
            return True
        elif self.joueur1_bateaux_restants == 0:
            statistiques = (
                f"Tours joués : {self.nombre_tours}\n"
                f"Tirs du joueur :\n"
                f"- Touchés : {self.tirs_joueur_touches}\n"
                f"- Manqués : {self.tirs_joueur_manques}\n"
                f"- Navires coulés : {self.navires_ordinateur_coules}\n\n"
                f"Tirs de l'ordinateur :\n"
                f"- Touchés : {self.tirs_ordinateur_touches}\n"
                f"- Manqués : {self.tirs_ordinateur_manques}\n"
                f"- Navires coulés : {self.navires_joueur_coules}"
            )
            self.afficher_ecran_fin("Défaite ! L'ordinateur a gagné.", statistiques)
            return True
        return False


    def fin_partie(self):
        self.disable_grids()
        for x in range(10):
            for y in range(10):
                # Grille du joueur
                if isinstance(self.joueur1.plateau.grille[x][y], Navire):
                    navire = self.joueur1.plateau.grille[x][y]
                    color = "darkred" if navire.verifier_etat() else ("red" if (x, y) in navire.touchees else "green")
                    self.grille_buttons[x][y].config(bg=color)

                # Grille de l'ordinateur
                if isinstance(self.ordinateur.plateau.grille[x][y], Navire):
                    navire = self.ordinateur.plateau.grille[x][y]
                    color = "darkred" if navire.verifier_etat() else ("red" if (x, y) in navire.touchees else "green")
                    self.computer_buttons[x][y].config(bg=color)


            # Ajout d'un bouton pour recommencer
            bouton_recommencer = tk.Button(
                self.master,
                text="Recommencer une partie",
                font=("Arial", 14),
                bg="blue",
                fg="white",
                command=self.recommencer_partie
            )
            bouton_recommencer.grid(row=15, column=0, columnspan=20, pady=10)


    def recommencer_partie(self):
        self.master.destroy()  # Ferme la fenêtre actuelle
        root = tk.Tk()
        app = BatailleNavaleApp(root)  # Nouvelle instance
        app.afficher_menu_accueil()  # Retour au menu d'accueil
        root.mainloop()
        
        
    def afficher_message_fin(self, message):
        """
        Affiche un message de fin de partie dans une fenêtre popup.
        """
        import tkinter as tk
        from tkinter import messagebox

        # Crée une fenêtre popup
        fin_popup = tk.Toplevel()
        fin_popup.title("Fin de la partie")

        # Texte du message
        label_message = tk.Label(fin_popup, text=message, font=("Helvetica", 14))
        label_message.pack(pady=20)

        # Bouton pour fermer le jeu ou recommencer
        bouton_rejouer = tk.Button(
            fin_popup,
            text="Rejouer",
            command=lambda: [fin_popup.destroy(), self.reinitialiser_jeu()],
            font=("Helvetica", 12)
        )
        bouton_rejouer.pack(pady=10)

        bouton_quitter = tk.Button(
            fin_popup,
            text="Quitter",
            command=self.root.quit,
            font=("Helvetica", 12)
        )
        bouton_quitter.pack(pady=10)

        fin_popup.transient(self.root)  # Centre par rapport à la fenêtre principale
        fin_popup.grab_set()           # Bloque les interactions avec la fenêtre principale
        self.root.wait_window(fin_popup)
        
    def reinitialiser_jeu(self):
        """
        Réinitialise la partie en recréant les grilles et les navires.
        """
        self.joueur1_bateaux_restants = 2
        self.ordinateur_bateaux_restants = 2
        self.creer_grilles()
        self.placer_navires_ordinateur()
        self.rafraichir_interface()
        print("[LOG] Partie réinitialisée.")

        
    def rafraichir_interface(self):
        """
        Met à jour l'interface graphique après une réinitialisation.
        """
        # Effacer les grilles existantes
        for widget in self.frame_grille_joueur.winfo_children():
            widget.destroy()
        for widget in self.frame_grille_ordinateur.winfo_children():
            widget.destroy()

        # Recréer les boutons de la grille
        self.creer_interface_grille(self.frame_grille_joueur, self.joueur1, est_joueur=True)
        self.creer_interface_grille(self.frame_grille_ordinateur, self.ordinateur, est_joueur=False)

        print("[LOG] Interface graphique rafraîchie.")
                    
                   
                    
    def afficher_ecran_fin(self, message, statistiques=None):
        """
        Affiche l'écran de fin avec un message et les statistiques si disponibles.
        """

        self.ecran_fin = tk.Frame(self.master, bg="gray", padx=50, pady=40)
        self.ecran_fin.place(relx=0.5, rely=0.35, anchor=tk.CENTER)  # Ajustement de la hauteur

        if "Victoire" in message:
            self.jouer_son("victory.wav")
        elif "Défaite" in message:
            self.jouer_son("defeat.wav")
            self.ecran_fin = tk.Frame(self.master, bg="gray", padx=50, pady=40)
            self.ecran_fin.place(relx=0.5, rely=0.35, anchor=tk.CENTER)  # Ajustement de la hauteur

        # Titre
        titre_label = tk.Label(
            self.ecran_fin,
            text=message,
            font=("Arial", 18, "bold"),
            bg="gray",
            fg="white",
            pady=20,
        )
        titre_label.pack()

        if statistiques:
            stats_label = tk.Label(
                self.ecran_fin,
                text=statistiques,
                font=("Arial", 12),
                bg="gray",
                fg="white",
                justify="left",
            )
            stats_label.pack()

        bouton_rejouer = tk.Button(
            self.ecran_fin,
            text="Rejouer",
            font=("Arial", 14),
            bg="green",
            fg="white",
            command=self.recommencer_partie,
        )
        bouton_rejouer.pack(pady=20)

        bouton_quitter = tk.Button(
            self.ecran_fin,
            text="Quitter",
            font=("Arial", 14),
            bg="red",
            fg="white",
            command=self.master.quit,
        )
        bouton_quitter.pack(pady=10)
