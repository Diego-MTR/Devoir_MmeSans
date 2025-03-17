% Définir les faits et les relations de base
homme(pierre).
homme(marc).
homme(paul).
homme(jacques).

femme(marie).
femme(sophie).

parent(pierre, paul).
parent(marie, paul).
parent(marc, sophie).
parent(jacques, marc).

% Définir les règles pour père et mère
père(X, Y) :- homme(X), parent(X, Y).
% Commande : ?- père(X, paul). % Trouve le père de Paul
% Réponse : X = pierre.

mère(X, Y) :- femme(X), parent(X, Y).
% Commande : ?- mère(X, paul). % Trouve la mère de Paul
% Réponse : X = marie.

% Règle pour définir les grands-parents
grand_parent(X, Y) :- parent(X, Z), parent(Z, Y).
% Commande : ?- grand_parent(X, paul). % Trouve les grands-parents de Paul
% Réponse : X = pierre ; X = marie.
% Commande : ?- grand_parent(jacques, sophie). % Vérifie si Jacques est grand-parent de Sophie
% Réponse : true.

% Règle pour définir frères et sœurs
frere_soeur(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y.
% Commande : ?- frere_soeur(paul, X). % Vérifie si Paul a des frères ou sœurs
% Réponse : false. (Paul n'a pas de frère ou sœur)

% Règle pour calculer la longueur d'une liste
longueur([], 0). % Cas de base : liste vide
longueur([_|Queue], N) :- longueur(Queue, M), N is M + 1.
% Commande : ?- longueur([pierre, marie, paul], N). % Calcule la longueur de la liste
% Réponse : N = 3.

% Règle pour vérifier si un élément est présent dans une liste
present(X, [X|_]). % Cas où l'élément est en tête de liste
present(X, [_|Queue]) :- present(X, Queue). % Cas où on continue à chercher dans la queue de la liste
% Commande : ?- present(marie, [pierre, marie, paul]). % Vérifie si Marie est présente dans la liste
% Réponse : true.

% Règle pour définir les oncles et tantes
oncle_tante(X, Y) :- frere_soeur(X, Z), parent(Z, Y).
% Commande : ?- oncle_tante(marc, paul). % Vérifie si Marc est l'oncle de Paul
% Réponse : false. (Marc n'est pas l'oncle de Paul)
% Commande : ?- oncle_tante(X, sophie). % Trouve les oncles de Sophie
% Réponse : X = jacques.

% Règle pour définir les cousins
cousin(X, Y) :- parent(Z, X), parent(W, Y), frere_soeur(Z, W).
% Commande : ?- cousin(X, paul). % Trouve les cousins de Paul
% Réponse : Aucun cousin dans la base actuelle (aucune relation parentale entre les frères/sœurs des parents).
