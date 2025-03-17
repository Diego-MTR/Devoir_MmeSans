import networkx as nx
import matplotlib.pyplot as plt

# 1. Création des graphes
G = nx.Graph()  # Graphe non orienté
DG = nx.DiGraph()  # Graphe orienté

# 2. Ajouter des sommets aux graphes
sommets = [1, 2, 3, 4, 5]
G.add_nodes_from(sommets)
DG.add_nodes_from(sommets)

# 3. Afficher les sommets des graphes
print(f"Sommets du graphe non orienté G : {list(G.nodes)}")
print(f"Sommets du graphe orienté DG : {list(DG.nodes)}")

# 4. Supprimer un sommet (exemple pour le graphe non orienté)
G.remove_node(1)
print(f"Sommets après suppression de 1 dans G : {list(G.nodes)}")

# 5. Ajouter des arêtes aux graphes
G.add_edges_from([(2, 3), (2, 5), (3, 4), (4, 5)])
DG.add_edges_from([(1, 3), (2, 3), (2, 4), (2, 5), (4, 5), (5, 1)])

# 6. Représenter le graphe non orienté
plt.figure(figsize=(8, 6))
nx.draw(G, with_labels=True, node_color='lightblue', font_weight='bold')
plt.title("Graphe non orienté G")
plt.show()

# 7. Représenter le graphe orienté
plt.figure(figsize=(8, 6))
nx.draw(DG, with_labels=True, node_color='lightgreen', font_weight='bold', arrowsize=20)
plt.title("Graphe orienté DG")
plt.show()


