package model.dao;

import model.Compte;
import java.sql.*;
import java.util.*;

public class CompteDAO {
    public boolean checkLogin(String login, String password) {
        String sql = "SELECT * FROM compte WHERE login=? AND password=?";
        try (Connection conn = Database.getInstance();
                PreparedStatement ps = conn.prepareStatement(sql)) {
            ps.setString(1, login);
            ps.setString(2, password);
            ResultSet rs = ps.executeQuery();
            return rs.next();
        } catch (SQLException e) {
            e.printStackTrace();
            return false;
        }
    }

    public List<Compte> getAll() {
        List<Compte> comptes = new ArrayList<>();
        String sql = "SELECT * FROM compte";
        try (Connection conn = Database.getInstance();
                Statement st = conn.createStatement();
                ResultSet rs = st.executeQuery(sql)) {
            while (rs.next()) {
                Compte c = new Compte();
                c.setId(rs.getInt("id"));
                c.setLogin(rs.getString("login"));
                c.setPassword(rs.getString("password"));
                c.setRole(rs.getString("role"));
                comptes.add(c);
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return comptes;
    }

    public Compte getById(int id) {
        String sql = "SELECT * FROM compte WHERE id=?";
        try (Connection conn = Database.getInstance();
                PreparedStatement ps = conn.prepareStatement(sql)) {
            ps.setInt(1, id);
            ResultSet rs = ps.executeQuery();
            if (rs.next()) {
                Compte c = new Compte();
                c.setId(rs.getInt("id"));
                c.setLogin(rs.getString("login"));
                c.setPassword(rs.getString("password"));
                c.setRole(rs.getString("role"));
                return c;
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return null;
    }

    public Compte getByLogin(String login) {
        String sql = "SELECT * FROM compte WHERE login=?";
        try (Connection conn = Database.getInstance();
                PreparedStatement ps = conn.prepareStatement(sql)) {
            ps.setString(1, login);
            ResultSet rs = ps.executeQuery();
            if (rs.next()) {
                Compte c = new Compte();
                c.setId(rs.getInt("id"));
                c.setLogin(rs.getString("login"));
                c.setPassword(rs.getString("password"));
                c.setRole(rs.getString("role"));
                return c;
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return null;
    }

    public void add(Compte c) {
        String sql = "INSERT INTO compte (login, password, role) VALUES (?, ?, ?)";
        try (Connection conn = Database.getInstance();
                PreparedStatement ps = conn.prepareStatement(sql)) {
            ps.setString(1, c.getLogin());
            ps.setString(2, c.getPassword());
            ps.setString(3, c.getRole());
            ps.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void update(Compte c) {
        String sql = "UPDATE compte SET login=?, password=?, role=? WHERE id=?";
        try (Connection conn = Database.getInstance();
                PreparedStatement ps = conn.prepareStatement(sql)) {
            ps.setString(1, c.getLogin());
            ps.setString(2, c.getPassword());
            ps.setString(3, c.getRole());
            ps.setInt(4, c.getId());
            ps.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void delete(int id) {
        String sql = "DELETE FROM compte WHERE id=?";
        try (Connection conn = Database.getInstance();
                PreparedStatement ps = conn.prepareStatement(sql)) {
            ps.setInt(1, id);
            ps.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}