# Projet REST API - Authentification Utilisateur

Ce projet est une API REST développée en Java avec Spring Boot, permettant la gestion de l’authentification des utilisateurs à travers des endpoints sécurisés. Il s’agit d’un exemple pédagogique pour illustrer la création d’une API simple avec gestion de JWT (JSON Web Token).

---

## Fonctionnalités

- **Inscription (`/register`)**  
  Permet à un nouvel utilisateur de s’enregistrer en envoyant un nom d’utilisateur et un mot de passe.

- **Connexion (`/login`)**  
  Permet à un utilisateur de se connecter avec ses identifiants. Si la connexion est réussie, un token JWT est généré et retourné.

- **Sécurisation des endpoints**  
  Les endpoints sensibles peuvent être protégés par le token JWT obtenu lors de la connexion.

---

## Structure du projet

- `src/main/java/` : Code source principal (contrôleurs, services, modèles, configuration sécurité)
- `src/main/resources/` : Fichiers de configuration (application.properties, etc.)
- `src/test/java/` : Tests unitaires
- `pom.xml` : Dépendances Maven et configuration du projet
- `README.md` : Documentation du projet

---

## Prérequis

- Java 17 ou supérieur
- Maven

---

## Lancer le projet

1. Cloner le dépôt :
   ```bash
   git clone <url-du-repo>
   ```
2. Se placer dans le dossier du projet :
   ```bash
   cd <nom-du-projet>
   ```
3. Lancer l’application :
   ```bash
   mvn spring-boot:run
   ```

---

## Exemple d’utilisation avec Postman

### 1. Inscription

**Requête :**
```json
POST /register
{
  "username": "nouvel_utilisateur",
  "password": "motdepasse"
}
```

**Réponse attendue :**
```json
{
  "message": "Utilisateur enregistré avec succès"
}
```

### 2. Connexion

**Requête :**
```json
POST /login
{
  "username": "nouvel_utilisateur",
  "password": "motdepasse"
}
```

**Réponse attendue :**
```json
{
  "token": "eyJhbGciOiJIUzI1NiJ9..."
}
```

---

## Capture d’écran

Voici un aperçu de l’utilisation de l’API avec Postman :

![Aperçu Postman](./Capture%20d%E2%80%99%C3%A9cran%202025-06-04%20114854.png)

---

*Pour toute question, consultez le code source ou ouvrez une issue sur le dépôt GitHub.*