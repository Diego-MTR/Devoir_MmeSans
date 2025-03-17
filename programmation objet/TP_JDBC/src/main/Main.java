package main;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // Paramètres de connexion
        String dbName = "univcergy22";
        String dblogin = "root";
        String motdepasse = "";
        String host = "localhost";  // Modifier ici si l'IP change

        // Création du DAO
        DAOAcces dao = new DAOAcces(dbName, dblogin, motdepasse, host);

        // Menu interactif
        Scanner scanner = new Scanner(System.in);
        int choix;
        do {
            System.out.println("\n--- MENU ---");
            System.out.println("1. Lister les accès");
            System.out.println("2. Ajouter un accès");
            System.out.println("3. Supprimer un accès");
            System.out.println("4. Quitter");
            System.out.print("Choisissez une option : ");
            choix = scanner.nextInt();
            scanner.nextLine(); 

            switch (choix) {
                case 1:
                    for (Acces a : dao.lister()) {
                        System.out.println(a);
                    }
                    break;
                case 2:
                    System.out.print("Nom : ");
                    String prenom = scanner.nextLine();
                    System.out.print("Login : ");
                    String login = scanner.nextLine();
                    System.out.print("Mot de passe : ");
                    String password = scanner.nextLine();
                    System.out.print("Statut : ");
                    String statut = scanner.nextLine();
                    System.out.print("Âge : ");
                    int age = scanner.nextInt();

                    // Création de l'objet Acces avec les valeurs saisies
                    Acces nouvelAcces = new Acces(0, prenom, login, password, statut, age);
                    dao.ajouter(nouvelAcces);
                    break;
                case 3:
                    System.out.print("ID à supprimer : ");
                    int id = scanner.nextInt();

                    //  Création de l'objet Acces avec uniquement l'ID
                    Acces accesASupprimer = new Acces(id, null, null, null, null, 0);
                    dao.supprimer(accesASupprimer);
                    break;
                case 4:
                    System.out.println("Fermeture du programme...");
                    break;
                default:
                    System.out.println("Option invalide, veuillez réessayer.");
            }
        } while (choix != 4);

        // Fermeture de la connexion
        dao.fermer();
        scanner.close();
    }
}
