package controller;

import model.dao.CompteDAO;
import model.Compte;
import javax.servlet.*;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.*;
import java.io.IOException;

@WebServlet("/profil")
public class ProfilServlet extends HttpServlet {
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        HttpSession session = req.getSession();
        String oldLogin = (String) session.getAttribute("user");
        if (oldLogin == null) {
            resp.sendRedirect("login.jsp");
            return;
        }
        String newLogin = req.getParameter("login");
        String password = req.getParameter("password");

        CompteDAO dao = new CompteDAO();
        Compte compte = dao.getByLogin(oldLogin);
        compte.setLogin(newLogin);
        if (password != null && !password.isEmpty()) {
            compte.setPassword(password);
        }
        dao.update(compte);
        session.setAttribute("user", newLogin);
        resp.sendRedirect("profil.jsp?notif=success_edit");
    }
}