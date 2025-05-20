package controller;

import model.Compte;
import model.dao.CompteDAO;
import javax.servlet.*;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.*;
import java.io.IOException;
import java.util.List;

@WebServlet("/compte")
public class CompteServlet extends HttpServlet {
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        String action = req.getParameter("action");
        CompteDAO dao = new CompteDAO();

        if ("edit".equals(action)) {
            int id = Integer.parseInt(req.getParameter("id"));
            Compte c = dao.getById(id);
            req.setAttribute("compte", c);
            req.getRequestDispatcher("editCompte.jsp").forward(req, resp);
            return;
        } else if ("delete".equals(action)) {
            int id = Integer.parseInt(req.getParameter("id"));
            dao.delete(id);
            resp.sendRedirect("compte?notif=success_delete");
            return;
        } else {
            List<Compte> comptes = dao.getAll();
            req.setAttribute("comptes", comptes);
            req.getRequestDispatcher("comptes.jsp").forward(req, resp);
            return;
        }
    }

    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        String idStr = req.getParameter("id");
        String login = req.getParameter("login");
        String password = req.getParameter("password");
        String role = req.getParameter("role");

        Compte c = new Compte();
        c.setLogin(login);
        c.setPassword(password);
        c.setRole(role);

        CompteDAO dao = new CompteDAO();
        if (idStr == null || idStr.isEmpty()) {
            dao.add(c);
            resp.sendRedirect("compte?notif=success_add");
            return;
        } else {
            c.setId(Integer.parseInt(idStr));
            dao.update(c);
            resp.sendRedirect("compte?notif=success_edit");
            return;
        }
    }
}