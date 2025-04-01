# Projet Générateur de Personnages

## Description
Ce projet est une application Java permettant de créer, personnaliser et gérer des personnages dans un univers RPG. Il utilise des concepts avancés de programmation orientée objet tels que les patrons de conception (Builder, Decorator, Singleton) pour offrir une architecture modulaire et extensible.

## Fonctionnalités
- **Création de personnages** : Utilisation du patron Builder pour construire des personnages avec des caractéristiques personnalisées.
- **Ajout de capacités dynamiques** : Utilisation du patron Decorator pour ajouter des capacités comme l'invisibilité, la télépathie ou la résistance au feu.
- **Gestion d'équipes** : Création et gestion d'équipes de personnages, avec calcul de la puissance totale.
- **Simulation de combats** : Comparaison des niveaux de puissance pour déterminer le vainqueur d'un combat.
- **Validation des règles** : Vérification des limites de points de caractéristiques via un singleton `GameSettings`.

## Structure du Projet
Le projet est organisé en plusieurs packages pour une meilleure modularité :

### `rpg.core`
- **`Character`** : Classe représentant un personnage de base.
- **`Party`** : Classe pour gérer une équipe de personnages.

### `rpg.builder`
- **`CharacterBuilder`** : Classe permettant de construire un personnage en plusieurs étapes.

### `rpg.decorator`
- **`CharacterDecorator`** : Classe abstraite pour ajouter dynamiquement des capacités aux personnages.
- **Capacités** : `Invisibility`, `FireResistance`, `Telepathy`, etc.

### `rpg.dao`
- **`DAO<T>`** : Interface générique pour l'accès aux données.
- **`CharacterDAO`** : Implémentation pour gérer les personnages.

### `rpg.settings`
- **`GameSettings`** : Singleton contenant les règles globales du jeu (ex. : limite de points de caractéristiques).

### `rpg.main`
- **`Main`** : Point d'entrée de l'application, avec des exemples d'utilisation.

## Exemples d'Utilisation
### Création d'un personnage
```java
Character thief = new CharacterBuilder()
    .setName("Voleur")
    .setStrength(20)
    .setAgility(40)
    .setIntelligence(30)
    .build();
```

### Ajout de capacités
```java
Character enhancedThief = new Invisibility(new FireResistance(thief));
```

### Gestion d'une équipe
```java
Party party = new Party("Aventuriers");
party.addCharacter(thief);
party.addCharacter(enhancedThief);
System.out.println("Puissance totale : " + party.getTotalPowerLevel());
```

### Simulation de combat
```java
System.out.println(Party.simulateCombat(thief, enhancedThief));
```

## Prérequis
- **Java 20** : Le projet utilise des fonctionnalités compatibles avec Java 20.
- **IDE** : Un IDE comme IntelliJ IDEA est recommandé pour exécuter et modifier le projet.

## Installation
1. Clonez le dépôt :
   ```bash
   git clone https://github.com/Diego-MTR/Devoir_MmeSans.git
   ```
2. Ouvrez le projet dans votre IDE.
3. Configurez le SDK Java 20 dans les paramètres du projet.
4. Exécutez la classe `Main` pour tester les fonctionnalités.

## Contribution
Les contributions sont les bienvenues ! Veuillez suivre les étapes suivantes :
1. Forkez le dépôt.
2. Créez une branche pour vos modifications :
   ```bash
   git checkout -b feature/nom-de-la-fonctionnalite
   ```
3. Faites vos modifications et soumettez une pull request.

## Auteur
- **Diego MTR** : Étudiant en programmation orientée objet.

## Licence
Ce projet est sous licence MIT. Consultez le fichier `LICENSE` pour plus d'informations.