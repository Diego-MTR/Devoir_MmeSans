# Exercice 1 : Programmation Immutables

def addToEach(n, lst):
    """Ajoute n à chaque élément de la liste sans modifier la liste originale."""
    return [x + n for x in lst]

def removeDuplicates(lst):
    """Retourne une nouvelle liste sans doublons à partir de la liste donnée."""
    return list(set(lst))

# Exercice 2 : Objets Persistants et Promesses
from dataclasses import dataclass
import random
import asyncio

@dataclass(frozen=True)
class Personne:
    """Structure de données immuable représentant une personne avec un nom et un âge."""
    nom: str
    age: int

def anniversaire(personnes):
    """Retourne une nouvelle liste de personnes avec un âge incrémenté de 1."""
    return [Personne(p.nom, p.age + 1) for p in personnes]

async def getRandomNumber():
    """Retourne un nombre aléatoire entre 1 et 100 après un délai d'une seconde."""
    await asyncio.sleep(1)
    return random.randint(1, 100)

async def main():
    """Génère plusieurs nombres aléatoires et les affiche lorsqu'ils sont résolus."""
    numbers = await asyncio.gather(*(getRandomNumber() for _ in range(5)))
    print(numbers)

# Exercice 3 : Gestion d'Inventaire
@dataclass(frozen=True)
class Article:
    """Structure immuable représentant un article dans l'inventaire."""
    id: int
    nom: str
    prix: float
    stock: int

def ajouter_article(inventaire, article):
    """Ajoute un nouvel article à l'inventaire sans modifier l'original."""
    return inventaire + [article]

def mettre_a_jour_stock(inventaire, article_id, quantite):
    """Met à jour le stock d'un article sans modifier l'inventaire original."""
    return [Article(a.id, a.nom, a.prix, a.stock + quantite) if a.id == article_id else a for a in inventaire]

def passer_commande(inventaire, commande):
    """Retourne un nouvel inventaire après soustraction des articles achetés."""
    return [Article(a.id, a.nom, a.prix, a.stock - commande.get(a.id, 0)) for a in inventaire]

@dataclass(frozen=True)
class Promotion:
    """Représente une promotion avec des conditions et une réduction."""
    nom: str
    condition: dict  # Par exemple, {"montant_min": 50}
    reduction: float

def appliquer_promotions(commande, promotions):
    """Applique les promotions aux commandes et retourne le total après réduction."""
    total = sum(article.prix * quantite for article, quantite in commande.items())
    for promo in promotions:
        if total >= promo.condition.get("montant_min", 0):
            total -= total * promo.reduction
    return total

# Exercice 6 : Réflexion métier

def detecter_reapprovisionnement(inventaire, seuil=5):
    """Détecte les articles ayant un stock inférieur au seuil donné."""
    return [a for a in inventaire if a.stock < seuil]

# Architecture logicielle : Il faut un système de gestion des fournisseurs pour automatiser les commandes.
# Approche asynchrone : Utilisation de tâches asynchrones pour traiter plusieurs commandes en parallèle.
# Mesures de sécurité : Cryptage des données sensibles, authentification des utilisateurs, logs sécurisés.
# Question d'ouverture : En développement web, ces principes aident à gérer l'état de manière prévisible, comme avec React qui utilise des composants immuables et des fonctions pures.
# En intelligence artificielle, l'immuabilité améliore la reproductibilité des expériences et facilite le débogage.
# Les fonctions pures rendent les modèles de machine learning plus faciles à tester et comprendre.


if __name__ == "__main__":
    asyncio.run(main())

