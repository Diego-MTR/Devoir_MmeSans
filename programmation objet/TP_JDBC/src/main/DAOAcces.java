package main;

import java.sql.*;
import java.util.ArrayList;

public class DAOAcces {
    private Connection conn;
    private Statement stmt;

    // Constructeur : Charge le driver et créer la connexion
    public DAOAcces(String dbName, String dblogin, String motdepasse, String host) {
        try {
            String strClassName = "com.mysql.jdbc.Driver";
            String strUrl = "jdbc:mysql://" + host + ":3306/" + dbName + "?useSSL=false";

            Class.forName(strClassName);
            this.conn = DriverManager.getConnection(strUrl, dblogin, motdepasse);
            this.stmt = conn.createStatement();
            System.out.println("Connexion réussie à la base de données !");
        } catch (ClassNotFoundException e) {
            System.err.println("Driver non chargé !");
            e.printStackTrace();
        } catch (SQLException e) {
            System.err.println("Erreur de connexion à la base de données !");
            e.printStackTrace();
        }
    }

    // Fermer la connexion
    public void fermer() {
        try {
            if (stmt != null) stmt.close();
            if (conn != null) conn.close();
            System.out.println("Connexion fermée !");
        } catch (SQLException e) {
            System.err.println("Erreur lors de la fermeture !");
            e.printStackTrace();
        }
    }

    // Lister tous les accès et retourner une liste d'objets Acces
    public ArrayList<Acces> lister() {
        ArrayList<Acces> liste = new ArrayList<>();
        try {
            String query = "SELECT * FROM Acces";
            Statement stmt = conn.createStatement();
            ResultSet rs = stmt.executeQuery(query);

            while (rs.next()) {
                Acces a = new Acces(
                        rs.getInt("id"),
                        rs.getString("prenom"),
                        rs.getString("login"),
                        rs.getString("password"),
                        rs.getString("statut"),
                        rs.getInt("age")
                );
                liste.add(a);
            }
        } catch (SQLException e) {
            System.err.println("Erreur lors de la récupération des données !");
            e.printStackTrace();
        }
        return liste;
    }


    public void ajouter(Acces a) {
        if (a == null) {
            System.err.println("Erreur : L'objet Acces est null !");
            return;
        }
        
        try {
            String query = "INSERT INTO Acces (prenom, login, password, statut, age) VALUES (?, ?, ?, ?, ?)";
            PreparedStatement pstmt = conn.prepareStatement(query);
            pstmt.setString(1, a.getPrenom());
            pstmt.setString(2, a.getLogin());
            pstmt.setString(3, a.getPassword());
            pstmt.setString(4, a.getStatut());
            pstmt.setInt(5, a.getAge());

            int rowsAffected = pstmt.executeUpdate();
            if (rowsAffected > 0) {
                System.out.println("Ajout réussi !");
            }
        } catch (SQLException e) {
            System.err.println("Erreur lors de l'ajout !");
            e.printStackTrace();
        }
    }

    public void supprimer(Acces a) {
        if (a == null) {
            System.err.println("Erreur : L'objet Acces est null !");
            return;
        }

        try {
            String query = "DELETE FROM Acces WHERE id = ?";
            PreparedStatement pstmt = conn.prepareStatement(query);
            pstmt.setInt(1, a.getId());

            int rowsAffected = pstmt.executeUpdate();
            if (rowsAffected > 0) {
                System.out.println("Suppression réussie !");
            } else {
                System.out.println("Aucun enregistrement trouvé avec cet ID.");
            }
        } catch (SQLException e) {
            System.err.println("Erreur lors de la suppression !");
            e.printStackTrace();
        }
    }
}