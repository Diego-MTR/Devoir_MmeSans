import tkinter as tk  # Importation du module tkinter pour créer des interfaces graphiques
from bataille import BatailleNavaleApp  # Importation de la classe BatailleNavaleApp depuis le module bataille

class main:  
    # Lancement de l'application
    if __name__ == "__main__":
        root = tk.Tk()  # Crée la fenêtre principale de l'application
        app = BatailleNavaleApp(root)  # Crée une instance de l'application BatailleNavaleApp
        app.afficher_menu_accueil()  # Affiche le menu d'accueil
        root.mainloop()  # Démarre la boucle principale de l'application 