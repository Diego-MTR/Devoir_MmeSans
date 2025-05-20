package model.dao;

import model.Matiere;
import java.sql.*;
import java.util.*;

public class MatiereDAO {
    public List<Matiere> getAll() {
        List<Matiere> matieres = new ArrayList<>();
        String sql = "SELECT * FROM matiere";
        try (Connection conn = Database.getInstance();
                Statement st = conn.createStatement();
                ResultSet rs = st.executeQuery(sql)) {
            while (rs.next()) {
                Matiere m = new Matiere();
                m.setId(rs.getInt("id"));
                m.setNom(rs.getString("nom"));
                m.setNbHeures(rs.getInt("nb_heures"));
                matieres.add(m);
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return matieres;
    }

    public Matiere getById(int id) {
        String sql = "SELECT * FROM matiere WHERE id=?";
        try (Connection conn = Database.getInstance();
                PreparedStatement ps = conn.prepareStatement(sql)) {
            ps.setInt(1, id);
            ResultSet rs = ps.executeQuery();
            if (rs.next()) {
                Matiere m = new Matiere();
                m.setId(rs.getInt("id"));
                m.setNom(rs.getString("nom"));
                m.setNbHeures(rs.getInt("nb_heures"));
                return m;
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return null;
    }

    public void add(Matiere m) {
        String sql = "INSERT INTO matiere (nom, nb_heures) VALUES (?, ?)";
        try (Connection conn = Database.getInstance();
                PreparedStatement ps = conn.prepareStatement(sql)) {
            ps.setString(1, m.getNom());
            ps.setInt(2, m.getNbHeures());
            ps.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void update(Matiere m) {
        String sql = "UPDATE matiere SET nom=?, nb_heures=? WHERE id=?";
        try (Connection conn = Database.getInstance();
                PreparedStatement ps = conn.prepareStatement(sql)) {
            ps.setString(1, m.getNom());
            ps.setInt(2, m.getNbHeures());
            ps.setInt(3, m.getId());
            ps.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void delete(int id) {
        String sql = "DELETE FROM matiere WHERE id=?";
        try (Connection conn = Database.getInstance();
                PreparedStatement ps = conn.prepareStatement(sql)) {
            ps.setInt(1, id);
            ps.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}