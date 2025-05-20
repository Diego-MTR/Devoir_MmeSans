<!-- filepath: c:\Users\diego\OneDrive\BACHELOR\Cours\Devoir MmeSans\programmation objet\monapp-jsp\src\main\webapp\profil.jsp -->
<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<%@ page import="model.dao.CompteDAO,model.Compte" %>
<%
    String login = (String) session.getAttribute("user");
    String role = (String) session.getAttribute("role");
    Compte compte = null;
    if (login != null) {
        compte = new model.dao.CompteDAO().getByLogin(login);
    }
%>
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Mon Profil</title>
    <link rel="stylesheet" href="css/style.css">
    <style>
    .profil-container {
        max-width: 400px;
        margin: 60px auto;
        background: #fff;
        border-radius: 10px;
        box-shadow: 0 2px 16px rgba(0,0,0,0.10);
        padding: 32px 28px;
    }
    .profil-info {
        margin-bottom: 24px;
        text-align: center;
    }
    .profil-info span {
        display: block;
        font-size: 1.1em;
        margin-bottom: 8px;
    }
    .profil-btn {
        display: block;
        margin: 0 auto 18px auto;
        padding: 10px 24px;
        background: #2e7dff;
        color: #fff;
        border: none;
        border-radius: 5px;
        font-size: 1em;
        cursor: pointer;
        transition: background 0.2s;
    }
    .profil-btn:hover {
        background: #1b4fa0;
    }
    .profil-form {
        display: none;
        margin-top: 18px;
    }
    .profil-form input {
        width: 100%;
        margin-bottom: 14px;
        padding: 10px;
        border-radius: 5px;
        border: 1px solid #bbb;
        font-size: 1em;
    }
    .profil-form button {
        width: 100%;
        padding: 12px;
        background: #27ae60;
        color: #fff;
        border: none;
        border-radius: 5px;
        font-size: 1.1em;
        cursor: pointer;
        transition: background 0.2s;
    }
    .profil-form button:hover {
        background: #219150;
    }
    </style>
    <script>
    function showEditForm() {
        document.getElementById("profil-form").style.display = "block";
        document.getElementById("edit-btn").style.display = "none";
    }
    </script>
</head>
<body>
    <div class="sidebar">
        <h2>MonApp</h2>
        <a href="profil.jsp">🙍‍♂️ Profil</a>
        <a href="home.jsp">🏠 Accueil</a>
        <a href="matiere">📚 Voir les matières</a>
        <a href="compte">👤 Voir les comptes</a>
        <a href="logout" class="btn">Déconnexion</a>
    </div>
    <div class="main-content">
        <div class="header">
            <h1>Mon Profil</h1>
        </div>
        <div class="profil-container">
        <% if (login != null && compte != null) { %>
            <div class="profil-info">
                <span><strong>Nom d'utilisateur :</strong> <%= compte.getLogin() %></span>
                <span><strong>Rôle :</strong> <%= compte.getRole() %></span>
            </div>
            <button id="edit-btn" class="profil-btn" onclick="showEditForm()">Modifier mon profil</button>
            <form id="profil-form" class="profil-form" method="post" action="profil">
                <input type="text" name="login" value="<%= compte.getLogin() %>" required placeholder="Nom d'utilisateur">
                <input type="password" name="password" placeholder="Nouveau mot de passe (laisser vide pour ne pas changer)">
                <button type="submit">Enregistrer les modifications</button>
            </form>
        <% } else { %>
            <p>Vous devez être connecté pour voir cette page.</p>
        <% } %>
        </div>
        <%
            String notif = request.getParameter("notif");
            if ("success_edit".equals(notif)) {
        %>
        <script>
            notify("Profil modifié avec succès", "success");
        </script>
        <%
            }
        %>
    </div>
</body>
</html>