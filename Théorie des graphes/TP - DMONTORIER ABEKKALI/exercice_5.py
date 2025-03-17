import networkx as nx
import matplotlib.pyplot as plt

# 1. Création du graphe
G = nx.Graph()
# Ajouter des sommets
G.add_nodes_from(range(1, 9))
# Ajouter des arêtes avec des poids
edges = [
    (1, 2, 2), (1, 4, 1), (2, 3, 3), (2, 4, 3),
    (3, 5, 1), (4, 5, 1), (4, 6, 6), (5, 6, 4),
    (5, 7, 5), (6, 8, 2), (7, 8, 9)
]
G.add_weighted_edges_from(edges)

# Récupérer les attributs pour l'affichage
pos = nx.spring_layout(G)
labels_edges = nx.get_edge_attributes(G, 'weight')

# Représenter le graphe initial
plt.figure(figsize=(10, 8))
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=700, font_weight='bold')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels_edges)
plt.title("Graphe initial")
plt.show()

# 2. Vérification des sommets isolés et ajout d'une indication sur le graphique
def testnoeudisole(graph):
    for node in graph.nodes:
        if graph.degree[node] == 0:  # Un sommet est isolé s'il n'a pas de voisins
            return True
    return False

isolated = testnoeudisole(G)

# 3. Trouver l'arbre couvrant minimal
def AlgoACM(graph):
    mst = nx.minimum_spanning_tree(graph, weight='weight')
    return mst

ACM = AlgoACM(G)

# 4. Représenter l'arbre couvrant minimal avec indication du poids total
pos_mst = nx.spring_layout(ACM)  # Recalculer les positions pour l'ACM
labels_edges_mst = nx.get_edge_attributes(ACM, 'weight')

plt.figure(figsize=(10, 8))
nx.draw(ACM, pos_mst, with_labels=True, node_color='lightgreen', node_size=700, font_weight='bold')
nx.draw_networkx_edge_labels(ACM, pos_mst, edge_labels=labels_edges_mst)

# Calculer et afficher le poids total sur le graphique
total_weight = sum(nx.get_edge_attributes(ACM, 'weight').values())
plt.text(0, -1.2, f"Poids total : {total_weight}", fontsize=12, color='red', ha='center')

# Afficher si des sommets isolés existent
plt.text(0, -1.4, f"Contient des sommets isolés : {'Oui' if isolated else 'Non'}", fontsize=12, color='blue', ha='center')

plt.title("Arbre couvrant minimal")
plt.show()
