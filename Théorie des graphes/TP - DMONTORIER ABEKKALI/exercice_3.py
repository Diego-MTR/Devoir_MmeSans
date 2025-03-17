import networkx as nx
import matplotlib.pyplot as plt
import random

# 1. Choisir un nombre aléatoire de sommets
num_nodes = random.randint(2, 15)
print(f"Nombre de sommets : {num_nodes}")

# 2. Créer un graphe vide
G = nx.Graph()

# 3. Ajouter les sommets
for i in range(num_nodes):
    G.add_node(i, label=f"Sommet {i}", col=random.choice(['red', 'blue', 'green']))

# 4. Ajouter des arêtes aléatoires avec des poids
for i in range(num_nodes):
    for j in range(i + 1, num_nodes):  # Éviter les doublons
        if random.choice([True, False]):  # 50% de chance d'ajouter une arête
            weight = random.randint(1, 10)
            G.add_edge(i, j, weight=weight)

# 5. Récupérer les attributs des nœuds et des arêtes
node_colors = [G.nodes[node]['col'] for node in G.nodes]
labels_nodes = {node: G.nodes[node]['label'] for node in G.nodes}
labels_edges = nx.get_edge_attributes(G, 'weight')

# 6. Définir une disposition pour le graphe
pos = nx.spring_layout(G)

# 7. Représentation du graphe avec sommets de taille réduite
plt.figure(figsize=(10, 8))
nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=300, alpha=0.8)  # Taille réduite
nx.draw_networkx_labels(G, pos, labels=labels_nodes, font_size=10)
nx.draw_networkx_edges(G, pos, width=1.5, alpha=0.5)  # Épaisseur ajustée
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels_edges, font_color='black', font_size=8)
plt.title("Graphe non orienté généré aléatoirement avec sommets ajustés")
plt.axis('off')
plt.show()

# 8. Afficher les informations du graphe
print(f"Sommets du graphe : {list(G.nodes(data=True))}")
print(f"Arêtes du graphe : {list(G.edges(data=True))}")
