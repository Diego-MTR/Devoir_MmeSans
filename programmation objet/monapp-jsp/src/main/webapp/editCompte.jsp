<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<!DOCTYPE html>
<html lang="fr">
<head>
    <script>
    function notify(msg, type = "info") {
        let notif = document.createElement("div");
        notif.className = "notif " + type;
        notif.innerText = msg;
        document.body.appendChild(notif);
        setTimeout(() => notif.remove(), 3000);
    }
    function confirmAction(msg, url) {
        if (confirm(msg)) {
            window.location = url;
        }
        return false;
    }
    </script>
    <style>
    .notif {
        position: fixed;
        top: 30px; right: 30px;
        background: #2e7dff;
        color: #fff;
        padding: 16px 32px;
        border-radius: 6px;
        font-size: 1.1em;
        z-index: 9999;
        box-shadow: 0 2px 8px rgba(0,0,0,0.15);
        opacity: 0.95;
        animation: fadein 0.5s;
    }
    .notif.error { background: #e74c3c; }
    .notif.success { background: #27ae60; }
    @keyframes fadein { from { opacity: 0; top: 0; } to { opacity: 0.95; top: 30px; } }
    </style>
    <meta charset="UTF-8">
    <title>Éditer Compte</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <div class="sidebar">
        <h2>MonApp</h2>
        <a href="home.jsp">🏠 Accueil</a>
        <a href="matiere">📚 Voir les matières</a>
        <a href="compte">👤 Voir les comptes</a>
    </div>
    <div class="main-content">
        <div class="header">
            <h1>Éditer un Compte</h1>
            <a href="compte" class="btn">Retour</a>
        </div>
        <div class="content-box">
            <form method="post" action="compte">
                <input type="hidden" name="id" value="<%= ((model.Compte)request.getAttribute("compte")).getId() %>">
                <input type="text" name="login" placeholder="Login" required value="<%= ((model.Compte)request.getAttribute("compte")).getLogin() %>">
                <input type="password" name="password" placeholder="Mot de passe" required value="<%= ((model.Compte)request.getAttribute("compte")).getPassword() %>">
                <select name="role" required>
                    <option value="user" <%= ((model.Compte)request.getAttribute("compte")).getRole().equals("user") ? "selected" : "" %>>Utilisateur</option>
                    <option value="admin" <%= ((model.Compte)request.getAttribute("compte")).getRole().equals("admin") ? "selected" : "" %>>Administrateur</option>
                </select>
                <button type="submit" class="btn">Enregistrer</button>
            </form>
        </div>
    </div>
</body>
</html>