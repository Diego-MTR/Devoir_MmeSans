package main;

import java.sql.*;
import java.util.Scanner;

public class Delete {
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

            // Demander l'identifiant à supprimer
            Scanner scanner = new Scanner(System.in);
            System.out.print("Entrez l'ID à supprimer : ");
            int id = scanner.nextInt();
            scanner.close();

            // Requête SQL de suppression
            String query = "DELETE FROM Acces WHERE id = ?";
            PreparedStatement pstmt = conn.prepareStatement(query);
            pstmt.setInt(1, id);

            // Exécuter la suppression
            int rowsAffected = pstmt.executeUpdate();
            if (rowsAffected > 0) {
                System.out.println("Suppression réussie !");
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
