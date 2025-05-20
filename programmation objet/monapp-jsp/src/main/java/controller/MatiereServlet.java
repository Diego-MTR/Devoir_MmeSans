package controller;

import model.Matiere;
import model.dao.MatiereDAO;
import javax.servlet.*;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.*;
import java.io.IOException;
import java.util.List;

@WebServlet("/matiere")
public class MatiereServlet extends HttpServlet {
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        String action = req.getParameter("action");
        MatiereDAO dao = new MatiereDAO();

        if ("edit".equals(action)) {
            int id = Integer.parseInt(req.getParameter("id"));
            Matiere m = dao.getById(id);
            req.setAttribute("matiere", m);
            req.getRequestDispatcher("editMatiere.jsp").forward(req, resp);
            return;
        } else if ("delete".equals(action)) {
            int id = Integer.parseInt(req.getParameter("id"));
            dao.delete(id);
            resp.sendRedirect("matiere?notif=success_delete");
            return;
        } else {
            List<Matiere> matieres = dao.getAll();
            req.setAttribute("matieres", matieres);
            req.getRequestDispatcher("matieres.jsp").forward(req, resp);
            return;
        }
    }

    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        String idStr = req.getParameter("id");
        String nom = req.getParameter("nom");
        String nbHeuresStr = req.getParameter("nb_heures");

        Matiere m = new Matiere();
        m.setNom(nom);
        m.setNbHeures(Integer.parseInt(nbHeuresStr));

        MatiereDAO dao = new MatiereDAO();
        if (idStr == null || idStr.isEmpty()) {
            dao.add(m);
            resp.sendRedirect("matiere?notif=success_add");
            return;
        } else {
            m.setId(Integer.parseInt(idStr));
            dao.update(m);
            resp.sendRedirect("matiere?notif=success_edit");
            return;
        }
    }
}