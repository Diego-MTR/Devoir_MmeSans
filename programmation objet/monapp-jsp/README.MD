# MonApp JSP – Guide de démarrage

## Prérequis

- **Java JDK 8 ou supérieur** installé
- **Maven** installé (`mvn` dans le PATH)
- **Serveur Apache Tomcat 9** (fourni dans le dossier du projet)
- **Serveur de base de données local** (WAMP ou XAMPP recommandé)
- **Fichier SQL fourni** pour créer la base de données

---

## Étapes d'installation

### 1. Créer la base de données

- Lancez **WAMP** ou **XAMPP**.
- Ouvrez **phpMyAdmin** ou un autre outil MySQL.
- Importez le fichier `.sql` fourni dans le dossier du projet pour créer la base et les tables nécessaires.

### 2. Compiler le projet

- Ouvrez un terminal dans le dossier du projet.
- Exécutez la commande suivante pour compiler et générer le fichier `.war` :

  ```
  mvn clean package
  ```

- Le fichier `monapp.war` sera généré dans le dossier `target`.

### 3. Déployer le .war

- Copiez le fichier `target\monapp.war`.
- Collez-le dans le dossier :

  ```
  [chemin-vers-le-projet]\apache-tomcat-9.0.105\webapps\
  ```

### 4. Démarrer le serveur Tomcat

- Allez dans le dossier :

  ```
  [chemin-vers-le-projet]\apache-tomcat-9.0.105\bin
  ```

- Double-cliquez sur **startup.bat** pour lancer Tomcat.

---

## Accéder à l’application

- Ouvrez votre navigateur et allez à :

  ```
  http://localhost:8080/monapp/
  ```

---

## Fonctionnement de l’application

- **Navigation** via le menu latéral (profil, matières, comptes…)
- **Ajout** : cliquez sur le bouton **+** en bas à droite pour ajouter un compte ou une matière
- **Modification/Suppression** : utilisez les boutons ✏️ et 🗑️ à côté de chaque élément
- **Profil** : accédez à votre profil pour modifier vos informations
- **Déconnexion** : bouton dans la barre latérale
- **Création de compte** : accessible depuis la page de connexion ou le menu si vous n’êtes pas connecté

---

## Remarques

- Si vous modifiez la configuration de la base de données, adaptez le fichier `Database.java` avec vos paramètres MySQL.
- Si le port 8080 est déjà utilisé, modifiez-le dans `conf/server.xml` de Tomcat.
- Pour tout problème, vérifiez la console Windows et les logs Tomcat (`logs/`).

---

Projet réalisé dans le cadre du Bachelor – Programmation Objet.