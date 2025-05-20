package controller;

import model.Compte;
import model.dao.CompteDAO;
import javax.servlet.*;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.*;
import java.io.IOException;

@WebServlet("/login")
public class LoginServlet extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        String login = request.getParameter("login");
        String password = request.getParameter("password");
        // Après avoir vérifié le login et le mot de passe
        CompteDAO dao = new CompteDAO();
        Compte compte = dao.getByLogin(login);
        if (new CompteDAO().checkLogin(login, password)) {
            HttpSession session = request.getSession();
            session.setAttribute("user", login);
            session.setAttribute("role", compte.getRole());
            response.sendRedirect("home.jsp");
        } else {
            request.setAttribute("error", "Login ou mot de passe incorrect !");
            request.getRequestDispatcher("login.jsp").forward(request, response);
        }
    }

    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        request.getRequestDispatcher("login.jsp").forward(request, response);
    }
}