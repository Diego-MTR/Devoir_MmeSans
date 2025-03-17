![Bataille Navale](./assets/bataille.webp)

# Bataille Navale

Bataille Navale est une implémentation du jeu classique de bataille navale en Python utilisant la bibliothèque Pygame. Le but du jeu est de couler tous les navires de votre adversaire avant qu'il ne coule les vôtres.

## Installation

### Prérequis

- Python 3.x doit être installé sur votre machine. Vous pouvez le télécharger depuis [python.org](https://www.python.org/downloads/).

### Étapes d'installation

1. **Installer Python**:
    - Téléchargez et installez Python depuis [python.org](https://www.python.org/downloads/).
    - Assurez-vous d'ajouter Python à votre PATH lors de l'installation.

2. **Installer Pygame**:
    - Ouvrez une invite de commande (cmd) ou un terminal.
    - Exécutez la commande suivante pour installer Pygame:
      ```sh
      pip install pygame
      ```

3. **Cloner le répertoire du projet**:
    - Téléchargez ou clonez ce répertoire sur votre machine.

## Lancement du jeu

1. **Naviguer vers le répertoire du projet**:
    - Ouvrez une invite de commande (cmd) ou un terminal.
    - Utilisez la commande `cd` pour naviguer vers le répertoire où se trouve `bataille.py`.

2. **Exécuter le jeu**:
    - Exécutez la commande suivante pour lancer le jeu:
      ```sh
      python bataille.py
      ```

## Règles du jeu

- **Placement des navires**:
  - Chaque joueur place ses navires sur une grille de 10x10.
  - Les navires peuvent être placés horizontalement ou verticalement.
  - Les navires ne peuvent pas se chevaucher.

- **Types de navires**:
  - Porte-avions (5 cases)
  - Croiseur (4 cases)
  - Contre-torpilleur (3 cases)
  - Sous-marin (3 cases)
  - Torpilleur (2 cases)

- **Déroulement du jeu**:
  - Les joueurs tirent à tour de rôle pour essayer de toucher et couler les navires adverses.
  - Un tir touché est marqué en rouge, un tir manqué en bleu.
  - Le premier joueur à couler tous les navires adverses gagne.

- **Difficulté**:
  - Vous pouvez choisir entre deux niveaux de difficulté: Facile et Difficile.
  - En mode Difficile, l'ordinateur utilise une stratégie plus avancée pour tirer.

## Interface du jeu

- **Grille du joueur**:
  - Vous placez vos navires sur cette grille.
  - Les navires placés sont marqués en vert.

- **Grille de l'ordinateur**:
  - Vous tirez sur cette grille pour essayer de toucher les navires de l'ordinateur.

- **Indicateurs**:
  - Un label indique à qui est le tour de tirer.
  - Un autre label affiche le nombre de navires restants pour chaque joueur.

## Sons

- Le jeu utilise des effets sonores pour indiquer les tirs touchés, manqués, et les navires coulés.
- Assurez-vous que le dossier `sounds` contient les fichiers suivants:
  - `eau.wav`
  - `explosion.wav`
  - `victory.wav`
  - `defeat.wav`

Amusez-vous bien en jouant à la Bataille Navale !