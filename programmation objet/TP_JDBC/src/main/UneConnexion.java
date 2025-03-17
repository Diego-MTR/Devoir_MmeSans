package main;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class UneConnexion {

public static void main(String[] args) {
		
		try { 
			String strClassName = "com.mysql.jdbc.Driver";
			String dbName= "univcergy22"; 
			String login= "univcergy22"; 
			String motdepasse= "itescia"; 
			String strUrl = "jdbc:mysql://195.144.11.16:3306/" +  dbName;

			Class.forName(strClassName);
			Connection conn = DriverManager.getConnection(strUrl, login, motdepasse);
			// . . .
			conn.close();
			}
			catch(ClassNotFoundException e) {  
				System.err.println("Driver non chargé !");  e.printStackTrace();
			} catch(SQLException e) {
				System.err.println("Autre erreur !");  e.printStackTrace();
			}

		
		
	}
}
