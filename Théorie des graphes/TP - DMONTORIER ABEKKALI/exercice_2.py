import networkx as nx
import matplotlib.pyplot as plt

# 1. Création du premier graphe (grille carrée 3x3)
G1 = nx.grid_2d_graph(3, 3)  # Graphe en grille 3x3
pos1 = {(x, y): (x, y) for x, y in G1.nodes()}  # Position fixe pour la grille
plt.figure(figsize=(8, 6))
nx.draw(G1, pos=pos1, with_labels=True, node_color='lightblue', font_weight='bold')
plt.title("Graphe en grille (3x3)")
plt.show()


import networkx as nx
import matplotlib.pyplot as plt

# Création du graphe (étoile de David)
G2 = nx.Graph()

# Ajouter des sommets
G2.add_nodes_from(range(6))

# Ajouter les arêtes pour former l'étoile de David
G2.add_edges_from([
    (0, 3), (0, 4),  # Sommets reliés à 0
    (1, 5), (1, 2),  # Sommets reliés à 1
    (2, 1), (2, 5),  # Sommets reliés à 2
    (3, 4), (3, 0),  # Sommets reliés à 3
    (4, 3), (4, 0),  # Sommets reliés à 4
    (5, 1), (5, 2)   # Sommets reliés à 5
])

# Positions fixes pour les sommets en forme d'étoile de David
pos2 = {
    0: (0, 1),   # Haut
    1: (-1, 0.5),  # Gauche supérieur
    2: (1, 0.5),   # Droite supérieur
    3: (-1, -0.5), # Gauche inférieur
    4: (1, -0.5),  # Droite inférieur
    5: (0, -1)     # Bas
}

# Dessiner le graphe
plt.figure(figsize=(8, 6))
nx.draw(G2, pos=pos2, with_labels=True, node_size=500, node_color='lightblue', font_weight='bold')
plt.title("Étoile de David avec connexions correctes")
plt.show()
