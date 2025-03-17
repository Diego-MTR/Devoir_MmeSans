package main;

import java.sql.*;

public class Select {
    public static void main(String[] args) {
        try { 
            String strClassName = "com.mysql.jdbc.Driver";
            String dbName = "univcergy22";
            String login = "root";
            String motdepasse = "";

            String strUrl = "jdbc:mysql://localhost:3306/" + dbName + "?useSSL=false";

            Class.forName(strClassName);
            Connection conn = DriverManager.getConnection(strUrl, login, motdepasse);
            Statement stUsers = conn.createStatement();

            ResultSet rsUsers = stUsers.executeQuery("select * from Acces");
            while(rsUsers.next()) {
                System.out.print("Id[" + rsUsers.getInt(1) + "]"
                + rsUsers.getString(2)
                + "[" + rsUsers.getString("statut") + "] "
                + rsUsers.getInt("age") +"\n"); }
            conn.close();
        }
            catch(ClassNotFoundException e) {
                System.err.println("Driver non chargé !");  e.printStackTrace();
            } catch(SQLException e) {
                System.err.println("Autre erreur !");  e.printStackTrace();
            }



    }
}
