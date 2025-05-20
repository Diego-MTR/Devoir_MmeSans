package controller;

import model.Compte;
import model.dao.CompteDAO;
import javax.servlet.*;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.*;
import java.io.IOException;

@WebServlet("/register")
public class RegisterServlet extends HttpServlet {
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        String login = req.getParameter("login");
        String password = req.getParameter("password");
        Compte c = new Compte();
        c.setLogin(login);
        c.setPassword(password);
        c.setRole("user");
        new CompteDAO().add(c);
        resp.sendRedirect("login.jsp?notif=register_success");
    }
}