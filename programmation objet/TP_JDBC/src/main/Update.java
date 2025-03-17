package main;

import java.sql.*;
import java.util.Scanner;

public class Update {
    public static void main(String[] args) {
        try {
            String strClassName = "com.mysql.jdbc.Driver";
            String dbName = "univcergy22";
            String login = "root";
            String motdepasse = "";
            String strUrl = "jdbc:mysql://localhost:3306/" + dbName + "?useSSL=false";

            // Charger le driver MySQL
            Class.forName(strClassName);
            Connection conn = DriverManager.getConnection(strUrl, login, motdepasse);

            // Demander l'ID et le nouveau statut
            Scanner scanner = new Scanner(System.in);
            System.out.print("Entrez l'ID dont vous voulez modifier le statut : ");
            int id = scanner.nextInt();
            scanner.nextLine();  // Consommer la ligne restante

            System.out.print("Entrez le nouveau statut : ");
            String nouveauStatut = scanner.nextLine();
            scanner.close();

            // Requête SQL de mise à jour
            String query = "UPDATE Acces SET statut = ? WHERE id = ?";
            PreparedStatement pstmt = conn.prepareStatement(query);
            pstmt.setString(1, nouveauStatut);
            pstmt.setInt(2, id);

            // Exécuter la mise à jour
            int rowsAffected = pstmt.executeUpdate();
            if (rowsAffected > 0) {
                System.out.println("Mise à jour réussie !");
            } else {
                System.out.println("Aucun enregistrement trouvé avec cet ID.");
            }

            // Fermer la connexion
            conn.close();
        }
        catch (ClassNotFoundException e) {
            System.err.println("Driver non chargé !");
            e.printStackTrace();
        }
        catch (SQLException e) {
            System.err.println("Erreur SQL !");
            e.printStackTrace();
        }
    }
}
