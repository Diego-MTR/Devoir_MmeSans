# TP : Théorie des Graphes

**Diego MONTORIER - ADAM BEKKALI**
**Bachelor Groupe 4**
**09/12/2024**

## Introduction

Dans ce TP, nous utilisons la bibliothèque `NetworkX` pour manipuler et représenter des graphes en Python. La bibliothèque `matplotlib` est utilisée pour afficher les graphes visuellement.

---

## Questions et Réponses

### **Exercice 1 :**
1. **Comment créer un graphe non orienté et un graphe orienté ?**
   - Un graphe non orienté se crée avec :
     ```python
     G = nx.Graph()
     ```
   - Un graphe orienté se crée avec :
     ```python
     G = nx.DiGraph()
     ```

2. **Quelle est la différence entre `add_node` et `add_nodes_from` ?**
   - `add_node` : Ajoute un seul sommet.
     ```python
     G.add_node(1)  # Ajoute le sommet 1
     ```
   - `add_nodes_from` : Ajoute plusieurs sommets à partir d'une liste.
     ```python
     G.add_nodes_from([1, 2, 3])  # Ajoute les sommets 1, 2, 3
     ```

3. **Comment ajouter une arête pondérée dans un graphe ?**
   - Avec l'argument `weight` :
     ```python
     G.add_edge(1, 2, weight=4)  # Ajoute une arête entre 1 et 2 avec un poids de 4
     ```

4. **Que fait la méthode `write_adjlist` ?**
   - Elle sauvegarde le graphe dans un fichier texte au format "liste d'adjacence". Par exemple :
     ```python
     nx.write_adjlist(G, "graphe.txt")
     ```

5. **Différences entre les graphes avant et après le chargement :**
   - Le graphe sauvegardé peut être rechargé avec `read_adjlist`, mais les positions des nœuds ou les attributs supplémentaires peuvent être perdus si non spécifiés dans le fichier.

---

### **Exercice 5 :**
1. **Étapes pour représenter un graphe avec `NetworkX` :**
   - **Créer un graphe** : Ajouter des sommets et des arêtes.
   - **Ajouter des attributs** (poids, couleurs, etc.).
   - **Définir une disposition** pour organiser les sommets avec des fonctions comme `spring_layout`.
   - **Dessiner le graphe** avec :
     ```python
     nx.draw()
     nx.draw_networkx_labels()
     nx.draw_networkx_edge_labels()
     ```

2. **Comment vérifier si un sommet est isolé ?**
   - Une fonction Python comme :
     ```python
     def testnoeudisole(graph):
         for node in graph.nodes:
             if graph.degree[node] == 0:
                 return True
         return False
     ```

3. **Que fait la fonction `nx.cycle_basis` ?**
   - Elle retourne une liste de cycles indépendants dans un graphe non orienté, utile pour analyser les connexions.

4. **Arbre couvrant minimal (ACM) :**
   - On peut le trouver avec `nx.minimum_spanning_tree`.
   - Exemple :
     ```python
     mst = nx.minimum_spanning_tree(G, weight='weight')
     ```

---

## Instructions pour Exécuter le TP

### **Prérequis : Installer les bibliothèques**
Avant d'exécuter les scripts, installez les bibliothèques nécessaires avec :
```bash
pip install networkx matplotlib
```
```bash
pip install networkx networkx
```